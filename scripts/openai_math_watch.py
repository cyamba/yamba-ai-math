"""Offline diff of a local openai/math checkout against the recorded watch baseline.

Usage:
    python3 scripts/openai_math_watch.py report <path-to-openai-math-checkout>
    python3 scripts/openai_math_watch.py snapshot <path-to-openai-math-checkout> [--commit SHA] [--date YYYY-MM-DD]

`report` prints new, removed and retitled result families, new history.md sections and
interest matches. It never writes. `snapshot` rewrites the baseline in
references/openai-math-watch.json and should only run after the report has been triaged
into references/openai-math-watch.md. Neither command fetches from the network, and a
keyword match is a routing hint, not evidence that a result is correct or relevant.
"""

from __future__ import annotations

import argparse
import html
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STATE = ROOT / "references" / "openai-math-watch.json"

FAMILY = re.compile(r"^\*\*(\d{3})\. (.+?)\*\*(.*)$", re.M)
TOTALS = re.compile(r"\*\*(\d+) manuscripts covering (\d+) result families\.\*\*")
HISTORY_SECTION = re.compile(r"^## (.+)$", re.M)
TAGS = re.compile(r"<[^>]+>")


def clean(text: str) -> str:
    return re.sub(r"\s+", " ", html.unescape(TAGS.sub("", text))).strip().rstrip(".")


def parse_contents(text: str) -> dict:
    families = {}
    for number, title, rest in FAMILY.findall(text):
        summary = clean(re.sub(r"\(\[Lean\]\([^)]*\)\)", "", rest))
        families[number] = {"title": clean(title), "lean": "(lean/docs/" in rest, "summary": summary}
    totals = TOTALS.search(text)
    return {
        "manuscripts": int(totals[1]) if totals else None,
        "families_total": int(totals[2]) if totals else None,
        "families": families,
    }


def parse_history(text: str) -> list[str]:
    return [section.strip() for section in HISTORY_SECTION.findall(text)]


def read_checkout(path: Path) -> dict:
    contents = path / "CONTENTS.md"
    if not contents.is_file():
        raise SystemExit(f"{contents} not found; pass the root of an openai/math checkout")
    parsed = parse_contents(contents.read_text(encoding="utf-8"))
    history = path / "history.md"
    parsed["history_sections"] = parse_history(history.read_text(encoding="utf-8")) if history.is_file() else []
    return parsed


def interest_matches(families: dict, interests: list[dict]) -> dict[str, list[str]]:
    matches: dict[str, list[str]] = {}
    for number, family in sorted(families.items()):
        haystack = f"{family['title']} {family.get('summary', '')}".lower()
        hits = [rule["id"] for rule in interests if any(word.lower() in haystack for word in rule["keywords"])]
        if hits:
            matches[number] = hits
    return matches


def diff(baseline: dict, current: dict) -> dict:
    old, new = baseline["families"], current["families"]
    return {
        "added": sorted(set(new) - set(old)),
        "removed": sorted(set(old) - set(new)),
        "retitled": sorted(n for n in set(old) & set(new) if old[n]["title"] != new[n]["title"]),
        "newly_formalized": sorted(n for n in set(old) & set(new) if new[n]["lean"] and not old[n]["lean"]),
        "new_history_sections": [s for s in current["history_sections"] if s not in baseline.get("history_sections", [])],
    }


def report(state: dict, current: dict) -> str:
    changes = diff(state["baseline"], current)
    families = current["families"]
    watched = {str(n) for n in state.get("watched_families", {})}
    matches = interest_matches(families, state["interests"])
    lines = [
        f"Baseline: {state['baseline']['commit']} ({state['baseline']['date']}), "
        f"{state['baseline']['manuscripts']} manuscripts / {state['baseline']['families_total']} families",
        f"Checkout: {current['manuscripts']} manuscripts / {current['families_total']} families",
        "",
        "New history.md sections: " + (", ".join(changes["new_history_sections"]) or "none"),
    ]
    for label, key in (("Added families", "added"), ("Removed families", "removed"), ("Retitled families", "retitled"),
                       ("Newly Lean-formalized", "newly_formalized")):
        lines.append(f"{label}: {len(changes[key])}")
        source = state["baseline"]["families"] if key == "removed" else families
        for number in changes[key]:
            flag = " [watched]" if number in watched else ""
            hint = f" interests={','.join(matches[number])}" if number in matches else ""
            lines.append(f"  {number}. {source[number]['title']}{flag}{hint}")
    touched = [n for n in watched if n in changes["retitled"] + changes["newly_formalized"] + changes["removed"]]
    lines += ["", "Watched families touched: " + (", ".join(sorted(touched)) or "none (content edits inside a family "
              "are not visible here; read history.md and the family's version notes)")]
    lines.append("Keyword matches are routing hints only; triage each one before recording it.")
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("command", choices=["report", "snapshot"])
    parser.add_argument("checkout", type=Path)
    parser.add_argument("--commit", help="openai/math commit the checkout is at (snapshot)")
    parser.add_argument("--date", help="commit date YYYY-MM-DD (snapshot)")
    args = parser.parse_args(argv)

    state = json.loads(STATE.read_text(encoding="utf-8"))
    current = read_checkout(args.checkout)
    if args.command == "report":
        print(report(state, current))
        return 0
    if not (args.commit and args.date):
        parser.error("snapshot requires --commit and --date")
    families = {n: {"title": f["title"], "lean": f["lean"]} for n, f in current["families"].items()}
    state["baseline"] = {"commit": args.commit, "date": args.date, **current, "families": families}
    STATE.write_text(json.dumps(state, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Baseline updated to {args.commit} ({len(current['families'])} families)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
