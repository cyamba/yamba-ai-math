---
name: bench-dashboard
description: Publish or update the private yamba-ai-math benchmark radar dashboard artifact from the tracked records. Meta-harness only.
disable-model-invocation: true
argument-hint: [--snapshots]
---

# Benchmark dashboard

The dashboard is a private claude.ai artifact made from the Dashboard artifact type. Its URL is in
`.claude/bench/dashboard.json`. Its page is `.claude/bench/dashboard/page.html`; its six datasets
(`records`, `scores`, `gates`, `notes`, `metrics`, `trajectory`) are JSON files exported from the records.

1. `python3 .claude/bench/bench.py export-artifact [--snapshots]`. It prints the export directory, which
   holds `<dataset>.json`, `manifest.json` (titles, descriptions) and `index.doc.json` (the page).
2. Upload each `<dataset>.json` to the artifact's asset store (Artifact publish, `url`, `asset: true`,
   one JSON file per call) and note each returned `url`.
3. Read the artifact's `datasets` and `files` documents with `ArtifactData`, then write one `batch`:
   `update` each `datasets/<id>` with `source: {kind: "file", url, name: "<id>.json", format: "json"}`
   and `updated: {at: <now ISO>, by: "yambench"}` (`set` with `title` and `description` from the manifest
   when it does not exist yet), and `update` `files/index.html` from `index.doc.json` when the page
   changed. Pin each existing document with its `if_version`.
4. Read `data/users/me` doc `check` as the Dashboard type describes; fix only what it confirms.
5. Open the artifact. For an offline copy, `python3 .claude/bench/bench.py dashboard` writes a
   self-contained HTML file with the same page and data.
