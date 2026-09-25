#!/usr/bin/env python3
"""Detect source changes, not changes in model capability. Standard library only.

Default: local report/state. --issue: maintain a bot-owned GitHub review issue.
No model calls, installations, remote code execution or automatic claim edits.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import os
import re
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urlsplit
from urllib.request import HTTPRedirectHandler, Request, build_opener
ROOT=Path(__file__).resolve().parents[1]
MAX_BYTES=2_000_000
TITLE='Source watch: review queue'
MARKER='<!-- decision-models-source-watch:v1 -->'
STATE_RE=re.compile(r'<!-- decision-models-state\n(.*?)\n-->',re.S)
ALLOWED={'api.github.com','huggingface.co','docs.typesafe.ai','typesafe.ai'}

class NoRedirect(HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        # Avoid forwarding credentials or accessing unreviewed hosts.
        raise ValueError('Redirect refused; review and update the canonical URL.')


def checked_url(url: str) -> str:
    p=urlsplit(url)
    if p.scheme!='https' or p.hostname not in ALLOWED or p.username or p.password or p.port not in (None,443):
        raise ValueError('Endpoint is not on the approved HTTPS host list.')
    return p.hostname


def headers_for(url: str, token: str='') -> dict[str,str]:
    host=checked_url(url)
    headers={'User-Agent':'awesome-decision-models-source-watch/1.0','Accept':'application/json' if host=='api.github.com' or '/api/' in url else 'text/html'}
    if host=='api.github.com':
        headers['X-GitHub-Api-Version']='2022-11-28'
        if token:headers['Authorization']='Bearer '+token
    return headers


def http_bytes(url: str, token: str='', method: str='GET', payload: dict|None=None) -> bytes:
    headers=headers_for(url,token)
    if method!='GET' and urlsplit(url).hostname!='api.github.com':raise ValueError('Writes only allowed to GitHub issue endpoints.')
    data=None
    if payload is not None:data=json.dumps(payload,ensure_ascii=False).encode();headers['Content-Type']='application/json'
    request=Request(url,data=data,headers=headers,method=method)
    # Never retry a write: duplicate issue/comment creation is worse than a failed run.
    for attempt in range(3 if method=='GET' else 1):
        try:
            with build_opener(NoRedirect()).open(request,timeout=20) as response:
                result=response.read(MAX_BYTES+1)
                if len(result)>MAX_BYTES:raise ValueError('Response exceeds bounded read limit.')
                return result
        except HTTPError as exc:
            if method=='GET' and exc.code in {429,500,502,503,504} and attempt<2:time.sleep(2**attempt);continue
            raise
        except URLError:
            if method=='GET' and attempt<2:time.sleep(2**attempt);continue
            raise
    raise RuntimeError('Request did not complete')


def fingerprint(source: dict, content: bytes) -> str:
    if source['kind'] in {'github_file','hf_model'}:
        obj=json.loads(content)
        sha=obj.get('sha') if isinstance(obj,dict) else None
        if not isinstance(sha,str) or not re.fullmatch(r'[0-9a-f]{40,64}',sha):raise ValueError('Expected revision/blob SHA absent; not recording a change.')
        return sha
    if source['kind']=='web_page':return hashlib.sha256(content).hexdigest()
    raise ValueError('Unknown source kind')


def scan(sources: list[dict], previous: dict, fetcher=http_bytes, token: str='') -> tuple[dict,list[dict],list[dict]]:
    next_state=dict(previous); changes=[]; errors=[]
    for source in sources:
        sid=source['id']
        try:
            checked_url(source['url'])
            current=fingerprint(source,fetcher(source['url'],token=token))
            old=previous.get(sid)
            if old is not None and old!=current:changes.append({'id':sid,'before':old,'after':current,'url':source['url'],'meaning':source['meaning']})
            next_state[sid]=current
        except (ValueError,TypeError,KeyError,OSError,HTTPError,URLError) as exc:
            # Preserve the last successful value; a fetch error is not a release.
            code=f'HTTP {exc.code}' if isinstance(exc,HTTPError) else type(exc).__name__
            errors.append({'id':sid,'error':code,'url':source['url']})
    # Deliberately retain removed IDs until a human reviews the state; no silent reset.
    return next_state,changes,errors


def safe(text: str) -> str:
    return re.sub(r'[\r\n|<>`]',' ',str(text))[:200]


def report(sources: list[dict], previous: dict, state: dict, changes: list[dict], errors: list[dict], now: str) -> str:
    new=sum(s['id'] not in previous and s['id'] in state for s in sources)
    lines=['# Source watch', '', f'Checked: {now}', '', f'Sources: {len(sources)}; changed: {len(changes)}; newly baselined: {new}; fetch errors: {len(errors)}.', '',
      '**This detects source changes, not improved model quality.** A model-repository SHA can change because of documentation. Raw HTML changes may be noise. No scientific claims, model weights or repository files were automatically changed.', '']
    if changes:
        lines += ['## Changes requiring review','','| Source | Previous → current | Review question |','| --- | --- | --- |']
        for c in changes:lines.append(f"| [{safe(c['id'])}]({c['url']}) | `{c['before'][:12]}` → `{c['after'][:12]}` | {safe(c['meaning'])} |")
    if errors:
        lines += ['','## Fetch errors','', 'Previous successful fingerprints were preserved. An error is not evidence of a release, regression or abandoned project.','']
        lines += [f"- [{safe(e['id'])}]({e['url']}): {safe(e['error'])}" for e in errors]
    if new:lines += ['','New sources were baselined; their current versions are not claimed to be new releases.']
    return '\n'.join(lines)+'\n'


def api(repo: str, suffix: str, token: str, method: str='GET', payload: dict|None=None):
    if not re.fullmatch(r'[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+',repo):raise ValueError('Invalid owner/repository identifier')
    return json.loads(http_bytes(f'https://api.github.com/repos/{repo}/{suffix}',token,method,payload))


def find_issue(repo: str,token: str) -> dict|None:
    # Listing all states keeps the most recent baseline even when someone closed the queue.
    for page in range(1,21):
        items=api(repo,f'issues?state=all&per_page=100&page={page}',token)
        if not isinstance(items,list):raise ValueError('Unexpected issues response')
        for issue in items:
            user=issue.get('user',{})
            if issue.get('title')==TITLE and MARKER in (issue.get('body') or '') and user.get('type')=='Bot' and 'pull_request' not in issue:return issue
        if len(items)<100:return None
    raise ValueError('Issue discovery exceeded 2,000 items; refusing to create a duplicate queue.')


def read_issue_state(body: str) -> dict:
    match=STATE_RE.search(body)
    if not match:raise ValueError('Existing watcher issue lacks valid state; refusing to reset its baseline.')
    state=json.loads(match.group(1))
    if not isinstance(state,dict) or any(not isinstance(k,str) or not isinstance(v,str) or not re.fullmatch(r'[0-9a-f]{40,64}',v) for k,v in state.items()):raise ValueError('Invalid stored fingerprints')
    return state


def issue_body(text: str,state: dict) -> str:
    body=MARKER+'\n'+text+'\n<!-- decision-models-state\n'+json.dumps(state,sort_keys=True)+'\n-->\n'
    if len(body)>60000:raise ValueError('Issue body exceeds safe bound')
    return body


def main() -> int:
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--issue',action='store_true',help='Write a bot-owned GitHub review issue using GITHUB_TOKEN.')
    p.add_argument('--repo',default=os.environ.get('GITHUB_REPOSITORY',''))
    p.add_argument('--state',type=Path,default=ROOT/'.source-watch-state.json')
    p.add_argument('--output',type=Path,default=ROOT/'reports/source-watch.md')
    args=p.parse_args()
    token=os.environ.get('GITHUB_TOKEN','')
    sources=json.loads((ROOT/'data/watchlist.json').read_text())['sources']
    issue=None
    try:
        if args.issue:
            if not token or not args.repo:raise ValueError('--issue needs GITHUB_TOKEN and owner/repo.')
            if os.environ.get('GITHUB_ACTIONS')!='true':raise ValueError('--issue is restricted to GitHub Actions; use local report mode outside Actions.')
            issue=find_issue(args.repo,token)
            previous=read_issue_state(issue.get('body') or '') if issue else {}
        else:
            previous=json.loads(args.state.read_text()) if args.state.exists() else {}
            if not isinstance(previous,dict):raise ValueError('Local state must be an object')
        state,changes,errors=scan(sources,previous,token=token)
        now=datetime.now(timezone.utc).isoformat(timespec='seconds')
        text=report(sources,previous,state,changes,errors,now)
        args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(text)
        if args.issue:
            body=issue_body(text,state)
            if issue:
                # Archive material changes before replacing the current status body.
                if changes or errors:api(args.repo,f"issues/{issue['number']}/comments",token,'POST',{'body':text})
                payload={'body':body}
                if changes or errors:payload['state']='open'
                api(args.repo,f"issues/{issue['number']}",token,'PATCH',payload)
            else:api(args.repo,'issues',token,'POST',{'title':TITLE,'body':body})
        else:
            args.state.parent.mkdir(parents=True,exist_ok=True)
            temp=args.state.with_name(args.state.name+'.tmp');temp.write_text(json.dumps(state,indent=2)+'\n');temp.replace(args.state)
        print(text)
        # A partial fetch failure is visible in the report/issue AND marks the run unsuccessful.
        return 1 if errors else 0
    except (ValueError,TypeError,KeyError,OSError,HTTPError,URLError) as exc:
        print('Source watch failed: '+(f'HTTP {exc.code}' if isinstance(exc,HTTPError) else type(exc).__name__+': '+str(exc)),file=sys.stderr)
        return 2
if __name__=='__main__':raise SystemExit(main())
