# REF-02 연구 인덱스

- identity: `sealed`
- source: `SRC-COL2-027`
- boundary: `1~284화 / exact`
- canonical_completed_precision_scope: `1~20화`
- prepared_hold_scope: `21~30화`
- latest_batch: `BATCH-REF02-0003`
- latest_receipt: `RCPT-20260806-1854-REF02`
- latest_status: `HOLD_STANDARD_RESTORE`

## 정본 결함

`REPOSITORY_MANIFEST.yaml`이 지정한 다음 필수 문서가 정본 루트에 없다.

- `REFERENCE_RESEARCH_ANALYSIS_SOP_v6.md`
- `REFERENCE_RESEARCH_REPOSITORY_CONTRACT_v1.md`
- `REFERENCE_WORK_MODEL_SCHEMA_v1.md`

21~30화 연구는 검증된 로컬 승인본을 직접 읽고 별도 브랜치에 준비했으나, 위 문서 복구와 재검증 전에는 `canonical_completed_precision_scope`를 30화로 올리지 않는다.

## 배치

- `BATCH-REF02-0001` — 1~10화 / complete
- `BATCH-REF02-0002` — 11~20화 / complete
- `BATCH-REF02-0003` — 21~30화 / HOLD_STANDARD_RESTORE

## 원천 장면

- `SC-REF02-0001~0004` — 1~10화
- `SC-REF02-0005~0012` — 11~20화
- `SC-REF02-0013~0022` — 21~30화 / hold branch

## 작품 모델

- `CHR-REF02-0001` — 주인공 A 판단 모델, 1~30화 준비
- `REL-REF02-0001` — 제한된 권리 계약과 상호 교환, 1~30화 신규
- `EVT-REF02-0001` — 사건 결과의 성장 인프라·새 위험 전환, 1~30화 신규
- `STY-REF02-0001` — 보상 정산·생활 관계·다음 위험 배열, 1~30화 신규
- `PRO-REF02-0001` — 설명·시점·재분류 운용, 1~30화 준비

## 활성 TH

- `TH-REF02-CHR-02` — `VERIFIED_THREAD` 보강
- `TH-REF02-REL-04` — `VERIFIED_THREAD` 보강
- `TH-REF02-TEC-02` — `VERIFIED_THREAD` 승격 준비
- `TH-REF02-EVT-03` — `VERIFIED_THREAD` 신규

## 감사

- `AUDIT-REF02-0001` — 필수 정본 문서 누락 및 21~30화 HOLD 감사

## 다음 절차

1. 필수 정본 문서 3종을 매니페스트 경로에 복구한다.
2. 복구 커밋 SHA와 문서 체크섬을 검증한다.
3. 21~30화 브랜치를 최신 `main`에 재기반화하고 ID·링크·익명성·연구 판정을 다시 감사한다.
4. 통과하면 병합하고 영수증에 연구 내용 SHA와 FINAL SHA를 기록한다.
5. 다음 구간은 `31~40화`다.
