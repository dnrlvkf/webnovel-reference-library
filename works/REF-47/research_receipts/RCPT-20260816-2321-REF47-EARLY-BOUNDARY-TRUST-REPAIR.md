# REF-47 연구 영수증

- receipt_id: `RCPT-20260816-2321-REF47-EARLY-BOUNDARY-TRUST-REPAIR`
- date_time: `2026-08-16T23:21:00+09:00`
- researcher: `ChatGPT`
- work_id: `REF-47`
- research_mode: `작품 전체 왕복 채굴 / 초반 회차 경계 검증 + 신뢰 실패 복구 방식`
- question: `2-166화 경계를 직접 검증한 뒤 protagonist-side 역할 최고 기준 오독을 찾고, 실패 뒤 판단권·정보·책임·역할이 어떻게 조정되는지 비교한다.`
- source_scope: `SRC-DIRECT-001 / ep1-166 boundary verification + ep78,124,132,163 full/selected reread + existing TH-02 comparison scenes`
- base_sha: `a5e0b288fb5f01a7d3a3b3543ca7d26cfa59afdf`
- content_commit_sha: `143411edf64cea71a9a9dc149f0bef4221bc902d`
- final_sha_mode: `self_excluding_receipt_finalization`
- status: `complete_with_housekeeping_hold`

## 표준·원문

- SOP v7.1: SHA `3803ff35ff9d68211aa2ab655b76dd387567f441a424f41e2a8e5884722fe8c5`, bytes `120486` — lock match.
- contract v1: SHA `8a6479621af6d1196433ca5760ae727eb5ccc1b876dea468df3faafc964e304e`, bytes `12579` — lock match.
- schema v2: SHA `1e6f5188749130900349cc7f54a9c07f888946d912485124fe45c7b4f50563f8`, bytes `19277` — lock match.
- source: SHA `95d22f155d582ec702142b906161f4b36241627a76cdf858ff9b39cd6d686a4e`, bytes `5927798`, UTF-16 — match.

## 회차 경계 검증

- ep1-166 연속 경계 `166`건 직접 검증.
- ep166 종료 `92261`, 다음 line `92262` explicit ep167 header 확인.
- 비표준 경계 ep25/62/68/157/158 직접 포함.
- boundary core SHA `58d92a04b52dc661e4bbc8d7f4567280cf770976c58a47e8b916d9feb874ff52`.
- boundary fullmap SHA `4b707c2c1ee217c280529a258eee15ba8668a0510839c9459da2e24b1a7303d2`.
- source bridge 상태를 `ep1-350 directly verified / verified_all_claimed_scope`로 승격.

## Source Scene

- `SC-REF47-0034`: ep78 `42571-42661` / `00de1a8858d2d6f389d321a423f02b9c0456a237e29e48050c2e8216dc57d098` — 불확실성 인지 상태의 신뢰·승격.
- `SC-REF47-0035`: ep124 `70335-70419` / `b01193dc27cfb539fb84fe9e72a529893315a8809625e29c8223b8303ef7696b` — 역할 유지 + 국소 규율.
- `SC-REF47-0036`: ep132 `74159-74189` / `186095f3aaa4cc31eec82a355c36ba3d9f0999d5828dfc76f575d573cd758f85` — 잘못·배신과 제자 역할의 후속 병존.
- `SC-REF47-0037`: ep163 `90358-90460` / `4d27487d83c8ed2f754ba8114d3b5a3cd2c4ea1e5ad64135a496b1e98bbcf7c4` — 감정/관계 상태 오독 경계.

## 여섯 트랙

### CHARACTER
- 신규 CHR 없음.
- protagonist-side 오독을 `감정/관계 상태`와 `역할 최고 기준 위임`으로 분리.
- 불확실성을 알고 제한 권리를 주는 판단을 확인.

### RELATIONSHIP
- `REL-REF47-0004`를 ep124/132까지 확장.
- 실패·이탈 뒤 `제자 역할·지원 유지 + 실제 의무 위반 국소 규율`을 장기 관계 구조로 보강.

