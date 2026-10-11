#!/usr/bin/env python3
"""Render documentation from curated JSON. No network and no third-party packages."""
from __future__ import annotations
import argparse
import json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]

def cell(text: str) -> str:
    return text.replace('|', '\\|').replace('\n', ' ')

def outputs(root: Path = ROOT) -> dict[Path, str]:
    cat = json.loads((root/'data/catalog.json').read_text())
    evs = json.loads((root/'data/evaluations.json').read_text())['records']
    entries, sources = cat['entries'], {s['id']:s for s in cat['sources']}
    core = [e for e in entries if e['category']=='core_models']
    out = {}
    for lang, template, target in [('en','README.en.md','README.md'),('zh','README.zh.md','README.zh-CN.md')]:
        text=(root/'templates'/template).read_text()
        h = ['Model','Mechanism / proposition','Useful experiment','Important limitation'] if lang=='en' else ['模型','机制／定位','适合的实验','重要限制']
        table=['| '+' | '.join(h)+' |','| --- | --- | --- | --- |']
        for e in core:
            name=f"[{e['name']}]({e['url']})"
            table.append('| '+' | '.join([name,cell(e['summary'][lang]),cell(e['use'][lang]),cell(e['caveat'][lang])])+' |')
        replacements={'DATE':cat['reviewed_on'],'ENTRY_COUNT':str(len(entries)),'CORE_COUNT':str(len(core)),'EVIDENCE_COUNT':str(len(evs)),'CORE_TABLE':'\n'.join(table)}
        short_zh={
          'E01':'Laya：专项训练收益与校准数据问题需要分开。',
          'E02':'CLM：在 38 个保留任务上选择候选，不是独立完成编码。',
          'E03':'Nimble / Jev：配对人工标签评测仍须按任务解读。',
          'E04':'GLiNER2.5-Decide：新评测范围、来源可见性与名称辨别。',
          'E05':'Kev：区分开发集、测试集与来源域。',
          'E06':'Clef：厂商比较中的任务取舍，不是通用胜出。',
          'E07':'Strands Decider：问题指令敏感性与实验选择限制。',
          'E08':'Strands v21：发布种子与同机多种子比较。',
          'E09':'Drex v1.5：公开套件平局与基准训练重叠。',
          'E10':'Microsoft-Decision-1：作者报告的扰动稳定性。',
          'E11':'Strands Qwen v1：新配方、种子平均及缺图限制。'}
        replacements['EVIDENCE_LINKS']='\n'.join(f"- [{e['id']} — {e['title'] if lang=='en' else short_zh[e['id']]}](docs/evidence.md#{e['id'].lower()})" for e in evs)
        for category in ['baselines','routing','reliability','evaluation','foundations','related_lists']:
            lines=[]
            for e in entries:
                if e['category']!=category:continue
                line=f"- **[{e['name']}]({e['url']})** — {e['summary'][lang]} {e['caveat'][lang]}"
                lines.append(line)
            replacements[category.upper()]='\n'.join(lines)
        for key,value in replacements.items():text=text.replace('{{'+key+'}}',value)
        out[root/target]=text
    models=['# Model cards / 模型卡','', '[Home](../README.md) · [中文首页](../README.zh-CN.md) · [Evidence](evidence.md)','',f"Source review: {cat['reviewed_on']}. These are source-backed descriptions and curatorial use cases, not production certifications.",'','`Unknown` is intentional. An inspected source revision does not identify the deployed weight revision. Language support, licenses and resource requirements must be checked for the exact artifact. Recorded weight identifiers are source-reported unless a local binary verification is explicitly documented; recording an identifier is not a claim that the weights were downloaded or hashed here.','']
    for e in core:
        models += [f"<a id=\"{e['id']}\"></a>",f"## {e['name']}",'',f"[Project / model]({e['url']})",'',e['summary']['en'],e['summary']['zh'],'','| Dimension | English | 中文 |','| --- | --- | --- |']
        for key,label in [('scale','Scale'),('mechanism','Mechanism'),('training','Training'),('availability','Deployment'),('use','Suggested use'),('caveat','Boundary')]:
            models.append('| '+label+' | '+cell(e[key]['en'])+' | '+cell(e[key]['zh'])+' |')
        models += ['',f"**License note:** {e['license_note']}",f"**Recorded weight identifier:** {e['weight_revision'] or 'Unknown / not pinned'}",'','**Sources:** '+'; '.join(f"[{sources[s]['title']}]({sources[s]['url']})" for s in e['source_ids']), '']
    out[root/'docs/models.md']='\n'.join(models)+'\n'
    evid=['# Evidence ledger / 评测证据','', '[Home](../README.md) · [中文首页](../README.zh-CN.md) · [Methodology](methodology.md)','','These are **archival claim records**, not a common leaderboard. None was rerun by this repository. A source review checks what was reported, not whether the underlying experiment is reproducible or unbiased.','','本页保存带条件的历史声明，不生成混合排名。所列记录均为来源报告，不是本仓库独立复现。来源阅读、产物审计与实验复现是三种不同工作。','', 'Reported fractions are displayed as percentages where appropriate. More printed digits do not imply greater statistical precision. Source publication dates remain unknown unless independently established.','']
    for e in evs:
        evid += [f"<a id=\"{e['id'].lower()}\"></a>",f"## {e['id']} · {e['title']}",'',f"**Evidence:** `{e['evidence_type']}` · **Reviewed:** {e['reviewed_on']} · **Reproduced here:** no",'', '| Protocol | Recorded context |','| --- | --- |']
        for k,v in e['protocol'].items():evid.append('| '+k.replace('_',' ').capitalize()+' | '+cell(v)+' |')
        evid += ['','| Reported measurement | Value |','| --- | --- |']
        for m in e['metrics']:
            val=f"{m['value']*100:.2f}%" if m['unit']=='fraction' else str(m['value'])
            if 'numerator'in m:val=f"{m['numerator']}/{m['denominator']} ({val})"
            evid.append('| '+cell(m['label'])+' | '+val+' |')
        evid += ['',f"**Interpretation:** {e['conclusion']}",'']+['- '+c for c in e['caveats']]+['','**Artifacts and limits:**']
        evid += ['- '+k.replace('_',' ')+': '+str(v) for k,v in e['artifacts'].items()]
        evid += ['','**Sources:** '+'; '.join(f"[{sources[s]['title']}]({sources[s]['url']})" for s in e['source_ids']), '']
    out[root/'docs/evidence.md']='\n'.join(evid)+'\n'
    sr=['# Source register / 来源登记','', '[Home](../README.md) · [Methodology](methodology.md)','','`content_reviewed`: relevant body text inspected, not every linked artifact. `abstract_reviewed`: abstract and publication metadata only. `source_revision`: immutable source-text revision when captured, **not weight provenance**. Unknown fields are not silently filled from memory.','','`content_reviewed` 仅表示已检查相关正文，不代表逐个运行所有附件；`abstract_reviewed` 表示摘要与元数据层面的阅读。部分无法打开的模型／数据卡已在相应条目中明确说明。','']
    for s in cat['sources']:
        sr += [f"<a id=\"{s['id']}\"></a>",f"## {s['title']}",'',f"- Source: {s['url']}",f"- Kind: `{s['kind']}`; review depth: `{s['review_depth']}`; reviewed: {s['reviewed_on']}",f"- Source revision: `{s['source_revision'] or 'not captured / live URL'}`"]
        if s['review_note']:sr.append('- Note: '+s['review_note'])
        sr.append('')
    out[root/'docs/sources.md']='\n'.join(sr)+'\n'
    return out

def main() -> int:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check',action='store_true',help='Fail if generated files differ; do not write.')
    args=parser.parse_args()
    changed=[]
    for path,text in outputs().items():
        if not path.exists() or path.read_text()!=text:
            changed.append(str(path.relative_to(ROOT)))
            if not args.check:path.parent.mkdir(parents=True,exist_ok=True);path.write_text(text)
    if args.check and changed:
        print('Out-of-date generated files: '+', '.join(changed));return 1
    print(('Checked' if args.check else 'Rendered')+' 5 generated documents.')
    return 0
if __name__=='__main__':raise SystemExit(main())
