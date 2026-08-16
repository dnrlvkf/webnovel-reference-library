# REF-47 연구 영수증

- receipt_id: `RCPT-20260816-2037-REF47-CONNECTIVITY-PILOT`
- date_time: `2026-08-16T20:37:00+09:00`
- work_id: `REF-47`
- research_mode: `작품 전체 왕복 채굴 / research-layer connectivity pilot`
- question: `서로 다른 기능의 기존 장면에서 원문→Source Scene→작품 모델/PROSE→PSE/PVAR/TH 상행과 집필 문제→연구층→Source Scene/PSE→원문 하행이 새 스키마나 강제 파일 생성 없이 실제로 왕복되는가`
- base_sha: `f92ec6d8a49edc8bbf33ff33e17f325aeb904a95`
- content_commit_sha: `3bbfdf6e8cde0b2b15f974a07e67b30f38c4d584`
- final_sha_mode: `self_excluding_receipt_finalization`
- status: `PASS_WITH_TWO_STALE_REVERSE_LINKS_REPAIRED`

## 원문 범위
- `SRC-DIRECT-001 / ep256 / SC-REF47-0007 / lines 137225-137297`
- `SRC-DIRECT-001 / ep298 / SC-REF47-0015 / lines 158903-159005`
- `SRC-DIRECT-001 / ep331 / SC-REF47-0017 / lines 176495-176571`
- full-episode boundary check: `ep331 / lines 176465-176880`

## 조회한 기록
- `REPOSITORY_MANIFEST.yaml`
- Project Source `REFERENCE_RESEARCH_ANALYSIS_SOP_v7.1.md`
- Project Source `REFERENCE_RESEARCH_REPOSITORY_CONTRACT_v1.md`
- Project Source `REFERENCE_WORK_MODEL_SCHEMA_v2.md`
- `indexes/research_layer_connectivity.md`
- `indexes/source_reentry_contract.md`
- `works/REF-47/source_registry/SOURCE-BRIDGE-REF47.md`
- `works/REF-47/indexes/source_scenes.md`
- `SOURCE-SCENES-REF47-0005-0008.md`
- `SOURCE-SCENES-REF47-0014-0017.md`
- `PSE-REF47-0007`, `PSE-REF47-0015`, `PSE-REF47-0017`
- `PRO-REF47-0002`, `PRO-REF47-0004`, `PRO-REF47-0006`
- `PVAR-REF47-0002`, `PVAR-REF47-0004`, `PVAR-REF47-0005`
- `TH-REF47-01`
- `CHR-REF47-0001`, `REL-REF47-0002`는 장기 모델 연결 경계를 확인하기 위해 조회했으나 파일럿 장면의 익명 역할 슬롯과 직접 동일시하지 않음.

## 원문 확인
- Google Drive canonical locator에서 `SRC-DIRECT-001` raw bytes를 재다운로드.
- raw byte size `5,927,798`, SHA-256 `95d22f155d582ec702142b906161f4b36241627a76cdf858ff9b39cd6d686a4e` 일치.
- SC-0007 normalized segment SHA `6439dea638e206cbe02318b38ee7e90d3239e179733225e4da4750534b117a8d` 일치.
- SC-0015 normalized segment SHA `f6ca299d9a6ad557cbeaad6e691dcc230e28b8ff275d41b2f85f2f21b08e64b2` 일치.
- SC-0017 normalized segment SHA `c659e68a4d5cd9a0ad306ff13332b65433abddce22c80a694bbb3a000fce840d` 일치.
- ep331 full-episode normalized SHA `4605c6eca8b2dfeb86ca6b95b6edd4bfc07ec12025cffbfb44bc613bd8b91bca` 일치.

## 세 장면 왕복 감사

### SC-REF47-0007 — 역할에 따른 질문권·답변 의무 이동
- 상행: source → Source Scene observed chain → `PSE-REF47-0007` → `PRO-REF47-0002` / `PVAR-REF47-0002` → 후속 대화 결속 비교 `PRO-REF47-0004` / `PVAR-REF47-0004`.
- 하행: `역할에 따라 질문권/답변 의무가 이동하는 대화` → PVAR/PSE → SC-0007 → ep256 source reread.
- 발견: `PVAR-REF47-0004`가 `PSE-REF47-0007`을 가리키지만 PSE 쪽 역링크와 Source Scene `linked_existing`에 후속 PVAR가 누락됨.
- 조치: 양쪽 역링크 보강.

### SC-REF47-0015 — 전문 판정에서 보고·지휘 권한 충돌로 이동
- 상행: source → Source Scene의 CHARACTER/RELATIONSHIP/EVENT/PROSE observed chain → `PSE-REF47-0015` → `PRO-REF47-0004` / `PVAR-REF47-0004`.
- 하행: `같은 사건을 서로 다른 비용 기준으로 보고 질문 기능이 책임 공격으로 바뀌는 장면` → PVAR/PSE → SC-0015 → ep298 source reread.
- 판정: 기존 양방향 링크 정상. 별도 EVT 파일을 만들지 않아도 Source Scene의 상태 변화와 PROSE 증거로 현재 질문을 손실 없이 복원 가능.

