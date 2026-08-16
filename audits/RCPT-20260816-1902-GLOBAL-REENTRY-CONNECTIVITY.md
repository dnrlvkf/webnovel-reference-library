# GLOBAL 연구 영수증

- receipt_id: `RCPT-20260816-1902-GLOBAL-REENTRY-CONNECTIVITY`
- date_time: `2026-08-16T19:02:00+09:00`
- work_id: `GLOBAL`
- mode: `repository maintenance / source re-entry transport + research-layer connectivity`
- question: `파생 연구층에서 찾은 후보가 다른 집필 프로젝트에서도 실제 원문 회차 전체로 안전하게 재진입하고, 원문↔Source Scene↔5트랙↔PSE/PVAR↔Macro/Micro/TH를 양방향으로 추적하려면 어떤 최소 계약이 필요한가`
- source_scope: `no new source-text research claim; Project Source standards + current canonical manifest/registries/retrieval contracts/source bridges only`
- base_sha: `118faf46935cf1d8c3ed530b4b29328f05ce2240`
- content_commit_sha: `ab06d85d7252f050cf1c91e33a1f4b951b06325b`
- final_sha_mode: `self_excluding_receipt_finalization`
- research_content_sha: `79efdf8d7357be4693a9ee558560a4e9a82d5c5f918831e453fe0f4365b29c3e`
- remote_status: `core_changes_on_main; receipt_seal_pending`
- status: `complete_with_transport_hold`

## 표준 검증
- Project Source `REFERENCE_RESEARCH_ANALYSIS_SOP_v7.1.md` SHA-256 `3803ff35ff9d68211aa2ab655b76dd387567f441a424f41e2a8e5884722fe8c5`, 120486 bytes 직접 재검증.
- Project Source `REFERENCE_RESEARCH_REPOSITORY_CONTRACT_v1.md` SHA-256 `8a6479621af6d1196433ca5760ae727eb5ccc1b876dea468df3faafc964e304e`, 12579 bytes 직접 재검증.
- Project Source `REFERENCE_WORK_MODEL_SCHEMA_v2.md` SHA-256 `1e6f5188749130900349cc7f54a9c07f888946d912485124fe45c7b4f50563f8`, 19277 bytes 직접 재검증.
- GitHub `REFERENCE_RESEARCH_STANDARD_SOURCE_LOCK_v1.yaml`과 파일명·SHA-256·바이트 크기 일치. `HOLD_STANDARD_SOURCE` 없음.

## 조회한 정본 기록
- `REPOSITORY_MANIFEST.yaml`
- `REFERENCE_RESEARCH_STANDARD_SOURCE_LOCK_v1.yaml`
- `REFERENCE_RESEARCH_REPOSITORY_CONTRACT_v1.4_PROJECT_SOURCE_ADDENDUM.md`
- `registry/works.yaml`
- `registry/source_inventory.yaml`
- `works/REF-46/source_registry/SOURCE-BRIDGE-REF46.md`
- `works/REF-47/source_registry/SOURCE-BRIDGE-REF47.md`
- `indexes/scene_retrieval_contract.md`
- `indexes/expression_retrieval.md`
- `indexes/prose_realization_retrieval.md`
- `audits/RCPT-20260815-2209-GLOBAL-SOURCE-REENTRY.md`
- `indexes/recent_receipts.md`

## 확인된 문제
- 현행 계약은 파생 연구층을 원문 재진입 좌표로 제한하고 full-episode reread를 요구하지만, 다른 ChatGPT 프로젝트가 canonical source bytes를 실제로 읽을 cross-project transport locator는 정본에 존재하지 않았다.
- `registry/source_inventory.yaml`은 source identity와 일부 구간 좌표를 보존하지만 transport/access와 identity를 구분하지 않았다.
- REF-46/REF-47 source bridge도 원문 SHA·encoding·episode/line 좌표는 있으나 다른 프로젝트가 접근할 repository/path locator는 없었다.
- 현재 GitHub 계정에서 참고작 원문 전용 비공개 source vault를 확인하지 못했다. 따라서 transport를 추정하거나 `SOURCE_READY`로 허위 승격하지 않는다.
- Schema v2는 이미 source_scenes/source_locations 및 related_* 링크를 허용한다. 연결성 문제를 이유로 Schema v3나 새 연구층을 만들 필요는 없었다.

## 변경
- `REPOSITORY_MANIFEST.yaml`
  - schema `1.6 → 1.7`.
  - `indexes/source_reentry_contract.md`, `indexes/research_layer_connectivity.md`를 현행 권위 경로로 등록.
  - 파생층은 좌표, accessible transport는 VERIFIED_MATCH 필수, public raw source 저장 금지, transport unbound는 SOURCE_LIMITED라는 정책을 명시.
