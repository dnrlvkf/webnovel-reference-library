# RCPT-20260816-2331-REF47-FULL-REVOCATION-THRESHOLD

- work_id: `REF-47`
- research_mode: `작품 전체 왕복 채굴 / 역할 권리 전면 회수 경계`
- research_question: `국소 조정으로 유지되던 관계가 어떤 행동 증거에서 실제 역할 권리 전면 회수로 넘어가며, 현재 판단의 오류와 역할 계속 성립 가능성의 붕괴를 어떻게 구분하는가.`
- base_sha: `93793406195e7931d10898d3c18cb31303a5aabc`
- content_commit_sha: `c7af4a5b04accf9e80cc5e5c92e7cb83b910555e`
- final_sha_mode: `self_excluding_receipt_finalization`
- status: `complete_with_housekeeping_hold`
- source_id: `SRC-DIRECT-001`
- source_scope: `1-350 reverse search + ep264,266,285-286,299-300,302,324,330,339 selected/full reread + existing TH-02 comparison scenes`
- source_sha256: `95d22f155d582ec702142b906161f4b36241627a76cdf858ff9b39cd6d686a4e`
- source_bytes: `5927798`
- source_encoding: `UTF-16`

## 조회한 기록

- `REPOSITORY_MANIFEST.yaml`
- `REFERENCE_RESEARCH_STANDARD_SOURCE_LOCK_v1.yaml`
- Project Source `REFERENCE_RESEARCH_ANALYSIS_SOP_v7.1.md`
- Project Source `REFERENCE_RESEARCH_REPOSITORY_CONTRACT_v1.md`
- Project Source `REFERENCE_WORK_MODEL_SCHEMA_v2.md`
- `works/REF-47/README.md`
- `works/REF-47/source_registry/SOURCE-BRIDGE-REF47.md`
- `works/REF-47/indexes/source_scenes.md`
- `works/REF-47/indexes/threads.md`
- `works/REF-47/threads/TH-REF47-02.md`
- 기존 `SC-REF47-0022~0037` 비교 장면
- 최근 영수증 `RCPT-20260816-2321-REF47-EARLY-BOUNDARY-TRUST-REPAIR`

## 원문 확인

- ep1-350 episode boundary가 직접 검증된 상태를 확인하고 신규 대상 회차를 재독했다.
- 신규 Source Scene:
  - `SC-REF47-0038`: ep285-286 / lines 151581-151831 / `405f35ca481aa63c3f2d718473d75f9d58c69097d5447480b24fd9ef90ce21e0`
  - `SC-REF47-0039`: ep299-300 / lines 159657-159935 / `6defa601994bb99d97c382fb66ca6a015e50738d61454f45d1c532b87e0060d3`
  - `SC-REF47-0040`: ep302 / lines 161269-161341 / `a3f229d6a4b5afbc0e4846e2e3783b8974ce8a58fab11fcfec02b9d6ac502dcc`
  - `SC-REF47-0041`: ep324 / lines 173119-173557 / `d667131e44d95706f2b6d2084c8c81e2c170be9881e28ea32741f416dce536b9`
  - `SC-REF47-0042`: ep264 / lines 140773-140799 / `e379c148b70d8721983f13099261590396d273956859c8e617f31c9bced7cdcc`
- 추가 추적:
  - ep266 공식 관계 종료 후속 / lines 142117-142131 / `720c4bbb36324589a04e934ad45809184817680b83bf47b0d85b650d9d441aa2`
  - ep330 기관 이론 공격·등위 격하 검토 / lines 176035-176047 / `9dd819ed2393217c28b11613af98e9ec91c0296f580e913d30ee24fcb548831a`
  - ep339 기관 말살 대상 재분류 / lines 180299-180339 / `146351e6c35e1901fa709904f736c5bf9092a94a55e17fb2102ad758e10bcf55`

## 작품 모델 갱신

### CHARACTER
- 별도 CHR 파일은 만들지 않았다.
- 국소 실패에는 역할을 남기되, 관계 유지 자체가 상대에게 해롭다고 판단하면 애정과 역할을 분리해 역할을 종료하는 선택을 확인했다.
- 기관 충돌에서는 자기 지위의 권위 원천을 기관에 두지 않는 판단이 관계 붕괴의 촉발 선택으로 작동한다.

### RELATIONSHIP
- 별도 REL 파일은 만들지 않았다.
- 권리 상태를 `유지 / 정지+재심 / 직위 박탈+감금 / 공식 관계 종료 / 적대 재분류`로 분리했다.
- 역할 종료와 애정·보호 감정 종료를 분리했다.

### EVENT
- ep285-286: 파면 위협 → 비례성 논쟁 → 정직+재심.
- ep299-300→302: 권한 왜곡·은폐 → 파면+하옥.
- ep324→330→339: 권위 원천 부정 → 집행자 전멸 → 이론 공격/등위 격하 검토 → 말살 대상화.
- ep264→266: 관계 유지가 해롭다는 판단 → 파혼 선언 → 공식 관계 종료·호칭 변화.

### STORY
- 파면이라는 최고 위협과 실제 징계 판정을 회차 경계로 분리한다.
- 역할 위반 행동을 장면화한 뒤 행정 처분을 시간 압축으로 회수한다.
- 기관 관계 붕괴를 학술·등위·군사 비용으로 장기 회수한다.
- 관계 종료 직후 남은 애정을 배치해 `역할 종료=감정 종료` 오독을 차단한다.

### PROSE
- 신규 PRO/PSE/PVAR 없음.
- 결정적 근거는 표면 단어가 아니라 징계 선택지·행동 결과·권리 상태 변화의 배열이다.

