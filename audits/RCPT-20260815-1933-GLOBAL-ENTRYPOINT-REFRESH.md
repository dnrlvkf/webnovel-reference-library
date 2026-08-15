# GLOBAL 운영 정합성 영수증 — current entrypoint refresh

- receipt_id: `RCPT-20260815-1933-GLOBAL-ENTRYPOINT-REFRESH`
- date_time: `2026-08-15T19:33:00+09:00`
- work_id: `GLOBAL / REF-02 state sync`
- mode: `repository maintenance / entrypoint and state consistency audit`
- question: `현행 SOP v7·schema v2·scene retrieval contract 기준에서 과거 실행 규칙과 stale REF 상태가 새 채팅의 부트스트랩을 오염시키지 않도록 어떤 최소 정정이 필요한가`
- source_scope: `no new source-text research claim; repository operational metadata and routing only`
- base_sha: `6ec97aa61ab0e6e13100a655931f5805f8329e8c`
- branch: `agent/refresh-entrypoint-contracts`
- research_content_sha: `ab10b4b0346cb0a135ca20c1ac8d7dc1447ae9bd`
- final_sha: `ab10b4b0346cb0a135ca20c1ac8d7dc1447ae9bd`
- final_sha_mode: `self_excluding_receipt_and_index_finalization`
- remote_status: `branch_verified_before_pr`
- status: `complete_pending_merge`

## 조회

- current `main` HEAD and `REPOSITORY_MANIFEST.yaml`
- project-source `REFERENCE_RESEARCH_ANALYSIS_SOP_v7.md`
- project-source `REFERENCE_WORK_MODEL_SCHEMA_v2.md`
- `REFERENCE_RESEARCH_STANDARD_SOURCE_LOCK_v1.yaml`
- current addendum v1.3 and historical addenda v1.1/v1.2
- root `AGENTS.md`, `README.md`
- `indexes/scene_retrieval_contract.md`
- `catalog/INDEX.md` and legacy execution-card boundary identified in prior audit
- `registry/works.yaml`
- `works/REF-02/README.md`, `indexes/research.md`, `COMPLETION.md`
- `indexes/recent_receipts.md`

## 변경

- `REPOSITORY_MANIFEST.yaml`: `scene_retrieval_contract_path`, `expression_retrieval_path`를 명시하고 manifest schema를 1.6으로 갱신.
- `AGENTS.md`: 신규 연구/집필 검색을 manifest와 `works/*/indexes`에서 시작하도록 수정하고 Source Scene 비강제 부분검색 계약을 필수 라우팅으로 추가. `catalog/` 실행 카드 필드를 현행 실행 권위에서 제외.
- `README.md`: Source Scene 집필 검색 계약과 `catalog/` 레거시 경계를 명시하고 완료 작품의 `COMPLETION.md` 우선순위를 추가.
- current v1.3 addendum: scene/expression/prose retrieval 세 경로의 역할과 비강제 Source Scene 원칙을 명시.
- v1.1/v1.2 addendum: 삭제하지 않고 `SUPERSEDED / HISTORICAL COMPATIBILITY RECORD`로 표기.
- `registry/works.yaml`: REF-02를 1~284 complete/saturated 상태와 재개 조건으로 동기화.
- `works/REF-02/README.md`: stale 1~10 / next 11~20 지시와 오래된 BASE SHA 제거, completion/reopen 조건으로 교체.
- `works/REF-02/indexes/research.md`: current operating SOP를 매니페스트에서 해석하도록 바꾸고 과거 SOP 버전은 provenance로 한정.
- `catalog/INDEX.md`: 레거시·비권위 경고와 실행 카드 비자동화 경계를 상단에 추가.

## 연구 트랙 영향

이번 변경은 새 원문 연구가 아니므로 CHARACTER·RELATIONSHIP·EVENT·STORY·PROSE·TECHNIQUE의 기존 판정을 생성·수정하지 않는다. 운용 진입점과 상태 메타데이터만 정합화했다.

## 판정

- SUPPORTED: `indexes/scene_retrieval_contract.md`는 현행 집필 검색의 필수 안전장치로 루트 진입점에 연결되어야 한다.
- CONTRADICTED: `catalog/` 또는 legacy execution-card fields가 신규 집필의 기본 실행 권위라는 해석.
- CONTRADICTED: REF-02가 현재 1~10 완료 후 11~20 진행 대기라는 상태.
- SUPPORTED: REF-02는 현재 source boundary 1~284에 대해 complete/saturated이며 새 원천 또는 구체적 반례가 있을 때만 재개한다.
- SUPPORTED: v1.1/v1.2 addenda는 역사 기록으로 보존하되 현행 부트스트랩 권위를 갖지 않는다.

## 감사

- BASE→research_content compare: 10 files modified, branch `ahead`, `behind_by: 0`.
- historical files were preserved; no deletion or force update.
- no new research ID, TH, Macro, Micro, PSE, PVAR created.
- no source-text claim added.
- current project-source SOP v7 and schema v2 remain the approved research/model standards.

## HOLD

- `REFERENCE_RESEARCH_REPOSITORY_CONTRACT_v1.md` base contract body is project-source canonical and was not rewritten in this maintenance change.
- historical `catalog/tables/execution-cards.csv` contents were not rewritten; their authority is isolated at root and catalog entrypoints instead.

## 다음 질문

이 정합성 정리 뒤 실제 새 집필 검색 테스트에서 `matched_problem / mismatch_boundary / usable_judgment / do_not_import` 부분 검색이 외부 Source Scene의 결합 복제를 줄이면서도 필요한 캐릭터·관계·사건·독자 그림 판단을 충분히 회수하는가.