### EVENT
- 신규 EVT 없음.
- ep124 이탈 준비→지원 확인→통상 벌점, ep163 감정 판정→제3자 정정을 Source Scene 상태 변화로 보존.

### STORY
- ep78 불확실성 공개→신뢰·승격.
- ep124→132 잘못/배신과 역할 유지의 장기 압축 회수.
- ep163 자기 관계 판정→제3자 착각 지적.

### PROSE
- 신규 PSE/PVAR 없음. 핵심은 표면 문구보다 권리·규율·정보 경계의 장면 결과.

### TECHNIQUE
- `TH-REF47-02` 보강.
- 복구 규칙: `실패 감지 → 실패한 층 식별 → 영향받지 않은 권리 유지 → 국소 규율/정보 조정/책임 추가/현재 판단 반박 → 후속 재검증`.

## 판정 변화

- `DIRECT`: protagonist-side 감정/관계 상태 오독 ep163.
- `HOLD / narrowed negative`: protagonist-side `역할 최고 기준 오독→판단권 오배분→직접 수정`은 1-350에서 미확인.
- `CONTRADICTED`: 후속 숨은 정체 공개만으로 과거 신뢰를 자동 오독으로 소급하는 해석. ep78은 불확실성을 이미 알고 있었다.
- `SUPPORTED`: 현재 TH-02 검증군에서는 실패 뒤 관계 전체 즉시 철회보다 실패한 층의 국소 조정이 반복된다.
- `HOLD`: 판단권 전면 회수가 독립 반복 메커니즘인지 미확인.

## 생성·수정

생성:
- `works/REF-47/source_registry/EPISODE-BOUNDARIES-REF47-0001-0166.md`
- `works/REF-47/source_scenes/SOURCE-SCENES-REF47-0034-0037.md`
- `works/REF-47/research_batches/BATCH-20260816-EARLY-BOUNDARY-TRUST-REPAIR.md`
- `works/REF-47/audits/AUD-20260816-EARLY-BOUNDARY-TRUST-REPAIR.md`
- 본 영수증.

수정:
- `works/REF-47/source_registry/SOURCE-BRIDGE-REF47.md`
- `works/REF-47/threads/TH-REF47-02.md`
- `works/REF-47/relationships/REL-REF47-0004.md`
- `works/REF-47/indexes/threads.md`
- `works/REF-47/indexes/relationships.md`
- `works/REF-47/indexes/source_scenes.md`
- `indexes/recent_receipts.md` (seal 단계)

신규 Macro/Micro/PSE/PVAR/CHR/EVT/STORY 파일 없음.

## QA

- BASE→content: ahead_by 1, 정확히 의도한 10개 research/source-registry 파일만 변경.
- Source Scene 4건은 해결 질문이 서로 달라 중복 아님.
- 신규 TH 없음; 기존 TH-02로 손실 없이 수용.
- source boundary registry와 source bridge 연결 확인.

## 운영 housekeeping HOLD

- 도구 연결 점검 중 비정본 임시 refs `__ignore_tmp`, `__ignore_tmp2`가 BASE SHA를 가리키도록 생성되었다.
- canonical `main` 내용에는 영향이 없고 연구 diff에도 포함되지 않는다.
- 현재 GitHub connector에는 branch delete action이 노출되지 않고 로컬 환경의 `gh`도 없어 이 실행에서 삭제하지 못했다.
- 이를 숨기지 않고 housekeeping HOLD로 기록한다. 이후 삭제 가능한 GitHub ref 도구가 제공되면 두 refs만 삭제해야 한다.

## 다음 질문

국소 조정이 실패해 실제 역할 권리 전면 회수로 넘어가는 임계 조건, 특히 `역할 최고 기준 자체의 이탈`이 `현재 방법 실패`와 어떻게 구분되는지 추적한다.
