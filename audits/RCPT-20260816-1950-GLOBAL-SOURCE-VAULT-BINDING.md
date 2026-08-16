# GLOBAL 연구 영수증

- receipt_id: `RCPT-20260816-1950-GLOBAL-SOURCE-VAULT-BINDING`
- date_time: `2026-08-16T19:50:00+09:00`
- work_id: `GLOBAL / REF-02 / REF-46 / REF-47`
- mode: `repository maintenance / cross-project source vault binding + canonical re-entry E2E validation`
- question: `파생 연구층에서 선택한 참고 후보가 프로젝트 첨부 원문에 의존하지 않고 정본 source identity와 접근 제어된 transport를 따라 실제 원문 회차 전체까지 다시 내려갈 수 있는가`
- source_scope: `no new story/research claim; source transport binding + raw source identity verification + PSE-REF47-0018 canonical re-entry test`
- base_sha: `92b38c7cf208476a1c02a17fde612141d33a41fc`
- content_commit_sha: `50ae261568f99ec3c6ae1454a2fb7e770d6cba26`
- final_sha_mode: `self_excluding_receipt_and_recent-index finalization`
- research_content_sha: `c87aa6cf2b7431ad4b76cb4653b5af7b46452a9f9435cc4ba49bcd994d41fde9`
- status: `transport_ready_with_external_project_acceptance_hold`

## 표준과 기존 계약
- 승인 표준은 기존 lock과 일치하는 `REFERENCE_RESEARCH_ANALYSIS_SOP_v7.1.md`, `REFERENCE_RESEARCH_REPOSITORY_CONTRACT_v1.md`, `REFERENCE_WORK_MODEL_SCHEMA_v2.md`를 유지했다.
- 기존 `indexes/source_reentry_contract.md`의 핵심 원칙인 `source identity != source access`, current-run raw-byte verification, 공개 저장소 raw source 금지를 유지했다.
- 새 연구층이나 Schema v3는 만들지 않았다.

## BASE와 작업 중 정본 이동
- 작업 시작 정본 BASE SHA: `92b38c7cf208476a1c02a17fde612141d33a41fc`.
- 준비 과정에서 실수로 `audits/.source-vault-binding-placeholder`가 생성된 커밋 `6e66c86605d6b0d7cc33e4f0a32bbfb2ce7bcc47`이 main에 올라갔다.
- 즉시 같은 파일을 삭제한 커밋 `11e04322eb3b03ec9b1f4907e62ea4969e10bca8`을 반영했고, 삭제 뒤 Git tree는 이전 정본 tree `4c1afeaa84e74765054c5a0cc63c1f189e7ba294`로 복귀했다.
- 이 placeholder는 연구 내용·원천·ID·인덱스에 영향이 없었으며 본 영수증에서 운영 실수로 명시한다.

## private source vault
- provider: `Google Drive`
- folder_id: `11bd2KIk6LJsGX9zPeue0StX6DlNfPuQW`
- folder role: `webnovel-reference-source-vault`
- source files are stored as raw `text/plain`; Google Docs native conversion을 사용하지 않았다.
- Drive metadata에서 세 파일 모두 `shared: false`, owner-only 권한을 확인했다.
- 공개 GitHub 연구 저장소에는 원문 바이트나 실제 원문 파일명을 저장하지 않았다.

## VERIFIED source bindings
### REF-02 / SRC-COL2-027
- Drive file_id: `17nvr-SaeIORyLNDA3ZGeU8FAu_cX8w02`
- expected/raw byte size: `4366295`
- expected/raw SHA-256: `17b0f41b6b64eefe6f3d1354d22e2d75529be153b1f0f7fd71f00a016f96b766`
- encoding: `utf-8`
- result: `VERIFIED_MATCH`

### REF-46 / SRC-LEGACY-REF46
- 기존 legacy bridge의 exact source identity를 새 opaque source ID `SRC-LEGACY-REF46`에 결박했다.
- Drive file_id: `1dy1huiWN5uO9VTwjHCCqgoAmc_IvEewz`
- expected/raw byte size: `14520163`
- expected/raw SHA-256: `9cf9d175c228c02e960a04f3d721f29bb4362b380065f2fd200b828291ba1191`
- encoding: `utf-8`
- result: `VERIFIED_MATCH`

### REF-47 / SRC-DIRECT-001
- Drive file_id: `1Ipfl9-ckUFLTjK1j_l6FF4kC48Cg2Rdy`
- expected/raw byte size: `5927798`
- expected/raw SHA-256: `95d22f155d582ec702142b906161f4b36241627a76cdf858ff9b39cd6d686a4e`
- encoding: `utf-16`
- result: `VERIFIED_MATCH`
- source transport 검증은 기존 `partial_header_verification` 경계를 확대하지 않는다.

## canonical E2E re-entry test
프로젝트 첨부 TXT를 검색 경로로 사용하지 않고 다음 사슬을 다시 밟았다.