### SC-REF47-0017 — 자기 판단 기준으로 기억/삶 수용 선택을 확정
- 상행: source → Source Scene CHARACTER/EVENT/PROSE chain → `PSE-REF47-0017` → `PRO-REF47-0004` / `PVAR-REF47-0004` → 후속 장기 재분류 연구 `PRO-REF47-0006` / `PVAR-REF47-0005` → `TH-REF47-01`.
- 하행: `독자가 아는 관계를 현재 인물의 체험 기억 부재 때문에 다시 분류해야 하는 장면` → TH/PVAR/PRO → PSE-0017 → SC-0017 → ep331 full episode reread.
- 발견: 후속 `PRO-0006/PVAR-0005/TH-01`이 SC-0017을 가리키지만 Source Scene의 `linked_existing`은 이전 연구 상태에 머물러 있었음.
- 조치: Source Scene 역링크 보강.

## 작품 모델 갱신
- CHARACTER: 신규 장기 캐릭터 파일 없음. Source Scene의 판단 기준→선택 연결로 충분한 장면에서 파일 생성을 강제하지 않는 현재 계약이 작동함을 확인.
- RELATIONSHIP: SC-0007/0015의 질문·차단·판정·지휘 권리 이동이 Source Scene에서 직접 추적됨. SC-0017을 기존 장기 관계 파일의 익명 슬롯과 억지 동일시하지 않음.
- EVENT: SC-0015의 `현장 분류→보고 여부→세력 분리`, SC-0017의 `수용 여부→자기 증거 확인→선택 조건 성립`을 Source Scene에서 상태 변화로 확인. 연결성만을 위해 신규 EVT를 만들지 않음.
- STORY: 장면의 실제 사건 운동과 독자에게 먼저 보이는 감각/표정/집단 반응이 Source Scene의 reader_picture/제시 사슬에서 구분됨. 별도 STORY 파일 신규 생성 불필요.
- PROSE: PSE/PVAR/PRO 상하행은 작동. 후속 비교 연구가 추가될 때 구 PSE/Source Scene 역링크가 갱신되지 않을 수 있는 drift를 확인하고 2건 보정.
- TECHNIQUE: SC-0017에서 Source Scene→PSE/PVAR→TH와 TH→PSE→Source Scene→원문 하행이 성립. `observed_chain`을 추천 순서로 승격하지 않음.

## 생성·수정·폐기
- 신규 연구 ID: 없음.
- 수정: `PSE-REF47-0007` — `PVAR-REF47-0004` 역링크 추가.
- 수정: `SC-REF47-0007` — `PVAR-REF47-0004` 후속 비교 링크 추가.
- 수정: `SC-REF47-0017` — `PRO-REF47-0006`, `PVAR-REF47-0005`, `TH-REF47-01` 후속 장기 연구 링크 추가.
- 폐기/강등: 없음.
- Macro/Micro: 생성하지 않음. 연결 감사만을 위해 독립 검색 단위를 늘릴 근거 없음.

## 반례·보류
- `모든 Source Scene에 CHARACTER/RELATIONSHIP/EVENT/STORY 별도 파일이 있어야 연결이 완성된다`: `CONTRADICTED`. 현재 연구 질문을 손실 없이 왕복할 수 있으면 장면 근거와 기존 상위 모델 연결로 충분하다.
- `역링크 누락은 새 Schema/edge DB가 필요하다는 증거다`: `CONTRADICTED`. 두 건 모두 후속 연구가 생긴 뒤 이전 파일 메타데이터가 갱신되지 않은 운영 drift였다.
- 파일럿 3장면만으로 모든 REF의 기존 기록이 무결하다고 일반화하지 않는다. 신규/갱신 배치마다 connectivity audit를 유지한다.

## 감사 결과
- `PASS`: 원문→장면→판단/사건/표현→장기 모델/TH 상행 가능.
- `PASS`: 집필 문제→PRO/PVAR/TH→PSE/Source Scene→실제 원문 하행 가능.
- `PASS`: SC-0015 healthy control은 수정 없이 왕복.
- `PASS after repair`: SC-0007, SC-0017의 stale reverse links 최소 보강.
- Schema v3, 새 edge taxonomy, 새 장면 레코드 유형 불필요.
- 원문 표면·고유명은 연구층에 새로 복제하지 않음.

## 변경 파일
- `works/REF-47/prose/evidence/PSE-REF47-0007.md`
- `works/REF-47/source_scenes/SOURCE-SCENES-REF47-0005-0008.md`
- `works/REF-47/source_scenes/SOURCE-SCENES-REF47-0014-0017.md`
- `works/REF-47/research_receipts/RCPT-20260816-2037-REF47-CONNECTIVITY-PILOT.md`
- `indexes/recent_receipts.md` (seal 단계)

## 다음 질문
- 기반 계약 추가 작업보다 새 참고작 연구를 재개한다.
- 향후 연구 배치에서 `새 상위/비교 연구가 기존 Source Scene/PSE를 가리킬 때 기존 파일의 reverse link도 갱신되었는가`를 연결 감사에 포함한다.
- 동일 질문으로 유사 reverse-link drift가 반복될 경우에만 자동 검증 도구나 스키마 수준 보강을 재검토한다.
