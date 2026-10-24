"""Metadata-only freeze builder; never imports or runs a research candidate."""
from pathlib import Path
import datetime as dt
import hashlib
import json

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
raw=ROOT/'.runs/phase2-20261025'
records=[json.loads(line) for line in (raw/'subprocess.jsonl').read_text().splitlines()]
attempts=[r for r in records if r['label'].startswith('tableau-revision-')]
files=set(HERE.glob('revision*'))
files.discard(HERE/'revision-freeze.json')
files.update(HERE/name for name in ('freeze.json','author.md','structural.py','inventory.py','cancellation.py','structural-initial.py'))
files.add(ROOT/'research/partitions/checks/tableaux.py')
for row in attempts:
    files.update((Path(row['stdout']),Path(row['stderr'])))
manifest={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest()
          for p in sorted(files) if p.is_file()}
packet={'status':'author_frozen_pending_distinct_final_review',
        'frozen_utc':dt.datetime.now(dt.timezone.utc).isoformat(),
        'scope':'single reserved refinement within frozen family2; n=6 only',
        'stage_start_utc':'2026-10-24T22:28:48+00:00',
        'claim':'intrinsic local partial injection proved; full 132-order domain coverage exhaustively checked',
        'numeric_result':{'negative':3980,'mapped':3980,'positive_tested':6800,'original_preserved':151,'remaining':0,'failures':0},
        'resource_receipt':{'revision_subprocess_attempts':len(attempts),
           'revision_subprocess_wall_seconds':sum(r['wall_seconds'] for r in attempts),
           'revision_subprocess_cpu_seconds':sum(r['cpu_seconds'] for r in attempts),
           'revision_peak_rss_bytes':max(r['peak_rss_bytes'] for r in attempts),
           'charged_indices':[r['index'] for r in attempts],
           'note':'freeze builder itself is metadata-only; running meter may record it after this snapshot'},
        'prior_preliminary_pin_note':'Two preliminary pins describe pre-triangle sources; exact originals retained/recovered. Final original17-file freeze is unchanged.',
        'sha256':manifest}
(HERE/'revision-freeze.json').write_text(json.dumps(packet,indent=2)+'\n')
print(json.dumps({'frozen_files':len(manifest),'resources':packet['resource_receipt'],
                  'freeze_sha256':hashlib.sha256((HERE/'revision-freeze.json').read_bytes()).hexdigest()},indent=2))
