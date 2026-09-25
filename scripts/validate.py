#!/usr/bin/env python3
"""Offline structural validation. This does not certify external facts or URLs."""
from __future__ import annotations
import json
import math
import re
import sys
from datetime import date
from pathlib import Path
from urllib.parse import unquote, urlsplit
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
import render
CATEGORIES={'core_models','baselines','routing','reliability','evaluation','foundations','related_lists'}
SOURCE_KINDS={'repository','official_publication','official_docs','model_card','evaluation_report','paper','curated_list'}


def validate_data(cat: dict, evidence: dict, watch: dict) -> list[str]:
    errors=[]
    def fail(message): errors.append(message)
    def unique(items,label):
        ids=[x.get('id') for x in items]
        if any(not isinstance(i,str) or not i for i in ids):fail(f'{label}: missing ID')
        if len(ids)!=len(set(ids)):fail(f'{label}: duplicate ID')
        return set(ids)
    def valid_date(value,label):
        try: date.fromisoformat(value)
        except (ValueError,TypeError):fail(f'{label}: invalid date')
    def https(url,label):
        p=urlsplit(url)
        if p.scheme!='https' or not p.hostname or p.username or p.password:fail(f'{label}: must be a public HTTPS URL without credentials')
    for doc in (cat,evidence,watch):
        if doc.get('schema_version')!=1:fail('Unsupported schema_version')
    valid_date(cat.get('reviewed_on'),'catalog')
    srcids=unique(cat['sources'],'sources'); eids=unique(cat['entries'],'entries')
    unique(evidence['records'],'evidence');unique(watch['sources'],'watchlist')
    for s in cat['sources']:
        https(s['url'],s['id']);valid_date(s['reviewed_on'],s['id'])
        if s['kind'] not in SOURCE_KINDS:fail(f"{s['id']}: invalid source kind")
        if s['review_depth'] not in {'content_reviewed','abstract_reviewed','metadata_only'}:fail(f"{s['id']}: invalid review depth")
        rev=s.get('source_revision')
        if rev is not None and not re.fullmatch(r'[0-9a-f]{40}',rev):fail(f"{s['id']}: invalid source revision")
    for e in cat['entries']:
        https(e['url'],e['id']);valid_date(e['reviewed_on'],e['id'])
        if e['category'] not in CATEGORIES:fail(f"{e['id']}: invalid category")
        if not e['source_ids'] or set(e['source_ids'])-srcids:fail(f"{e['id']}: unresolved sources")
        keys=['summary','use','caveat']+(['scale','mechanism','training','availability'] if e['category']=='core_models' else [])
        for key in keys:
            if any(not e.get(key,{}).get(lang,'').strip() for lang in ('en','zh')):fail(f"{e['id']}: missing bilingual {key}")
        if e['category']=='core_models' and ('weight_revision' not in e or not e.get('license_note')):fail(f"{e['id']}: missing provenance/license field")
    for r in evidence['records']:
        valid_date(r['reviewed_on'],r['id'])
        if not r['source_ids'] or set(r['source_ids'])-srcids:fail(f"{r['id']}: unresolved sources")
        if not r['model_ids'] or set(r['model_ids'])-eids:fail(f"{r['id']}: unresolved model IDs")
        if r['evidence_type'] not in {'author_reported','third_party_reported','reproduced_here','unverified_claim'}:fail(f"{r['id']}: invalid evidence type")
        for key in ('task','test_unit','split','reference','training','measurement','hardware'):
            if not r.get('protocol',{}).get(key):fail(f"{r['id']}: missing protocol {key}")
        if not r.get('caveats') or not r.get('artifacts'):fail(f"{r['id']}: missing limitations or artifact status")
        if not isinstance(r.get('reproduced_here'),bool):fail(f"{r['id']}: reproduction flag must be boolean")
        if r.get('reproduced_here'):
            rep=r.get('reproduction',{})
            if r['evidence_type']!='reproduced_here' or not all(rep.get(k) for k in ('evaluator','environment','command','artifact_path')):fail(f"{r['id']}: unsupported reproduction claim")
        for m in r['metrics']:
            x=m['value']
            if isinstance(x,bool) or not isinstance(x,(int,float)) or not math.isfinite(x):fail(f"{r['id']}: non-finite metric");continue
            if m['unit']=='fraction' and not 0<=x<=1:fail(f"{r['id']}: fraction outside [0,1]")
            if 'numerator' in m or 'denominator' in m:
                n,d=m.get('numerator'),m.get('denominator')
                if not isinstance(n,int) or not isinstance(d,int) or d<=0 or not 0<=n<=d:fail(f"{r['id']}: invalid counts")
                elif not math.isclose(n/d,x,abs_tol=1e-6):fail(f"{r['id']}: count/value mismatch")
    for s in watch['sources']:
        https(s['url'],s['id']);p=urlsplit(s['url'])
        if not s.get('meaning'):fail(f"{s['id']}: missing change semantics")
        if s['kind']=='github_file' and (p.hostname!='api.github.com' or '/contents/' not in p.path):fail(f"{s['id']}: unsafe GitHub endpoint")
        elif s['kind']=='hf_model' and (p.hostname!='huggingface.co' or not p.path.startswith('/api/models/')):fail(f"{s['id']}: unsafe Hugging Face endpoint")
        elif s['kind']=='web_page' and p.hostname not in {'docs.typesafe.ai','typesafe.ai'}:fail(f"{s['id']}: unapproved page host")
        elif s['kind'] not in {'github_file','hf_model','web_page'}:fail(f"{s['id']}: unsupported watch kind")
    return errors


