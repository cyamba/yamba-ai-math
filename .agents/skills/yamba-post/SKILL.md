---
name: yamba-post
description: Capture a useful side finding or handoff in the canonical repository and, when requested, deliver an actionable note to the configured recipient's YambaPost Google Drive inbox.
---

# Capture now, investigate in the right project later

Preserve useful side findings without expanding the active KR1 investigation.
First create a short canonical local note, or add a parked item to
[feedback.md](../../../research/rogers-ramanujan/feedback.md). Include ID, project,
kind, PENDING status, evidence/assurance, why it may matter elsewhere, next action,
and source/result links. State the receiving project if known; do not invent one.
Label speculation and unvalidated workflow hypotheses. Capturing is not investigating.

## Configuration (never committed)

Delivery targets belong to the operator of the current checkout and live outside
tracked files. Resolve each value from the environment first, then from
`.agents/local/yamba-post.json` (gitignored; copy `yamba-post.example.json` next
to this file):

| Key | Meaning |
| --- | --- |
| `YAMBAPOST_RECIPIENT` | Handle of the operator who may authorize posts, written `@recipient` below |
| `YAMBAPOST_INBOX_FOLDER_ID` | Google Drive folder ID of that operator's YambaPost inbox |
| `YAMBAPOST_FORMAT_REF_FILE_ID` | Google Drive file ID of the inbox format reference |

Fail closed: if any value is missing, do not call Drive. Keep the local draft and
report delivery as `PENDING (YambaPost not configured)`. Never guess, search for,
or reuse a folder or file ID from git history, documentation, issues or another
repository.

## Delivery

When `@recipient` explicitly requests posting to YambaPost, resolve the
configuration, then load the installed Google Drive skill and follow it. The inbox
is the folder `YAMBAPOST_INBOX_FOLDER_ID`; inspect the format reference
`YAMBAPOST_FORMAT_REF_FILE_ID` before writing. Check for duplicates by ID and topic
before creating a note. Include the required ID, project, kind, PENDING status, next
action and source/result links. Preserve the canonical repository copy and provide
a usable repository reference or self-contained question when a local path is
inaccessible to the recipient.

Read back the saved Drive content before claiming delivery; record its link and
verified delivery state locally. Update a matching existing note rather than
creating a duplicate when authorized. If the connector or Drive skill is unavailable,
keep the local draft and report delivery pending. Do not check the inbox at session
start or post merely because this skill was loaded. An authorized post requires no
additional ritual confirmation, but does not authorize unrelated messages.