- `registry/source_inventory.yaml`
  - source identity와 cross-project transport를 분리.
  - 현재 cross-project transport를 `unbound / project_scoped_only`로 명시.
  - 기존 bound source의 source_id/hash/size/boundary는 변경하지 않음.
- `registry/works.yaml`
  - REF-02/46/47의 현재 재진입 상태를 `transport_unbound`, 범위를 `project_scoped_only`로 명시.
- `indexes/source_reentry_contract.md` 신규.
  - `UNBOUND / BOUND_UNVERIFIED / VERIFIED_MATCH / SOURCE_LIMITED / REVOKED` 상태 정의.
  - source identity와 transport locator 분리.
  - opaque private GitHub source-vault locator 계약과 VERIFIED_MATCH 절차 정의.
  - 파생 연구층→source_id→identity→transport→full episode reread 하행 사슬 정의.
- `indexes/research_layer_connectivity.md` 신규.
  - 기존 Schema v2 필드만 사용해 Source↔Source Scene↔5트랙↔PSE/PVAR↔Macro/Micro/TH의 양방향 연결 규칙 정의.
  - Source Scene을 evidence/re-entry hub로 유지.
  - `observed_chain`을 `recommended_chain`으로 바꾸지 않는 기존 방화벽 유지.

## 여섯 트랙별 영향
- CHARACTER: 판단→선택→EVENT→후속 선택을 Source Scene으로 역추적하는 최소 연결을 명시.
- RELATIONSHIP: 권리·책임 변화가 촉발 EVENT와 후속 권리 행사로 증명되도록 연결.
- EVENT: 상태 변경이 관계·정보·권한·자원·목표 변화로 이어지는 링크를 명시.
- STORY: 실제 EVENT와 제시/생략/압축/지연, 독자 정보 상태를 분리 연결.
- PROSE: 장면 조건→반응 채널→실제 표현→독자/상대 해석을 Source Scene/PSE/PVAR로 연결하고 집필 전 원문 재진입을 강제.
- TECHNIQUE: Macro/Micro/TH를 별도 태그 DB로 만들지 않고 5트랙·Source Scene·원문에 역링크하는 증거/검색층으로 유지.

## 반례·보류·HOLD
- `source identity가 있으니 다른 프로젝트에서도 읽을 수 있다`: `CONTRADICTED`. identity와 access는 다르다.
- `연구 프로젝트에서 한 번 원문을 읽었으면 다른 프로젝트도 VERIFIED_MATCH다`: `CONTRADICTED`.
- `공개 참고작 라이브러리에 원문을 넣으면 해결된다`: 채택하지 않음. 공개 raw-source 저장을 금지.
- `새 Schema v3/edge DB가 필요하다`: 채택하지 않음. Schema v2 관계 필드로 충분.
- 실제 cross-project source vault/locator: `HOLD / UNBOUND`. 따라서 다른 프로젝트에서 SOURCE_LIMITED가 완전히 해제되었다고 보고하지 않는다.

## 감사 결과
- BASE→content commit diff는 의도한 5개 경로만 변경.
- 기존 REF/Source Scene/PSE/PVAR/Macro/Micro/TH ID와 연구 판단을 일괄 이관하거나 재작성하지 않음.
- raw source·실제 작품명·private project repository path 유출 없음.
- 기존 source identity/hash/size/boundary 값 보존.
- 새 연구층·Schema v3·영구 edge taxonomy를 만들지 않음.
- `Fast source re-entry`를 위해 검증을 약화시키지 않고 transport가 없을 때 fail-closed 상태를 더 명확히 함.

## 변경 파일
- `REPOSITORY_MANIFEST.yaml`
- `registry/works.yaml`
- `registry/source_inventory.yaml`
- `indexes/source_reentry_contract.md`
- `indexes/research_layer_connectivity.md`
- `audits/RCPT-20260816-1902-GLOBAL-REENTRY-CONNECTIVITY.md`
- `indexes/recent_receipts.md` (seal에서 갱신)

## 다음 연구/운영 질문
1. 접근 제어된 private source vault를 opaque `source_id` 경로로 만들고 기존 canonical source identity에 결박할 것인가.
2. locator 결박 뒤 다른 실제 집필 프로젝트에서 `candidate → Source Scene/PSE → source_id → VERIFIED_MATCH → full episode reread → current-work rewrite` end-to-end 테스트가 통과하는가.
3. end-to-end 실패가 library locator 문제가 아니라 consumer capability 문제로 확인될 때만 webnovel orchestrator 수정 여부를 재검토한다.
