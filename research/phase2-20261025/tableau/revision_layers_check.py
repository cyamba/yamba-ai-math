"""Reuses the explicit exhaustive check with the local layers selected."""
import json
from pathlib import Path
import revision_check as check
from revision_layers import forward,inverse
check.forward=forward
check.inverse=inverse
result=check.run()
Path(__file__).with_name('revision-layers-results.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k not in ('remaining','all_results')},indent=2))
if result['remaining']:print(json.dumps({'first_remaining':result['remaining'][0]},indent=2))
raise SystemExit(bool(result['failures']))
