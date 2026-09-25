import json
import sys
import unittest
from pathlib import Path
from urllib.error import URLError
from urllib.request import Request
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
import watch_sources as w

A='a'*40
B='b'*40
SOURCE={'id':'example','kind':'github_file','url':'https://api.github.com/repos/example/repo/contents/README.md','meaning':'Inspect the changed source, not a claim of improvement.'}

class WatcherTests(unittest.TestCase):
    def test_token_only_sent_to_github(self):
        self.assertIn('Authorization',w.headers_for(SOURCE['url'],'secret'))
        self.assertNotIn('Authorization',w.headers_for('https://huggingface.co/api/models/a/b','secret'))
        self.assertNotIn('Authorization',w.headers_for('https://docs.typesafe.ai/primitives','secret'))
    def test_untrusted_host_rejected(self):
        with self.assertRaises(ValueError):w.headers_for('https://api.github.com.evil.example/x','secret')
    def test_plain_http_rejected(self):
        with self.assertRaises(ValueError):w.checked_url('http://api.github.com/x')
    def test_url_credentials_rejected(self):
        with self.assertRaises(ValueError):w.checked_url('https://user:secret@api.github.com/x')
    def test_nonstandard_port_rejected(self):
        with self.assertRaises(ValueError):w.checked_url('https://api.github.com:8443/x')
    def test_redirect_refused(self):
        with self.assertRaises(ValueError):w.NoRedirect().redirect_request(Request(SOURCE['url']),None,302,'moved',{},'https://evil.example')
    def test_api_fingerprint(self):self.assertEqual(w.fingerprint(SOURCE,json.dumps({'sha':A}).encode()),A)
    def test_api_error_not_fingerprint(self):
        with self.assertRaises(ValueError):w.fingerprint(SOURCE,b'{"message":"rate limit"}')
    def test_html_hash_stable(self):
        s=dict(SOURCE,kind='web_page');self.assertEqual(w.fingerprint(s,b'hello'),w.fingerprint(s,b'hello'))
        self.assertNotEqual(w.fingerprint(s,b'hello'),w.fingerprint(s,b'world'))
    def test_first_run_is_baseline_not_change(self):
        state,changes,errors=w.scan([SOURCE],{},fetcher=lambda *a,**k:json.dumps({'sha':A}).encode())
        self.assertEqual(state,{'example':A});self.assertEqual(changes,[]);self.assertEqual(errors,[])
    def test_unchanged_has_no_alert(self):
        state,changes,errors=w.scan([SOURCE],{'example':A},fetcher=lambda *a,**k:json.dumps({'sha':A}).encode())
        self.assertEqual(changes,[]);self.assertEqual(errors,[])
    def test_changed_detected(self):
        state,changes,errors=w.scan([SOURCE],{'example':A},fetcher=lambda *a,**k:json.dumps({'sha':B}).encode())
        self.assertEqual(state['example'],B);self.assertEqual(changes[0]['before'],A);self.assertEqual(errors,[])
    def test_network_error_preserves_good_state(self):
        def fail(*a,**k):raise URLError('offline')
        state,changes,errors=w.scan([SOURCE],{'example':A},fetcher=fail)
        self.assertEqual(state['example'],A);self.assertEqual(changes,[]);self.assertEqual(len(errors),1)
    def test_malformed_response_preserves_good_state(self):
        state,changes,errors=w.scan([SOURCE],{'example':A},fetcher=lambda *a,**k:b'not json')
        self.assertEqual(state['example'],A);self.assertEqual(changes,[]);self.assertEqual(len(errors),1)
    def test_state_roundtrip(self):
        body=w.issue_body('report',{'example':A})
        self.assertEqual(w.read_issue_state(body),{'example':A})
    def test_bad_issue_state_refuses_reset(self):
        with self.assertRaises(ValueError):w.read_issue_state('a human removed the state')
    def test_bad_fingerprint_in_state_refused(self):
        with self.assertRaises(ValueError):w.read_issue_state('<!-- decision-models-state\n{"example":"run arbitrary code"}\n-->')
    def test_report_distinguishes_new_source(self):
        text=w.report([SOURCE],{}, {'example':A},[],[],'2026-09-25T00:00:00+00:00')
        self.assertIn('changed: 0',text);self.assertIn('newly baselined: 1',text)
    def test_sanitize_untrusted_line(self):self.assertNotIn('\n',w.safe('x\n<script>|`'))

if __name__=='__main__':unittest.main()