### TECHNIQUE
- `TH-REF47-02`를 기존 신뢰·실패·국소 복구 스레드에서 `역할 계속 성립 가능성`까지 포괄하도록 보강했다.
- 신규 `SC-REF47-0038~0042`를 생성했다.
- 신규 TH/Macro/Micro 없음.

## 핵심 판정

- `SUPPORTED`: 국소 조정과 전면 회수의 상위 판별축은 결과의 심각도 하나가 아니라 **그 역할을 계속 인정하는 것이 아직 성립 가능한가**다.
- `SUPPORTED`: 특정 선택·방법·정보 채널·의무 위반처럼 실패 층이 국소적이고 동일 역할 수행 가능성이 남으면 정직/재심·벌점·정보 제한·책임 추가로 조정할 수 있다.
- `SUPPORTED`: 공적 권한이 역할 목적의 반대로 쓰이고 은폐까지 필요해지면 실제 파면+하옥처럼 직위와 자유가 함께 회수될 수 있다.
- `SUPPORTED`: 기관과 구성원이 지위 권위의 원천을 상호 부정하고 집행 관계가 살상으로 바뀌면 공동체 내부 역할에서 적대 제거 대상으로 재분류될 수 있다.
- `CONTRADICTED`: 전면 역할 종료는 반드시 상대의 배신·불신·애정 소멸 때문에 발생한다. ep264-266은 애정·보호 감정을 유지한 채 약혼 역할만 종료한다.

## 생성·수정·폐기

### 생성
- `SC-REF47-0038`
- `SC-REF47-0039`
- `SC-REF47-0040`
- `SC-REF47-0041`
- `SC-REF47-0042`

### 수정
- `TH-REF47-02`: `역할 계속 성립 가능성`과 전면 권리 회수/종료 분기 추가.
- source bridge / Source Scene index / TH index 갱신.

### 생성하지 않음
- 신규 CHR / REL / EVT / STORY / PRO / PSE / PVAR / Macro / Micro / TH 없음.

## 반례·보류

- `CONTRADICTED`: `전면 역할 종료 = 신뢰/애정 소멸`.
- `HOLD`: 기관 A가 주인공 A의 에테르 등위 자체를 공식 박탈했다는 직접 문구. 등위 격하는 검토 단계까지만 DIRECT.
- `HOLD`: 주인공 A가 상대 역할 최고 기준을 잘못 읽어 판단권을 오배분하고 그 위임 자체를 직접 철회한 사례.
- `HOLD`: 전면 회수 뒤 과거와 동일한 역할로 재진입하는 복구 메커니즘.
- `BOUNDARY`: 기관의 배신·말살 판정은 기관 시점 관계 분류이며 작품의 객관적 도덕 판정이 아니다.
- `BOUNDARY`: ep285-286에서 주인공 A 개인은 파면 의견을 유지했다. 기관 최종 판정인 정직과 합치지 않는다.

## 변경 파일

content commit `c7af4a5b04accf9e80cc5e5c92e7cb83b910555e`:
1. `works/REF-47/source_scenes/SOURCE-SCENES-REF47-0038-0042.md` — added
2. `works/REF-47/threads/TH-REF47-02.md` — modified
3. `works/REF-47/source_registry/SOURCE-BRIDGE-REF47.md` — modified
4. `works/REF-47/indexes/source_scenes.md` — modified
5. `works/REF-47/indexes/threads.md` — modified
6. `works/REF-47/research_batches/BATCH-20260816-FULL-REVOCATION-THRESHOLD.md` — added
7. `works/REF-47/audits/AUD-20260816-FULL-REVOCATION-THRESHOLD.md` — added

receipt finalization sequence adds this receipt and updates `indexes/recent_receipts.md` only.

## 감사 결과

- PASS: 원문 identity/encoding/hash/bytes 재검증.
- PASS: 신규 Source Scene 5건 line range + normalized segment SHA 고정.
- PASS: 정직을 파면으로 과장하지 않음.
- PASS: 기관 적대 재분류를 formal rank revocation으로 과장하지 않음.
- PASS: 관계 역할 종료와 감정 종료를 분리함.
- PASS: 기존 TH-02 직접 후속이므로 신규 TH를 만들지 않음.
- PASS: 신규 Macro/Micro/PSE/PVAR를 기계적으로 만들지 않음.
- audit: `works/REF-47/audits/AUD-20260816-FULL-REVOCATION-THRESHOLD.md`
- batch: `works/REF-47/research_batches/BATCH-20260816-FULL-REVOCATION-THRESHOLD.md`

## 동시성·housekeeping

- content commit 직전 원격 `main`이 BASE SHA `93793406195e7931d10898d3c18cb31303a5aabc`와 동일함을 재확인했다.
- content commit 반영 후 원격 `main`이 `c7af4a5b04accf9e80cc5e5c92e7cb83b910555e`를 가리킴을 확인했다.
- 기존 비정본 임시 브랜치 `__ignore_tmp`, `__ignore_tmp2`는 과거 BASE를 가리키는 housekeeping HOLD 상태이며 이번 연구 diff와 `main`에는 영향이 없다. 현재 노출된 connector에는 ref 삭제 동작이 없어 삭제 완료로 보고하지 않는다.

## 다음 질문

1. 정직·일시 정지처럼 **복귀 가능성을 보존한 권리 회수**는 실제로 어떤 행동 증거를 요구해 해제되는가.
2. 전면 회수·공식 관계 종료 뒤 다른 역할로 재진입한다면, 그것은 과거 역할 복원인가 새 관계 생성인가.
