# REF-47 연구 영수증

- receipt_id: `RCPT-20260816-2112-REF47-RIGHTS-FOLLOWUP`
- date_time: `2026-08-16T21:12:00+09:00`
- researcher: `ChatGPT`
- work_id: `REF-47`
- research_mode: `작품 전체 왕복 채굴 / 현재 관계 권리 후속 검증`
- question: `정체·기억 재분류 뒤 새로 열린 정보·접근·신뢰 권리가 후속 행동에서 실제로 유지되는가, 아니면 일회적 예외인가`
- source_scope: `SRC-DIRECT-001 / ep332, ep335, ep339, ep350 full episodes + SC-REF47-0018~0021`
- base_sha: `3be2f1a406c3cdf3425494f4b6ee2f1872679d98`
- content_commit_sha: `d5972066e80b7bc38d0cddc9be9a591d4b485157`
- final_sha_mode: `self_excluding_receipt_finalization`
- status: `complete`

## 조회한 기록

- `REPOSITORY_MANIFEST.yaml`
- Project Source `REFERENCE_RESEARCH_ANALYSIS_SOP_v7.1.md`
- Project Source `REFERENCE_RESEARCH_REPOSITORY_CONTRACT_v1.md`
- Project Source `REFERENCE_WORK_MODEL_SCHEMA_v2.md`
- `works/REF-47/source_registry/SOURCE-BRIDGE-REF47.md`
- `works/REF-47/relationships/REL-REF47-0002.md`
- `works/REF-47/threads/TH-REF47-01.md`
- `works/REF-47/indexes/source_scenes.md`
- `works/REF-47/indexes/relationships.md`
- `works/REF-47/indexes/threads.md`
- `works/REF-47/research_batches/BATCH-20260816-PRIOR-KNOWLEDGE-RECLASSIFICATION.md`
- `works/REF-47/audits/AUD-20260816-PRIOR-KNOWLEDGE-RECLASSIFICATION.md`
- `works/REF-47/research_receipts/RCPT-20260816-2037-REF47-CONNECTIVITY-PILOT.md`
- 기존 `PRO-REF47-0006`, `PSE-REF47-0019`, `PVAR-REF47-0005` 연결 범위

## 원문 확인

- canonical source identity: SHA-256 `95d22f155d582ec702142b906161f4b36241627a76cdf858ff9b39cd6d686a4e`, raw byte size `5927798`, UTF-16.
- ep332: `176881-177376` / normalized full-episode SHA `fd57213dc9e4c253153629322c82570c5f84810383ff329704d274c2c20313a0`.
- ep335: `178205-178568` / `dddedf863541993bea92ba8a06f0bd8d3ad619f29fa42096966dfeb62c524a40`.
- ep339: `179961-180428` / `a96e006b896463818523471b6b34935985f674639dc3e23e0c91d5bb9d2765a6`.
- ep350: `185225-185651` / `40a14817adc65dee5143a9acbd7706b7419b2656bc4ce42e098122a039d32701`.
- `SC-REF47-0018`: ep332 `177071-177163` / `e6d5bef266cc0c0b7c581f6d94a301728f1e37ec4a7baabcf7d7e2386b5b3eec`.
- `SC-REF47-0019`: ep335 `178205-178361` / `db0cced66c3a6dea489b75c1d4492ac46d29bb8ac2f54db107bf7539f8043416`.
- `SC-REF47-0020`: ep339 `179973-180117` / `3a27b110b11ee0caeff0b2028873e890524fb958bba7c982d1d7f05358442d88`.
- `SC-REF47-0021`: ep350 `185227-185529` / `1f2e07d3baa278f72470209d108c0932780bfe2e5b6b796d485880eff200d7e0`.

## 작품 모델 갱신

### CHARACTER
- 신규 CHR 없음.
- 현재 동행자 A가 숨은 의도의 공유 범위를 스스로 제한하면서도 실제 저지 역할은 수행하는 판단을 Source Scene/REL/TH에 연결했다.

### RELATIONSHIP
- `REL-REF47-0002` 보강.
- `SUPPORTED`: 과거 정체가 확정되지 않아도 현재 행동으로 제한된 접근·정보·대립/저지 권리가 먼저 생성될 수 있다.
- `SUPPORTED`: ep332 위임 → ep335 실제 행사/비밀 보존 → ep339 감시 인지 후 채널 유지 → ep350 사적 기록 전달로 권리가 반복·확대된다.

