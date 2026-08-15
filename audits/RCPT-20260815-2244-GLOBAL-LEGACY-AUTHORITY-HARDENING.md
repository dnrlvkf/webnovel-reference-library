# GLOBAL 연구 영수증

- receipt_id: `RCPT-20260815-2244-GLOBAL-LEGACY-AUTHORITY-HARDENING`
- date_time: `2026-08-15T22:44:00+09:00`
- work_id: `GLOBAL`
- mode: `repository maintenance / legacy authority hardening audit`
- question: `현행 참고작 연구 구조를 유지하면서도 과거 부속서와 catalog 실행 카드가 새 채팅·검색 도구에 의해 다시 실행 권위로 오인되는 경로를 어떻게 구조적으로 차단할 것인가`
- source_scope: `no new source-text research claim; current manifest, legacy addenda v1.1-v1.3, catalog legacy boundary, current README/AGENTS routing only`
- base_sha: `6ffc8f1e0e1576a3c9d2f5639d687de05fd36b3a`
- research_content_sha: `c48d13a8ce87d61c25a9f5f27d06c085d47b3f48`
- final_sha: `PENDING_INDEX_SEAL`
- remote_status: `pending_index_seal`
- status: `content_complete_pending_index_seal`

## 조회한 기록

- `REPOSITORY_MANIFEST.yaml`
- `README.md`
- `AGENTS.md`
- `catalog/INDEX.md`
- `catalog/tables/execution-cards.csv`
- `REFERENCE_RESEARCH_REPOSITORY_CONTRACT_v1.1_PROJECT_SOURCE_ADDENDUM.md`
- `REFERENCE_RESEARCH_REPOSITORY_CONTRACT_v1.2_PROJECT_SOURCE_ADDENDUM.md`
- `REFERENCE_RESEARCH_REPOSITORY_CONTRACT_v1.3_PROJECT_SOURCE_ADDENDUM.md`
- 현행 `REFERENCE_RESEARCH_REPOSITORY_CONTRACT_v1.4_PROJECT_SOURCE_ADDENDUM.md`
- 최근 `RCPT-20260815-2239-GLOBAL-ONBOARDING-ROUTING`

## 문제 확인

- `catalog/tables/execution-cards.csv`에는 과거 `실행 완료 조건`, `권장 조합`, `전개 구조`, `조건부 생성 후보`, `0~3개만 검토`, `주원리 최대 1개` 같은 실행 카드형 필드와 값이 역사 데이터로 남아 있다.
- `catalog/INDEX.md`, README, AGENTS는 이미 `catalog/`를 LEGACY / NON-AUTHORITATIVE로 규정하고 있어 현행 논리 권위는 제거되어 있었다.
- 그러나 `REFERENCE_RESEARCH_REPOSITORY_CONTRACT_v1.1`과 `v1.2`의 머리말에는 현재 매니페스트가 v1.3을 가리킨다는 낡은 문장이 남아 있었다.
- `REFERENCE_RESEARCH_REPOSITORY_CONTRACT_v1.3`은 별도 SUPERSEDED 배너 없이 자기 자신을 현행 적용 부속서처럼 설명하는 문장이 남아 있었다.
- 현행 매니페스트에는 활성 경로는 있었지만 legacy/non-authoritative 경계와 historical contract 제외 정책을 기계 판독 가능한 필드로 따로 선언하지 않았다.

## 변경

- `REFERENCE_RESEARCH_REPOSITORY_CONTRACT_v1.1_PROJECT_SOURCE_ADDENDUM.md`
  - `SUPERSEDED / HISTORICAL COMPATIBILITY RECORD — NON-AUTHORITATIVE` 배너로 강화.
  - 특정 후속 버전을 현행이라고 하드코딩한 문장을 제거.
  - 현재 권위는 오직 `REPOSITORY_MANIFEST.yaml`의 `repository_contract_addendum_path`로 판정하도록 통일.
- `REFERENCE_RESEARCH_REPOSITORY_CONTRACT_v1.2_PROJECT_SOURCE_ADDENDUM.md`
  - 동일한 비권위 배너와 manifest-only 권위 판정으로 통일.
- `REFERENCE_RESEARCH_REPOSITORY_CONTRACT_v1.3_PROJECT_SOURCE_ADDENDUM.md`
  - 명시적 SUPERSEDED / NON-AUTHORITATIVE 배너 추가.
  - 자기 자신을 현행이라고 지시하던 문장을 역사 상태 기록으로 강등.
  - 당시 검색 라우팅·필수 루트 트리도 현행 지침이 아니라 역사 기록임을 명시.
- `REPOSITORY_MANIFEST.yaml`
  - `authority_boundary` 추가.
  - active research roots: `registry/`, `works/`, `comparisons/`, `mc_candidates/`, `indexes/`, `audits/`.
  - legacy non-authoritative roots: `catalog/`, `history/`.
  - historical contract paths: v1.1 / v1.2 / v1.3.
  - 기본 연구 검색에서 legacy roots 제외, bootstrap authority에서 historical contracts 제외, 현재 권위는 manifest에서만 판정하도록 기계 판독 정책 추가.

## 변경하지 않은 것

- `catalog/`와 `history/`의 역사 자료를 삭제하거나 재작성하지 않음.
- `catalog/tables/execution-cards.csv`의 과거 값 자체를 손대지 않음.
- 현행 v1.4 addendum 수정 없음.
- SOP v7.1 / Repository Contract v1 / Schema v2 수정 없음.
- works/ 아래 작품 연구 기록, Source Scene, Macro, Micro, TH, PSE, PVAR 수정 없음.
- 새 연구층, 새 DB, Schema v3 생성 없음.
- 40~80화 적응형 대구간 순회 같은 현행 운영 단위를 과거 실행 카드 요구사항으로 취급하지 않음.

## 감사 판정

- 현행 연구 데이터 구조 자체는 유지 가능하며 대규모 재구성 필요 없음.
- 과거 실행 카드 값은 역사 자료로 보존하되 기본 연구 검색에서는 비권위 경로로 제외하는 것이 적절함.
- 과거 계약 파일이 자기 자신 또는 특정 옛 버전을 현행으로 가리키는 경로를 제거함.
- 새 채팅이나 도구가 루트 파일을 임의 순서로 발견하더라도 manifest를 확인하지 않은 과거 계약을 bootstrap 권위로 삼지 않도록 fail-closed 경계를 강화함.

## 변경 파일

- `REFERENCE_RESEARCH_REPOSITORY_CONTRACT_v1.1_PROJECT_SOURCE_ADDENDUM.md`
- `REFERENCE_RESEARCH_REPOSITORY_CONTRACT_v1.2_PROJECT_SOURCE_ADDENDUM.md`
- `REFERENCE_RESEARCH_REPOSITORY_CONTRACT_v1.3_PROJECT_SOURCE_ADDENDUM.md`
- `REPOSITORY_MANIFEST.yaml`
- `audits/RCPT-20260815-2244-GLOBAL-LEGACY-AUTHORITY-HARDENING.md`
- `indexes/recent_receipts.md` (index seal 예정)

## 다음 질문

실제 다음 참고작 연구 배치에서 bootstrap 검색이 `authority_boundary`를 따라 legacy roots와 historical contracts를 기본 후보에서 제외하고, works/indexes/현행 addendum으로만 진입하는지 검증한다.
