import json
from pathlib import Path
data=json.loads(Path(__file__).with_name('revision-results.json').read_text())
hooks=[r for r in data['remaining'] if tuple(map(len,r['source']))==(3,1,1,1)]
print(json.dumps({'hooks':hooks,'first_pair':next(r for r in data['remaining'] if tuple(map(len,r['source']))==(2,2,1,1))},indent=2))
