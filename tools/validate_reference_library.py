from __future__ import annotations

import csv
import hashlib
import json
from pathlib import Path


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def csv_rows(path: Path) -> int:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return sum(1 for _ in csv.DictReader(handle))


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    errors: list[str] = []

    summary = json.loads((root / "catalog" / "summary.json").read_text(encoding="utf-8"))
    references = json.loads((root / "catalog" / "references.json").read_text(encoding="utf-8"))
    notion_files = json.loads((root / "migration" / "notion-files.json").read_text(encoding="utf-8"))

    pages = [path for path in (root / "history" / "notion-export" / "pages").rglob("*") if path.is_file()]
    if len(pages) != 1089 or summary["notion_files"] != 1089 or len(notion_files) != 1089:
        errors.append("Notion file count must remain 1089")
    if len(references) != 46 or summary["reference_count"] != 46:
        errors.append("Reference registry count must remain 46")

    expected_rows = {
        "reference-registry.csv": 46,
        "evidence-threads.csv": 151,
        "card-promotion-candidates.csv": 16,
        "research-receipts.csv": 32,
        "scope-audits.csv": 27,
        "source-scene-index.csv": 248,
        "temporary-reading-bundles.csv": 5,
        "anonymous-reading-scenes.csv": 261,
        "anonymous-expression-scenes.csv": 139,
        "expression-units.csv": 25,
        "work-receipts.csv": 3,
        "retrospectives.csv": 1,
        "hypothesis-promotion-candidates.csv": 1,
    }
    for name, expected in expected_rows.items():
        actual = csv_rows(root / "catalog" / "tables" / name)
        if actual != expected:
            errors.append(f"Row count mismatch for {name}: {actual} != {expected}")

    if len(list((root / "sources" / "REF-39").glob("REF39_PERSISTENT_SOURCE_VOLUME_*.txt"))) != 12:
        errors.append("REF-39 must have 12 persistent source volumes")
    if len(list((root / "sources" / "REF-46" / "volumes").glob("*.txt"))) != 12:
        errors.append("REF-46 must have 12 persistent source volumes")

    for row in notion_files:
        path = root / "history" / "notion-export" / "pages" / row["path"]
        if not path.is_file() or path.stat().st_size != row["bytes"] or sha256_file(path) != row["sha256"]:
            errors.append(f"Raw file mismatch: {row['path']}")
            if len(errors) >= 20:
                break

    checksum_path = root / "migration" / "CHECKSUMS.sha256"
    for line in checksum_path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        expected, relative = line.split("  ", 1)
        path = root / relative
        if not path.is_file() or sha256_file(path) != expected:
            errors.append(f"Checksum mismatch: {relative}")
            if len(errors) >= 20:
                break

    text_extensions = {".md", ".txt", ".json", ".csv", ".sha256", ".py"}
    for path in root.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in text_extensions:
            continue
        try:
            path.read_text(encoding="utf-8-sig")
        except UnicodeDecodeError as exc:
            errors.append(f"UTF-8 decode failure: {path.relative_to(root)}: {exc}")

    result = {
        "status": "FAIL" if errors else "PASS",
        "errors": errors,
        "notion_files": len(pages),
        "references": len(references),
        "ref39_volumes": len(list((root / "sources" / "REF-39").glob("REF39_PERSISTENT_SOURCE_VOLUME_*.txt"))),
        "ref46_volumes": len(list((root / "sources" / "REF-46" / "volumes").glob("*.txt"))),
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    raise SystemExit(1 if errors else 0)


if __name__ == "__main__":
    main()
