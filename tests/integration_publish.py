"""Exercise publish.sh against disposable LOCAL remotes. No GitHub calls."""
import os,subprocess,tempfile
from pathlib import Path
R=Path(__file__).resolve().parents[1]
def run(args,env=None,check=True):
 return subprocess.run(args,text=True,capture_output=True,env=env,check=check)
with tempfile.TemporaryDirectory() as tmp:
 t=Path(tmp);remote=t/'remote.git';bindir=t/'bin';bindir.mkdir()
 run(['git','init','--bare',str(remote)])
 gh=bindir/'gh'
 gh.write_text('''#!/usr/bin/env python3
import os,subprocess,sys
args=sys.argv[1:]
if args[:2]==['auth','status']: sys.exit(0)
if args[0]=='api':
 q=args[-1]
 print('true' if q=='.permissions.push' else 'main')
 sys.exit(0)
if args[:2]==['repo','clone']:
 sys.exit(subprocess.call(['git','clone',os.environ['FAKE_GH_REMOTE'],args[3]]))
raise SystemExit('Unexpected gh call')
''');gh.chmod(0o755)
 env=os.environ.copy();env['PATH']=str(bindir)+':'+env['PATH'];env['FAKE_GH_REMOTE']=str(remote)
 env.update(GIT_AUTHOR_NAME='Local test',GIT_AUTHOR_EMAIL='local-test@example.invalid',GIT_COMMITTER_NAME='Local test',GIT_COMMITTER_EMAIL='local-test@example.invalid')
 # These author fields exist only in a disposable local test environment.
 res=run(['bash',str(R/'scripts/publish.sh'),'test/empty','--dry-run'],env)
 assert 'Nothing committed or pushed' in res.stdout
 assert not run(['git','--git-dir',str(remote),'show-ref'],check=False).stdout
 print('PASS: dry run leaves empty remote unchanged')
 res=run(['bash',str(R/'scripts/publish.sh'),'test/empty','--yes'],env)
 assert 'Published to' in res.stdout
 files=run(['git','--git-dir',str(remote),'ls-tree','--name-only','-r','main']).stdout.splitlines()
 assert 'README.md' in files and '.github/workflows/source-watch.yml' in files
 assert not any('__pycache__' in p or p.startswith('.env') for p in files)
 before=run(['git','--git-dir',str(remote),'rev-parse','main']).stdout
 print('PASS: empty local remote initialized with complete files, without caches')
 res=run(['bash',str(R/'scripts/publish.sh'),'test/empty','--yes'],env,check=False)
 assert res.returncode==4 and 'REFUSED' in res.stderr
 assert run(['git','--git-dir',str(remote),'rev-parse','main']).stdout==before
 print('PASS: nonempty remote refused; existing commit unchanged')
