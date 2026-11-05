#!/usr/bin/env python3
# SPDX-License-Identifier: CC0-1.0
# Copyright (c) 2026 Fenolite contributors
"""Prove c0390 items with the pinned Fenolite, in one process (change c0390, design section 4).

    PY prove.py ITEM_FOLDER... --root LIBRARY --sheets DIR --report FILE

Per item: `library check` (read back, rules, no error finding), `library audit --item` (licence, provenance,
sources, notice), the CI `regenerate` comparison (explicit record -> KiCad bytes) plus the STEP body, and the
review sheets `library check --sheets` renders (each must be a non-empty HTML file holding an SVG drawing).
"""

from __future__ import annotations

import argparse
import contextlib
import hashlib
import io
import json
import os
import sys
import tomllib
from pathlib import Path


def cli(argv: list[str]) -> tuple[int, dict[str, object]]:
    from fenolite.cli.main import main  # type: ignore[import-not-found]

    out, err = io.StringIO(), io.StringIO()
    with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
        code = main([*argv, "--json"])
    text = out.getvalue().strip() or err.getvalue().strip()
    try:
        return code, json.loads(text.splitlines()[-1] if text and not text.startswith("{") else text or "{}")
    except json.JSONDecodeError:
        return code, {"raw": text[:400]}


def regenerate(folder: Path) -> list[str]:
    from fenolite.backends import step as step_mod  # type: ignore[import-not-found]
    from fenolite.backends.kicad.mod import prepare_authored_definition, write_footprint  # type: ignore[import-not-found]
    from fenolite.backends.kicad.sym import write_symbol_library  # type: ignore[import-not-found]
    from fenolite.catalog import records  # type: ignore[import-not-found]

    problems = []
    for record in sorted(folder.glob("*.toml")):
        data = tomllib.loads(record.read_text(encoding="utf-8"))
        parsed = records.parse_record(record.read_text(encoding="utf-8"), file=str(record))
        if data["schema"] == "fenolite.package.v0":
            definition = records.footprint_def(parsed)
            namespace, name = parsed.header.id.split(":", 1)
            outputs = {
                folder / "generated" / f"{namespace}.pretty" / f"{name}.kicad_mod": write_footprint(
                    prepare_authored_definition(definition), target=9
                ).encode()
            }
            if definition.bodies:
                outputs[folder / "generated" / f"{namespace}.3dshapes" / f"{name}.step"] = step_mod.write_bodies(
                    name, definition.bodies
                )
        else:
            outputs = {
                folder / "generated" / f"{record.stem}.kicad_sym": write_symbol_library(
                    (records.symbol_def(parsed),), target=9
                ).encode()
            }
        for path, data_bytes in outputs.items():
            if not path.is_file() or hashlib.sha256(path.read_bytes()).digest() != hashlib.sha256(data_bytes).digest():
                problems.append(f"{path}: missing or differs from regeneration")
    return problems


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("items", nargs="+", type=Path)
    parser.add_argument("--root", type=Path, required=True)
    parser.add_argument("--sheets", type=Path, required=True)
    parser.add_argument("--report", type=Path, required=True)
    args = parser.parse_args()
    root = args.root.resolve()
    sheets = args.sheets.resolve()
    os.chdir(root)
    rows = []
    failed = 0
    for item in args.items:
        rel = item.resolve().relative_to(root).as_posix()
        row: dict[str, object] = {"item": rel}
        code, reply = cli(["library", "check", rel, "--sheets", str(sheets)])
        issues = reply.get("issues", []) if isinstance(reply, dict) else []
        row["check"] = {"exit": code, "issues": [f"{i['severity']} {i['code']}" for i in issues]}  # type: ignore[index,union-attr]
        rendered = []
        for entry in reply.get("result", {}).get("items", []):  # type: ignore[union-attr]
            sheet = sheets / entry["sheet"]["path"]
            text = sheet.read_text(encoding="utf-8") if sheet.is_file() else ""
            rendered.append(bool(text) and "<svg" in text)
        row["sheets"] = {"count": len(rendered), "rendered": sum(rendered)}
        code_a, reply_a = cli(["library", "audit", ".", "--item", rel])
        row["audit"] = {
            "exit": code_a,
            "issues": [f"{i['severity']} {i['code']}: {i['message'][:200]}" for i in reply_a.get("issues", [])],  # type: ignore[union-attr]
        }
        row["regenerate"] = regenerate(root / rel)
        ok = code == 0 and code_a == 0 and not row["regenerate"] and rendered and all(rendered)
        row["ok"] = bool(ok)
        failed += 0 if ok else 1
        rows.append(row)
    report = {"items": len(rows), "failed": failed, "rows": rows}
    args.report.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    for row in rows:
        if not row["ok"]:
            print("FAIL", json.dumps(row)[:900])
    print(f"{len(rows) - failed}/{len(rows)} items proved")
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