### EVENT
- 신규 EVT 없음.
- ep332 역할 위임, ep335 역할 행사, ep339 정보 경계 재설정, ep350 사적 정보 확대를 Source Scene 상태 변화로 보존했다.

### STORY
- 정체 동일성 승인과 현재 관계 권리 생성을 분리해 제시한다는 후반 장기 배열을 확인했다.
- ep350은 독립적 감정 예외가 아니라 선행 권리 변화의 확대 회수로 재분류했다.

### PROSE
- 신규 PSE/PVAR 없음.
- ep332/335/339은 특정 문장 표면보다 공간·정보 비공개·감시 차단/복구가 행동과 결합되는 방식이 핵심이라 Source Scene으로 저장했다.
- ep350 저수준 재분류는 기존 `PSE-REF47-0019` / `PVAR-REF47-0005`를 재사용했다.

### TECHNIQUE
- `TH-REF47-01` 보강.
- 기존 `과거 권리 자동 이전 방지` 메커니즘에 `현재 행동으로 새 권리 생성 → 후속 행동으로 행사·유지·확대`를 연결했다.
- 신규 `SC-REF47-0018~0021` 생성.

## 생성·수정·폐기

- 생성: `SC-REF47-0018`, `SC-REF47-0019`, `SC-REF47-0020`, `SC-REF47-0021`.
- 생성: `BATCH-20260816-RIGHTS-FOLLOWUP`, `AUD-20260816-RIGHTS-FOLLOWUP`, 본 연구 영수증.
- 수정: `REL-REF47-0002`, `TH-REF47-01`, source bridge, relationship/thread/source-scene indexes.
- 신규 TH: 없음.
- Macro: 생성하지 않음. REL+TH+SC에서 검색 가치가 중복 없이 보존됨.
- Micro: 생성하지 않음. 특정 표현보다 장면의 권리 배분·후속 행동 사슬이 작동 핵심임.
- 신규 PSE/PVAR/CHR/EVT/STORY 파일: 없음.
- 폐기/강등: 없음.

## 반례·보류

- `CONTRADICTED`: 과거 정체가 확정되어야만 현재 관계 권리가 생긴다는 해석.
- `CONTRADICTED`: ep350의 사적 정보·접근 확대가 마지막 장면에서 한 번만 열린 예외라는 이전 추적 가설.
- `SUPPORTED / boundary`: 신뢰는 반드시 협력·편입만으로 표현되지 않고, 이 관계에서는 상대에게 자신을 반대·저지할 권리를 인정하면서 정보 경계를 맡기는 방식으로도 작동한다.
- `HOLD`: ep350 이후 현재 관계 권리의 장기 지속 여부는 제공 source boundary 밖이다.
- 다른 REF-47 관계에서도 같은 메커니즘이 반복되는지는 미확인.

## 감사 결과

- content diff: BASE → `d5972066e80b7bc38d0cddc9be9a591d4b485157`, 정확히 의도한 9개 연구 파일만 변경.
- Source Scene 4건 모두 source ID / episode / line / normalized SHA로 재진입 가능.
- 일반 연구층에 실제 작품명·저자명·고유명·검색 가능한 원문 장문을 새로 복제하지 않음.
- observed chain을 recommended chain으로 승격하지 않음.
- 기존 파일을 보강할 수 있는 곳은 신규 레코드로 중복하지 않음.
- Schema v3 / 신규 TH / Macro / Micro 불필요.
- audit: `PASS`.

## 변경 파일

### content commit
- `works/REF-47/relationships/REL-REF47-0002.md`
- `works/REF-47/threads/TH-REF47-01.md`
- `works/REF-47/source_scenes/SOURCE-SCENES-REF47-0018-0021.md`
- `works/REF-47/source_registry/SOURCE-BRIDGE-REF47.md`
- `works/REF-47/indexes/relationships.md`
- `works/REF-47/indexes/threads.md`
- `works/REF-47/indexes/source_scenes.md`
- `works/REF-47/research_batches/BATCH-20260816-RIGHTS-FOLLOWUP.md`
- `works/REF-47/audits/AUD-20260816-RIGHTS-FOLLOWUP.md`

### seal 단계
- `works/REF-47/research_receipts/RCPT-20260816-2112-REF47-RIGHTS-FOLLOWUP.md`
- `indexes/recent_receipts.md`

## 다음 질문

REF-47 내부의 다른 관계에서 `상대를 내 편으로 편입하지 않고도 반대·거절·저지할 권리를 인정하는 신뢰`가 반복·변형되는가. 반복된다면 어떤 조건에서 정보 공개와 대립 권리가 함께 증가하는가.