def slug(text: str) -> str:
    text=re.sub(r'<[^>]*>','',text).strip().lower()
    return ''.join(ch for ch in text if ch.isalnum() or ch in ' -_').replace(' ','-')


def validate_local_links(root: Path) -> list[str]:
    errors=[]
    link=re.compile(r'(?<!!)\[[^\]\n]*\]\(([^\s)]+)\)')
    for path in root.rglob('*.md'):
        if any(part in {'.git','reports','__pycache__','templates'} for part in path.relative_to(root).parts):continue
        text=path.read_text(encoding='utf-8')
        # Ignore fenced code; paths in shell examples are not Markdown links.
        text=re.sub(r'```.*?```','',text,flags=re.S)
        for target in link.findall(text):
            p=urlsplit(target)
            if p.scheme or p.netloc:continue
            dest=(path.parent/unquote(p.path)).resolve() if p.path else path.resolve()
            if not dest.is_relative_to(root.resolve()):errors.append(f'{path.relative_to(root)}: escaping link {target}');continue
            if not dest.exists():errors.append(f'{path.relative_to(root)}: missing local link {target}');continue
            if p.fragment and dest.suffix=='.md':
                body=dest.read_text(encoding='utf-8')
                ids=set(re.findall(r'<a\s+id=["\']([^"\']+)["\']',body))
                ids.update(slug(x) for x in re.findall(r'^#{1,6}\s+(.+)$',body,flags=re.M))
                if unquote(p.fragment) not in ids:errors.append(f'{path.relative_to(root)}: missing anchor {target}')
    return errors


def validate(root: Path=ROOT) -> list[str]:
    try:
        cat=json.loads((root/'data/catalog.json').read_text())
        ev=json.loads((root/'data/evaluations.json').read_text())
        watch=json.loads((root/'data/watchlist.json').read_text())
        errors=validate_data(cat,ev,watch)
        for path,text in render.outputs(root).items():
            if not path.exists() or path.read_text()!=text:errors.append(f'Generated file out of date: {path.relative_to(root)}')
        errors.extend(validate_local_links(root))
        return errors
    except (OSError,KeyError,TypeError,ValueError) as exc:return [f'Validation could not complete: {exc}']


def main() -> int:
    errors=validate()
    if errors:
        print('\n'.join('ERROR: '+e for e in errors));return 1
    print('PASS: schema, references, bilingual fields, numerical records, generated files and local Markdown links.')
    print('Not checked: public URL reachability, model execution, factual truth or benchmark reproduction.')
    return 0
if __name__=='__main__':raise SystemExit(main())
