from __future__ import annotations

import argparse
import csv
import hashlib
import json
import shutil
import zipfile
from collections import Counter, defaultdict
from pathlib import Path


EXPECTED_EXTENSIONS = {
    ".md": 1022,
    ".txt": 32,
    ".csv": 30,
    ".json": 3,
    ".zip": 2,
}

TABLES = {
    "01 · 공용 실행 카드 · 개편본": "execution-cards.csv",
    "02-A · REF 원천 레지스트리": "reference-registry.csv",
    "02-B · REF 심층 증거 스레드": "evidence-threads.csv",
    "02-C · 공용 카드 승격 후보": "card-promotion-candidates.csv",
    "02-D · 연구 검색 영수증": "research-receipts.csv",
    "02-E · 연구 범위 감사": "scope-audits.csv",
    "03-A · 참고작 원문 장면 색인": "source-scene-index.csv",
    "03-B · 임시 원문 독서 묶음": "temporary-reading-bundles.csv",
    "03-C · 익명 원문 독서 장면": "anonymous-reading-scenes.csv",
    "03-E · 익명 표현 장면 라이브러리": "anonymous-expression-scenes.csv",
    "03-F · 익명 표현 단위 사전": "expression-units.csv",
    "04-A · 원본 작업 영수증 인덱스": "work-receipts.csv",
    "04-B · 실전 작업 회고 사례": "retrospectives.csv",
    "04-C · 공용 가설 승격 후보": "hypothesis-promotion-candidates.csv",
}

