import json
from pathlib import Path
import revision_extension as diagnostic
from revision_layers import forward
diagnostic.forward=forward
result=diagnostic.run()
Path(__file__).with_name('revision-extension-layers-results.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='all_results'},indent=2))