`PSE-REF47-0018`
→ canonical GitHub `source_locations: SRC-DIRECT-001 / ep328 / lines 175413-175457`
→ canonical `registry/source_inventory.yaml`
→ Drive file ID `1Ipfl9-ckUFLTjK1j_l6FF4kC48Cg2Rdy`
→ raw Drive download
→ current-run full source SHA/size verification
→ PSE segment verification
→ ep328 full-episode verification

검증 결과:
- raw source SHA-256: `95d22f155d582ec702142b906161f4b36241627a76cdf858ff9b39cd6d686a4e` / PASS
- raw source size: `5927798` / PASS
- `PSE-REF47-0018`, lines `175413-175457`, LF-normalized SHA-256: `1d7013f1320c636aeaf4ed581b2d090415a4e6185b0e459aafacf5b1e18efa1e` / PASS
- `FULL-EP-REF47-0328`, lines `175043-175492`, LF-normalized SHA-256: `8b505a15a618ecdde9058884a6c247cf193b1ecbaef6de52acd54a2ad2f5276d` / PASS
- 판정: `canonical PSE → source_id → access-controlled locator → current-run VERIFIED_MATCH → exact segment → full episode` E2E PASS.

## REF-47 legacy normalization correction
- `FULL-EP-REF47-0001`의 기존 hash `a4085b570676be7cd9fc2e59942651d7ad151d7c62286336445d7654460c1368`는 원문 불일치가 아니었다.
- 같은 471-862행을 CRLF로 결합하고 마지막 CRLF를 붙일 때 기존 hash가 재현됐다.
- LF-normalized 값은 `133528e6f6ae7e85964cda2cb08f4f671f90304488edcd47fd0cec5855009570`.
- `SOURCE-BRIDGE-REF47.md`에서 ep1만 legacy CRLF-normalization 예외임을 명시하고, 다른 full-episode 기본 규칙을 LF로 유지했다.

## 변경 파일
- `registry/works.yaml`
- `registry/source_inventory.yaml`
- `works/REF-46/source_registry/SOURCE-BRIDGE-REF46.md`
- `works/REF-47/source_registry/SOURCE-BRIDGE-REF47.md`
- `indexes/source_reentry_contract.md`
- `audits/RCPT-20260816-1950-GLOBAL-SOURCE-VAULT-BINDING.md`
- `indexes/recent_receipts.md` (후속 seal에서 갱신)

## 여섯 트랙 영향
- CHARACTER: 연구 판단 변경 없음. 향후 원문 판단 좌표에서 실제 source로 재진입 가능.
- RELATIONSHIP: 연구 판단 변경 없음.
- EVENT: 연구 판단 변경 없음.
- STORY: 연구 판단 변경 없음. full-episode reread transport만 실체화.
- PROSE: PSE에서 source segment와 full episode까지 current-run 재진입 E2E를 실제 검증.
- TECHNIQUE: Macro/Micro/TH를 원문 대체 실행 규칙으로 승격하지 않고 원문 재진입의 상위 검색 좌표로 유지.

## 반례·HOLD
- `Drive에 한 번 올렸으니 이후 실행은 SHA 검증을 생략해도 된다`: `CONTRADICTED`. 매 실행은 locator raw bytes를 canonical identity와 다시 대조해야 한다.
- `세 작품이 결박됐으니 collection 45개가 모두 transport-ready다`: `CONTRADICTED`. 현재 verified source는 3개뿐이고 나머지 42개는 `UNBOUND`.
- REF-47의 2-166화 episode header 전체: 기존과 동일하게 미검증. ep1 한 건과 167-350의 기존 검증 범위만 유지.
- 실제로 별도의 ChatGPT 프로젝트 UI로 전환해 같은 절차를 독립 재현하는 acceptance test: 현재 세션에는 프로젝트 전환 실행 도구가 없어 `HOLD_EXTERNAL_PROJECT_REPRODUCTION`. 다만 transport 자체는 프로젝트 첨부가 아니라 계정 연결 Drive locator로 검증됐다.

## 감사 결과
- raw source는 public repository에 저장되지 않았다.
- Drive 저장본은 세 파일 모두 raw-download SHA/size가 canonical identity와 일치했다.
- 기존 작품 연구 판단과 Source Scene/PSE/PVAR/Macro/Micro/TH ID는 수정하지 않았다.
- source transport와 episode boundary 권한을 분리해 REF-47 미검증 경계를 자동 승격하지 않았다.
- source collection 전체가 아니라 실제 검증된 3 source만 `VERIFIED_MATCH`로 승격했다.

## 다음 운영 질문
1. 다음 실제 집필 프로젝트에서 REF-02/46/47 중 하나가 후보로 검색될 때 동일 locator를 따라 current-run raw identity + full-episode reread가 재현되는가.
2. 나머지 42 source는 미리 대량 이관하지 않고 실제 연구/집필 검색에 필요해질 때 source identity를 확인한 뒤 on-demand 결박할 것인가.
3. transport 재현 이후에는 기존 Source Scene↔5트랙↔PSE/PVAR↔Macro/Micro/TH 연결성 감사 샘플을 수행하고 참고작 연구를 재개한다.