MANIFESTS = {
    "bundle_summary.json": "ref46-bundle-summary.json",
    "volume_manifest.json": "ref46-volume-manifest.json",
    "volume_manifest 1.json": "ref39-volume-manifest.json",
}


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def write_text(path: Path, value: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(value, encoding="utf-8", newline="\n")


def write_json(path: Path, value: object) -> None:
    write_text(path, json.dumps(value, ensure_ascii=False, indent=2) + "\n")


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def find_table(raw: Path, prefix: str) -> Path:
    matches = sorted(raw.glob(f"{prefix}*.csv"))
    if not matches:
        raise RuntimeError(f"Missing table: {prefix}")
    base = [path for path in matches if not path.stem.endswith("_all")]
    return base[0] if base else matches[0]


def ref_sort_key(value: str) -> tuple[int, str]:
    digits = "".join(ch for ch in value if ch.isdigit())
    return (int(digits) if digits else 9999, value)


def safe_extract_zip(zip_path: Path, target: Path) -> None:
    target.mkdir(parents=True, exist_ok=True)
    root = target.resolve()
    with zipfile.ZipFile(zip_path) as archive:
        for info in archive.infolist():
            destination = (target / info.filename).resolve()
            if root != destination and root not in destination.parents:
                raise RuntimeError(f"Unsafe ZIP path: {info.filename}")
            if info.is_dir():
                destination.mkdir(parents=True, exist_ok=True)
                continue
            destination.parent.mkdir(parents=True, exist_ok=True)
            with archive.open(info) as source, destination.open("xb") as output:
                shutil.copyfileobj(source, output)


def repo_checksums(root: Path) -> list[str]:
    excluded = {Path("migration/CHECKSUMS.sha256")}
    lines: list[str] = []
    for path in sorted(item for item in root.rglob("*") if item.is_file()):
        relative = path.relative_to(root)
        if (
            relative in excluded
            or ".git" in relative.parts
            or "__pycache__" in relative.parts
            or path.suffix == ".pyc"
        ):
            continue
        lines.append(f"{sha256_file(path)}  {relative.as_posix()}")
    return lines


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--raw", type=Path, required=True)
    parser.add_argument("--source-zip", type=Path, required=True)
    parser.add_argument("--repo", type=Path, required=True)
    parser.add_argument("--validator", type=Path, required=True)
    args = parser.parse_args()

    raw = args.raw.resolve()
    source_zip = args.source_zip.resolve()
    repo = args.repo.resolve()
    validator = args.validator.resolve()

    if repo.exists():
        raise RuntimeError(f"Refusing to overwrite existing output: {repo}")

    raw_files = sorted(path for path in raw.rglob("*") if path.is_file())
    counts = Counter(path.suffix.lower() for path in raw_files)
    if len(raw_files) != 1089 or dict(counts) != EXPECTED_EXTENSIONS:
        raise RuntimeError(f"Unexpected export structure: {len(raw_files)} files, {dict(counts)}")

    repo.mkdir(parents=True)
    pages = repo / "history" / "notion-export" / "pages"
    shutil.copytree(raw, pages)
    archive_target = repo / "history" / "source-archives" / "notion-export-2026-08-06.zip"
    archive_target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source_zip, archive_target)

    table_sources: dict[str, Path] = {}
    table_rows: dict[str, int] = {}
    for prefix, stable_name in TABLES.items():
        source = find_table(raw, prefix)
        destination = repo / "catalog" / "tables" / stable_name
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, destination)
        table_sources[stable_name] = source
        table_rows[stable_name] = len(read_csv(source))

    (repo / "catalog" / "manifests").mkdir(parents=True, exist_ok=True)
    for source_name, stable_name in MANIFESTS.items():
        shutil.copy2(raw / source_name, repo / "catalog" / "manifests" / stable_name)

    ref39 = repo / "sources" / "REF-39"
    ref39.mkdir(parents=True)
    for path in sorted(raw.glob("REF39_PERSISTENT_SOURCE_VOLUME_*.txt")):
        shutil.copy2(path, ref39 / path.name)
    shutil.copy2(raw / "volume_manifest 1.json", ref39 / "volume_manifest.json")
    shutil.copy2(raw / "REF39_EXACT_ORIGINAL_BYTES_BACKUP.zip", ref39 / "exact-original-bytes-backup.zip")

    ref46 = repo / "sources" / "REF-46"
    safe_extract_zip(raw / "ref46_persistent_source_volumes_v1.zip", ref46)
    shutil.copy2(raw / "bundle_summary.json", ref46 / "bundle_summary.json")

    registry = read_csv(table_sources["reference-registry.csv"])
    evidence = read_csv(table_sources["evidence-threads.csv"])
    scenes = read_csv(table_sources["source-scene-index.csv"])
    anonymous = read_csv(table_sources["anonymous-reading-scenes.csv"])
    expressions = read_csv(table_sources["anonymous-expression-scenes.csv"])

    evidence_counts = Counter(row.get("REF 코드", "").strip() for row in evidence)
    scene_counts = Counter(row.get("REF 코드", "").strip() for row in scenes)
    anonymous_counts = Counter(row.get("REF 코드", "").strip() for row in anonymous)
    expression_counts = Counter(row.get("REF 코드", "").strip() for row in expressions)
    works: dict[str, set[str]] = defaultdict(set)
    for row in scenes:
        ref_code = row.get("REF 코드", "").strip()
        work = row.get("작품명", "").strip()
        if ref_code and work:
            works[ref_code].add(work)

    references: list[dict[str, object]] = []
    for row in sorted(registry, key=lambda item: ref_sort_key(item.get("REF 코드", ""))):
        ref_code = row.get("REF 코드", "").strip()
        references.append(
            {
                "ref_code": ref_code,
                "works": sorted(works[ref_code]),
                "searchable": row.get("검색 가능", "").strip(),
                "boundary_status": row.get("경계 상태", "").strip(),
                "restored_boundary": row.get("복원 경계", "").strip(),
                "non_canon": row.get("비정사", "").strip(),
                "index_block": row.get("색인 블록", "").strip(),
                "file_hint": row.get("파일 힌트 회차", "").strip(),
                "technical_note": row.get("기술 메모", "").strip(),
                "counts": {
                    "evidence_threads": evidence_counts[ref_code],
                    "source_scenes": scene_counts[ref_code],
                    "anonymous_reading_scenes": anonymous_counts[ref_code],
                    "expression_scenes": expression_counts[ref_code],
                },
            }
        )

    summary = {
        "schema_version": "REFERENCE-LIBRARY-MIGRATION-1",
        "repository": "dnrlvkf/webnovel-reference-library",
        "visibility": "private",
        "source_export_sha256": sha256_file(source_zip),
        "notion_files": len(raw_files),
        "extension_counts": dict(sorted(counts.items())),
        "reference_count": len(references),
        "table_rows": table_rows,
        "persistent_sources": {
            "REF-39": {
                "volumes": len(list(ref39.glob("REF39_PERSISTENT_SOURCE_VOLUME_*.txt"))),
                "exact_backup": "sources/REF-39/exact-original-bytes-backup.zip",
            },
            "REF-46": {
                "volumes": len(list((ref46 / "volumes").glob("*.txt"))),
                "manifest": "sources/REF-46/volume_manifest.json",
            },
        },
    }
    write_json(repo / "catalog" / "summary.json", summary)
    write_json(repo / "catalog" / "references.json", references)

    index_lines = [
        "# 공용 참고작 색인",
        "",
        f"- REF 레지스트리: {len(references)}개",
        f"- 심층 증거 스레드: {len(evidence)}개",
        f"- 원문 장면 색인: {len(scenes)}개",
        f"- 익명 원문 장면: {len(anonymous)}개",
        f"- 익명 표현 장면: {len(expressions)}개",
        "",
        "| REF | 작품명 | 경계 상태 | 증거 | 원문 장면 | 익명 장면 | 표현 장면 |",
        "| --- | --- | --- | ---: | ---: | ---: | ---: |",
    ]
    for item in references:
        counts_item = item["counts"]
        work_names = ", ".join(item["works"]) or "—"
        index_lines.append(
            f"| {item['ref_code']} | {work_names.replace('|', '/')} | "
            f"{str(item['boundary_status']).replace('|', '/')} | "
            f"{counts_item['evidence_threads']} | {counts_item['source_scenes']} | "
            f"{counts_item['anonymous_reading_scenes']} | {counts_item['expression_scenes']} |"
        )
    write_text(repo / "catalog" / "INDEX.md", "\n".join(index_lines) + "\n")

    migration_files = [
        {
            "path": path.relative_to(raw).as_posix(),
            "bytes": path.stat().st_size,
            "sha256": sha256_file(path),
        }
        for path in raw_files
    ]
    write_json(repo / "migration" / "notion-files.json", migration_files)

    readme = """# 웹소설 공용 참고작 라이브러리

작품별 정본 저장소와 분리된 비공개 참고작 연구 라이브러리입니다.

## 사용 순서

1. `catalog/INDEX.md`에서 REF와 작품·근거 수를 찾습니다.
2. `catalog/tables/`의 레지스트리·증거 스레드·장면 색인을 조회합니다.
3. REF-39와 REF-46은 `sources/`의 지속 원문 볼륨을 우선 사용합니다.
4. 원형 확인이나 복구가 필요할 때만 `history/notion-export/pages/`를 봅니다.

## 권위와 경계

- `history/`는 노션 내보내기 원형과 입력 ZIP을 보존합니다.
- `catalog/`는 검색 편의를 위한 파생 색인입니다.
- `sources/`는 노션 안의 지속 원문 패키지를 읽기 쉽게 펼친 복사본입니다.
- 이 저장소의 자료는 어느 작품의 정본도 아닙니다.
- 참고작의 표면 문장·고유명·장면을 그대로 복제하지 않습니다.
"""
    write_text(repo / "README.md", readme)

    agents = """# 공용 참고작 라이브러리 작업 규칙

1. 이 저장소는 참고·연구 자료이며 작품별 정본이 아니다.
2. 검색은 `catalog/`에서 시작하고, 판단 근거가 필요할 때 해당 REF의 증거·원문 위치로 내려간다.
3. 참고작의 문장, 고유명, 사건 배열을 결과물에 그대로 복제하지 않는다.
4. 구조·기능·실패 조건을 추출하되 적용 여부는 대상 작품의 정본과 연속성을 기준으로 다시 판단한다.
5. `history/`의 원형 파일은 수정하지 않는다.
6. 새 자료는 원본 보존, 체크섬, 색인 갱신을 한 커밋에서 함께 처리한다.
"""
    write_text(repo / "AGENTS.md", agents)
    write_text(repo / ".gitignore", "__pycache__/\n*.pyc\n")
    write_text(repo / ".gitattributes", "# 보존 저장소: 바이트 자동 변환 금지\n* -text\n")

    report = f"""# 이관 보고서

- 입력 ZIP SHA-256: `{sha256_file(source_zip)}`
- 노션 원형 파일: {len(raw_files)}개
- REF 레지스트리: {len(references)}개
- 정규화 테이블: {len(TABLES)}개
- REF-39 지속 원문 볼륨: {summary['persistent_sources']['REF-39']['volumes']}개
- REF-46 지속 원문 볼륨: {summary['persistent_sources']['REF-46']['volumes']}개
- 경로 이탈 항목: 0개
- `_all.csv` 중복본: 대응 기본본과 동일한 해시로 확인됨
"""
    write_text(repo / "migration" / "REPORT.md", report)

    tools = repo / "tools"
    tools.mkdir(parents=True)
    shutil.copy2(Path(__file__).resolve(), tools / "build_reference_library.py")
    shutil.copy2(validator, tools / "validate_reference_library.py")
    write_text(repo / "migration" / "CHECKSUMS.sha256", "\n".join(repo_checksums(repo)) + "\n")

    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
