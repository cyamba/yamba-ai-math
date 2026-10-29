#!/usr/bin/env python3
"""Stop hook: snapshot the armed benchmark run, silently. It never blocks or fails a session."""

import contextlib
import io
import sys
from pathlib import Path

BENCH = Path(__file__).resolve().parents[1] / "bench"
sys.path.insert(0, str(BENCH))

captured = io.StringIO()
try:
    with contextlib.redirect_stdout(captured), contextlib.redirect_stderr(captured):
        from yambench.cli import main

        main(["snapshot", "--hook", "--quiet"])
except BaseException as error:  # noqa: BLE001 - a hook must always exit 0
    captured.write(f"{type(error).__name__}: {error}\n")
log_dir = BENCH.parents[1] / ".runs" / "bench"
if captured.getvalue() and log_dir.is_dir():
    with open(log_dir / "hook.log", "a", encoding="utf-8") as log:
        log.write(captured.getvalue())
sys.exit(0)
