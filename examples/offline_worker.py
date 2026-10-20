"""Synthetic protocol worker. Does not use a model or perform research."""

import json
import sys


request = json.load(sys.stdin)
upstream = [item["step_id"] for item in request["upstream"]]
json.dump({
    "summary": f"SYNTHETIC PROTOCOL FIXTURE: received {request['step']['id']} for role {request['agent']['id']}; upstream stages: {upstream}. No sources inspected, proofs checked, experiments run, or model calls made.",
    "claims": [{
        "text": "This response exercises dispatch and dependency plumbing only; it establishes no research result.",
        "status": "unverified",
    }],
    "artifacts": [],
}, sys.stdout)
sys.stdout.write("\n")
