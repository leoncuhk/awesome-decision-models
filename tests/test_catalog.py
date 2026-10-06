import copy
import json
import sys
import tempfile
import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
import render
import validate

class CatalogTests(unittest.TestCase):
    def setUp(self):
        self.cat=json.loads((ROOT/'data/catalog.json').read_text())
        self.ev=json.loads((ROOT/'data/evaluations.json').read_text())
        self.watch=json.loads((ROOT/'data/watchlist.json').read_text())
    def errors(self):return validate.validate_data(self.cat,self.ev,self.watch)
    def test_current_catalog_valid(self):self.assertEqual(self.errors(),[])
    def test_duplicate_id_rejected(self):
        self.cat['entries'].append(copy.deepcopy(self.cat['entries'][0]))
        self.assertTrue(any('duplicate' in e for e in self.errors()))
    def test_unknown_source_rejected(self):
        self.cat['entries'][0]['source_ids']=['missing-source']
        self.assertTrue(any('unresolved sources' in e for e in self.errors()))
    def test_missing_translation_rejected(self):
        self.cat['entries'][0]['caveat']['zh']=''
        self.assertTrue(any('bilingual' in e for e in self.errors()))
    def test_fraction_rejected(self):
        self.ev['records'][0]['metrics'][0]['value']=76.6
        self.assertTrue(any('outside' in e for e in self.errors()))
    def test_count_mismatch_rejected(self):
        self.ev['records'][1]['metrics'][0]['numerator']=30
        self.assertTrue(any('mismatch' in e for e in self.errors()))
    def test_nan_rejected(self):
        self.ev['records'][0]['metrics'][0]['value']=float('nan')
        self.assertTrue(any('non-finite' in e for e in self.errors()))
    def test_unsupported_reproduction_rejected(self):
        self.ev['records'][0]['reproduced_here']=True
        self.assertTrue(any('unsupported reproduction' in e for e in self.errors()))
    def test_invalid_source_pin_rejected(self):
        self.cat['sources'][0]['source_revision']='main'
        self.assertTrue(any('revision' in e for e in self.errors()))
    def test_watch_host_rejected(self):
        self.watch['sources'][0]['url']='https://evil.example/contents/README.md'
        self.assertTrue(any('unsafe' in e for e in self.errors()))
    def test_generated_documents_synced(self):
        for path,text in render.outputs().items():self.assertEqual(path.read_text(),text,str(path))
    def test_new_evidence_links_render_in_both_languages(self):
        rendered=render.outputs()
        for name in ('README.md','README.zh-CN.md'):
            for eid in ('e06','e07','e08'):
                self.assertIn(f'(docs/evidence.md#{eid})',rendered[ROOT/name])
    def test_evidence_intro_does_not_freeze_record_count(self):
        self.assertNotIn('五项记录',render.outputs()[ROOT/'docs/evidence.md'])
    def test_current_and_historical_strands_evidence_are_separate(self):
        records={r['id']:r for r in self.ev['records']}
        self.assertIn('v19',records['E07']['protocol']['task'])
        self.assertIn('v21',records['E08']['protocol']['task'])
        self.assertEqual(records['E08']['metrics'][0]['denominator'],231)
        self.assertEqual(records['E08']['metrics'][0]['numerator'],176)
    def test_new_models_and_watch_ids_remain_unique(self):
        ids={e['id'] for e in self.cat['entries']}
        self.assertTrue({'clef','strands-decider','pplx-decider'} <= ids)
        watch={e['id'] for e in self.watch['sources']}
        self.assertTrue({'strands-model','strands-v21-model','pplx-decider-model'} <= watch)
    def test_local_links_valid(self):self.assertEqual(validate.validate_local_links(ROOT),[])
    def test_escaping_local_link_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d);(p/'x.md').write_text('[escape](../secret.md)')
            self.assertTrue(any('escaping' in e for e in validate.validate_local_links(p)))
    def test_chinese_heading_slug(self):self.assertEqual(validate.slug('先看任务，而不是模型名称'),'先看任务而不是模型名称')
    def test_read_only_render_check_is_deterministic(self):self.assertEqual(render.outputs(),render.outputs())

if __name__=='__main__':unittest.main()
