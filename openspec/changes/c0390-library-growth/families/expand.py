#!/usr/bin/env python3
# SPDX-License-Identifier: CC0-1.0
# Copyright (c) 2026 Fenolite contributors
"""Expand c0390 family tables into fenolite-library item folders.

    PY expand.py build TABLE.toml... --root LIBRARY     # PY: a Python where the pinned `fenolite` imports
    PY expand.py list TABLE.toml... --root LIBRARY

`build` creates, per table row, `footprints/cc0/<Namespace>/<name>/`: it runs Fenolite's c0260 package
generator on the row's family record, writes the generated pads, graphics and bodies as an explicit
`package.toml` (the record kind the library audit of the pinned core reads), the KiCad footprint the CI
`regenerate` job reproduces from it, Fenolite's STEP body, LICENSE, NOTICE, PROVENANCE.json (with the
family record and the generator stamp) and item.json.
The same tables give the same bytes: no clock, no randomness, sorted keys.
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import tomllib
from pathlib import Path

HERE = Path(__file__).resolve().parent
CHANGE = "c0390"
TABLES_PATH = "openspec/changes/c0390-library-growth/families"
SECTIONS = ("generate", "land", "symbol")
ARRAY_TABLES = ("side", "mechanical", "pin", "variant")
HEADER = ("schema", "id", "version", "summary", "category", "licence", "evidence", "sources")
KIND_FOLDER = {"footprint": "footprints", "symbol": "symbols"}
RECORD_FILE = {"footprint": "package.toml", "symbol": "pins.toml"}
SCHEMA = {"footprint": "fenolite.package.v0", "symbol": "fenolite.pins.v0"}
CC0_DIGEST = "0dd25be0803b1e2764b0323560013cdd5ad9ca92ba4780bd7db0cbe6ce821dd8"


def _scalar(value: object) -> str:
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, int):
        return str(value)
    if isinstance(value, str):
        return json.dumps(value, ensure_ascii=False)
    if isinstance(value, list):
        return "[" + ", ".join(_scalar(v) for v in value) + "]"
    if isinstance(value, dict):
        return "{ " + ", ".join(f"{_key(k)} = {_scalar(v)}" for k, v in value.items()) + " }"
    raise TypeError(f"unsupported TOML value {value!r} (floats are refused: write lengths as text)")


def _key(key: str) -> str:
    return key if re.fullmatch(r"[A-Za-z0-9_-]+", key) else json.dumps(key)


def toml_text(record: dict[str, object], comments: list[str]) -> str:
    lines = [f"# {c}" for c in comments]
    ordered = [k for k in HEADER if k in record] + [k for k in record if k not in HEADER]
    for key in ordered:
        value = record[key]
        if key in SECTIONS or (key in ARRAY_TABLES and isinstance(value, list)):
            continue
        lines.append(f"{_key(key)} = {_scalar(value)}")
    for key in ordered:
        value = record[key]
        if key in SECTIONS:
            assert isinstance(value, dict)
            plain = {k: v for k, v in value.items() if not (isinstance(v, list) and v and all(isinstance(x, dict) for x in v) and k in ("pins", "graphic"))}
            lines += ["", f"[{key}]"] + [f"{_key(k)} = {_scalar(v)}" for k, v in plain.items()]
            for sub, rows in value.items():
                if sub in plain:
                    continue
                for row in rows:
                    lines += ["", f"[[{key}.{sub}]]"] + [f"{_key(k)} = {_scalar(v)}" for k, v in row.items()]
        elif key in ARRAY_TABLES and isinstance(value, list):  # a header's ``pin`` is one table
            for row in value:
                lines += ["", f"[[{key}]]"] + [f"{_key(k)} = {_scalar(v)}" for k, v in row.items()]
    return "\n".join(lines) + "\n"


def canonical_json(data: object) -> str:
    return json.dumps(data, indent=2, sort_keys=True, ensure_ascii=False) + "\n"


def merge(base: dict[str, object], extra: dict[str, object]) -> dict[str, object]:
    out = dict(base)
    for key, value in extra.items():
        if isinstance(value, dict) and isinstance(out.get(key), dict):
            out[key] = merge(out[key], value)  # type: ignore[arg-type]
        else:
            out[key] = value
    return out


def rows_of(table_path: Path) -> list[dict[str, object]]:
    table = tomllib.loads(table_path.read_text(encoding="utf-8"))
    if table.get("schema") != "fenolite.c0390-family.v0":
        raise SystemExit(f"{table_path}: schema must be fenolite.c0390-family.v0")
    rows = []
    for row in table["row"]:
        record = merge(table.get("record", {}), row.get("record", {}))
        rows.append(
            {
                "kind": table["kind"],
                "namespace": row.get("namespace", table["namespace"]),
                "name": row["name"],
                "title": row["title"],
                "summary": row["summary"],
                "category": row.get("category", table["category"]),
                "version": row.get("version", table.get("version", "1.0.0")),
                "date": table["date"],
                "sources": row.get("sources", table.get("sources", [])),
                "used": row.get("used", table.get("used", "")),
                "tags": sorted(set(table.get("tags", [])) | set(row.get("tags", []))),
                "record": record,
                "table": f"{TABLES_PATH}/{table_path.name}",
                "comment": table.get("comment", ""),
            }
        )
    return rows


def item_folder(root: Path, row: dict[str, object]) -> Path:
    return root / KIND_FOLDER[row["kind"]] / "cc0" / str(row["namespace"]) / str(row["name"])


def write(rows: list[dict[str, object]], root: Path) -> None:
    sources = tomllib.loads((HERE / "sources.toml").read_text(encoding="utf-8"))
    cc0 = (HERE / "CC0-1.0.txt").read_bytes()
    seen: set[tuple[str, str]] = set()
    for row in rows:
        ident = f"{row['namespace']}:{row['name']}"
        if (row["kind"], ident) in seen:
            raise SystemExit(f"duplicate {row['kind']} {ident}")
        seen.add((row["kind"], ident))
        folder = item_folder(root, row)
        if folder.exists():
            shutil.rmtree(folder)
        folder.mkdir(parents=True)
        kind = str(row["kind"])
        record: dict[str, object] = {
            "schema": SCHEMA[kind],
            "id": ident,
            "version": row["version"],
            "summary": row["summary"],
            "category": row["category"],
            "licence": "CC0-1.0",
            "evidence": "INFERRED",
            "sources": row["sources"],
            **row["record"],  # type: ignore[dict-item]
        }
        cited = []
        for sid in row["sources"]:  # type: ignore[union-attr]
            src = sources[sid]
            cited.append(
                {
                    "date": src["date"],
                    "id": sid,
                    "revision": src["revision"],
                    "title": src["title"],
                    "url": src["url"],
                    "used": row["used"] or src["used"],
                }
            )
        comments = [
            "SPDX-License-Identifier: CC0-1.0",
            "Copyright (c) 2026 Fenolite contributors",
            f"Authored for fenolite-library (change {CHANGE}) from public package dimensions: "
            + ", ".join(f"{c['id']} {c['title']} ({c['revision']})" for c in cited)
            + ". Numbers only; no drawing, CAD file or 3D model copied.",
        ]
        row["comments"] = comments
        if kind == "symbol":
            (folder / RECORD_FILE[kind]).write_text(toml_text(record, comments), encoding="utf-8")
        (folder / "LICENSE").write_bytes(cc0)
        what = (
            "Fenolite's c0260 package generator from public package dimensions"
            if kind == "footprint"
            else "Fenolite's pin-table records from generic device-class conventions"
        )
        notice_line = (
            f"{row['date']}: original item authored for fenolite-library (change {CHANGE}) with {what}; "
            "no upstream design material."
        )
        (folder / "NOTICE").write_text(
            notice_line + "\n\nCopyright (c) 2026 Fenolite contributors. Dedicated under CC0-1.0.\n", encoding="utf-8"
        )
        provenance = {
            "authors": ["Fenolite contributors"],
            "copyright": ["Copyright (c) 2026 Fenolite contributors"],
            "datasheets": cited,
            "evidence": "INFERRED",
            "featured": None,
            "generation": {
                "change": CHANGE,
                "table": row["table"],
                "tool": "fenolite",
            },
            "id": ident,
            "kind": kind,
            "licence_text_sha256": CC0_DIGEST,
            "modification_notice": notice_line,
            "origin": "authored",
            "schema": "fenolite.provenance.v0",
            "sources": row["sources"],
            "spdx": "CC0-1.0",
            "trademarks": {"marks": [], "note": "", "restricted": False},
            "upstream": None,
            "version": row["version"],
        }
        (folder / "PROVENANCE.json").write_text(canonical_json(provenance), encoding="utf-8")
        meta = {"title": row["title"], "summary": row["summary"], "tags": row["tags"]}
        (folder / ".c0390-item.json").write_text(canonical_json(meta), encoding="utf-8")
    print(f"{len(rows)} item folders written")


FENOLITE_PIN = "e7673c811d5ca25d269c2d9c0f30e686f5148844"


def _terminals(data: dict[str, object]) -> dict[str, int]:
    """The explicit record's ``pins``: the terminal count the library check expects, counted as the core
    counts a family record (an exposed pad or a numbered tab is one more terminal; a header has rows x
    columns)."""
    family = data.get("family")
    if family == "nolead" and isinstance(data.get("ep"), dict):
        return {"pins": int(data["pins"]) + 1}  # type: ignore[call-overload]
    if family == "header":
        return {"pins": int(data["rows"]) * int(data["columns"])}  # type: ignore[call-overload]
    return {}


def _footprint_record(row: dict[str, object], folder: Path) -> tuple[str, dict[str, object]]:
    """Run the c0260 generator on the row's family record and return the explicit record text the
    library's record parser reads, with the facts of the generation for PROVENANCE.json."""
    from fenolite.catalog import records  # type: ignore[import-not-found]
    from fenolite.catalog.footprints import generate as run_generator  # type: ignore[import-not-found]
    from fenolite.catalog.footprints import read_package  # type: ignore[import-not-found]

    ident = f"{row['namespace']}:{row['name']}"
    family_record: dict[str, object] = {
        "schema": "fenolite.package.v0",
        "id": ident,
        "summary": row["summary"],
        "evidence": "INFERRED",
        "sources": row["sources"],
        **row["record"],  # type: ignore[dict-item]
    }
    family_text = toml_text(family_record, [])
    package = read_package(family_text, file=f"{row['name']}.family.toml")
    generated = run_generator(package, library=str(row["namespace"]))
    errors = [i for i in generated.issues if i.severity == "error"]
    if errors or generated.footprint is None:
        raise ValueError("; ".join(f"{i.code}: {i.message}" for i in generated.issues) or "no footprint")
    fp = generated.footprint
    header = records.parse_header(
        {
            "schema": "fenolite.package.v0",
            "id": ident,
            "version": row["version"],
            "summary": row["summary"],
            "category": row["category"],
            "licence": "CC0-1.0",
            "evidence": "INFERRED",
            "sources": row["sources"],
        },
        "package",
        file="package.toml",
    )
    data = family_record
    dims: dict[str, tuple[int, ...]] = {}
    raw = records.parse_record(  # reuse the record reader's own bounds for the stored dimensions
        toml_text(
            {
                "schema": "fenolite.package.v0",
                "id": ident,
                "version": row["version"],
                "summary": row["summary"],
                "licence": "CC0-1.0",
                "evidence": "INFERRED",
                "sources": row["sources"],
                "generator": "explicit",
                "kind": fp.kind,
                **{k: v for k, v in data.items() if k in ("pins", "pitch")},
                **_terminals(data),
                **{
                    k: {
                        n: (f"{b['min']}..{b['max']}" if isinstance(b, dict) else b)
                        for n, b in v.items()
                        if isinstance(b, dict) or not b.endswith((" max", " min"))
                    }
                    for k, v in data.items()
                    if k in ("body", "span", "lead") and isinstance(v, dict)
                },
            },
            [],
        ),
        file="dimensions.toml",
    )
    dims = dict(raw.dimensions)
    pads = tuple(
        records.PadEntry(
            number=p.number,
            shape=p.shape,
            size=p.size,
            at=p.position,
            kind=p.kind,
            rotation=p.rotation,
            drill=p.drill,
            layers=p.layers,
            corner_ratio=p.corner_ratio,
            mask_margin=p.mask_margin,
        )
        for p in fp.pads
    )
    graphics = tuple(
        records.GraphicEntry(
            kind=g.kind, layer=g.layer, points=g.points, width=g.width, filled=g.filled, key=f"{g.layer}:{i}"
        )
        for i, g in enumerate(fp.graphics)
    )
    bodies = tuple(
        records.BodyEntry(
            kind=b.kind,
            height=b.height,
            standoff=b.standoff,
            outline=b.outline,
            layer=b.layer,
            model=b.model,
            name=b.name,
            z_min=b.z_min,
            z_max=b.z_max,
            projection_unknown=b.projection_unknown,
        )
        for b in fp.bodies
    )
    record = records.PackageRecord(
        header=header,
        generator="explicit",
        kind=fp.kind,
        flags=fp.flags,
        dimensions=dims,
        pads=pads,
        graphics=graphics,
        family=str(data["family"]),
        bodies=bodies,
    )
    stamp = fp.description.rsplit(". ", 1)[-1] if ". " in fp.description else fp.description
    text = records.record_text(record)
    comments = row["comments"]  # type: ignore[assignment]
    text = "".join(f"# {c}\n" for c in comments) + text  # type: ignore[union-attr]
    facts = {
        "change": CHANGE,
        "fenolite": FENOLITE_PIN,
        "table": row["table"],
        "tool": "fenolite",
        "generator": stamp,
        "family_record": json.loads(json.dumps(family_record)),
        "findings": sorted({f"{i.severity} {i.code}" for i in generated.issues}),
        "explicit_record": "the generator's pads, graphics and bodies written as a generator='explicit' record "
        "(the record kind the library audit reads); outputs regenerate from package.toml",
    }
    return text, facts


def build(rows: list[dict[str, object]], root: Path) -> None:
    from fenolite.backends import step as step_mod  # type: ignore[import-not-found]
    from fenolite.backends.kicad.mod import prepare_authored_definition, write_footprint  # type: ignore[import-not-found]
    from fenolite.backends.kicad.sym import write_symbol_library  # type: ignore[import-not-found]
    from fenolite.catalog import records  # type: ignore[import-not-found]

    write(rows, root)
    failures = []
    built = 0
    for row in rows:
        folder = item_folder(root, row)
        kind = str(row["kind"])
        meta_path = folder / ".c0390-item.json"
        meta = json.loads(meta_path.read_text(encoding="utf-8"))
        meta_path.unlink()
        if kind == "symbol":
            try:
                text = (folder / "pins.toml").read_text(encoding="utf-8")
                parsed = records.parse_record(text, file="pins.toml")
                sym = write_symbol_library((records.symbol_def(parsed),), target=9)
            except Exception as exc:  # noqa: BLE001 - reported per item, the batch stops
                failures.append((str(folder.relative_to(root)), f"{type(exc).__name__}: {exc}"))
                shutil.rmtree(folder)
                continue
            (folder / "generated").mkdir()
            (folder / "generated" / "pins.kicad_sym").write_text(sym, encoding="utf-8")
            files = ["generated/pins.kicad_sym", "pins.toml"]
            provenance = json.loads((folder / "PROVENANCE.json").read_text(encoding="utf-8"))
            provenance["generation"] = {
                "change": CHANGE,
                "fenolite": FENOLITE_PIN,
                "table": row["table"],
                "tool": "fenolite",
                "explicit_record": "explicit pin placements and graphics; generated/pins.kicad_sym regenerates from pins.toml",
            }
            (folder / "PROVENANCE.json").write_text(canonical_json(provenance), encoding="utf-8")
            namespace, name = str(row["namespace"]), str(row["name"])
        else:
            try:
                text, facts = _footprint_record(row, folder)
                parsed = records.parse_record(text, file="package.toml")
                definition = records.footprint_def(parsed)
                mod = write_footprint(prepare_authored_definition(definition), target=9)
            except Exception as exc:  # noqa: BLE001 - reported per item, the batch stops
                failures.append((str(folder.relative_to(root)), f"{type(exc).__name__}: {exc}"))
                shutil.rmtree(folder)
                continue
            (folder / "package.toml").write_text(text, encoding="utf-8")
            name = str(row["name"])
            namespace = str(row["namespace"])
            files = ["package.toml", f"generated/{namespace}.pretty/{name}.kicad_mod"]
            (folder / files[1]).parent.mkdir(parents=True)
            (folder / files[1]).write_text(mod, encoding="utf-8")
            if definition.bodies:
                step = f"generated/{namespace}.3dshapes/{name}.step"
                (folder / step).parent.mkdir(parents=True)
                (folder / step).write_bytes(step_mod.write_bodies(name, definition.bodies))
                files.append(step)
            provenance = json.loads((folder / "PROVENANCE.json").read_text(encoding="utf-8"))
            provenance["generation"] = facts
            (folder / "PROVENANCE.json").write_text(canonical_json(provenance), encoding="utf-8")
        item = {
            "depends": [],
            "executes": False,
            "files": sorted(files),
            "id": f"{namespace}:{name}",
            "kind": kind,
            "schema": "fenolite.library-item.v0",
            "spdx": "CC0-1.0",
            "summary": meta["summary"],
            "tags": meta["tags"],
            "title": meta["title"],
            "version": row["version"],
        }
        (folder / "item.json").write_text(canonical_json(item), encoding="utf-8")
        built += 1
    for folder, message in failures:
        print("FAILED", folder, message[:800])
    print(f"{built} built, {len(failures)} failed")
    if failures:
        raise SystemExit(5)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("action", choices=("build", "list"))
    parser.add_argument("tables", nargs="+", type=Path)
    parser.add_argument("--root", type=Path, required=True)
    args = parser.parse_args()
    rows = [row for table in args.tables for row in rows_of(table)]
    root = args.root.resolve()
    if args.action == "build":
        build(rows, root)
    else:
        for row in rows:
            print(item_folder(root, row).relative_to(root).as_posix())


if __name__ == "__main__":
    main()
