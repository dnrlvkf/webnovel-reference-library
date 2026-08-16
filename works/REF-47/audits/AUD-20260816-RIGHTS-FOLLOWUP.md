# AUD-20260816-RIGHTS-FOLLOWUP

## 범위

- work: `REF-47`
- mode: `작품 전체 왕복 채굴 / 현재 관계 권리 후속 검증`
- BASE SHA: `3be2f1a406c3cdf3425494f4b6ee2f1872679d98`
- source: `SRC-DIRECT-001`
- full reread: ep332, ep335, ep339, ep350

## 정본·원문 검증

- canonical branch `main` / BASE HEAD 직접 확인.
- 현행 Project Source SOP v7.1 / Repository Contract v1 / Work Model Schema v2 기준 적용.
- raw source identity: SHA-256 `95d22f155d582ec702142b906161f4b36241627a76cdf858ff9b39cd6d686a4e`, bytes `5927798`, UTF-16.
- 대상 회차는 verified 167-350 header 범위 안에서 시작/다음 header 또는 EOF를 다시 확인.
- full-episode normalized SHA 재현: ep332 `fd57213d...13a0`, ep335 `dddedf86...24a40`, ep339 `a96e006b...765a6`, ep350 `40a14817...2701`.
- 신규 Source Scene segment SHA 4건 재현.

## 여섯 트랙 품질 감사

- CHARACTER: 성격 형용사가 아니라 현재 동행자 A가 무엇을 공개/보류하고 어떤 역할은 실제 수행하는지 행동 기준으로 기록. 신규 장기 CHR 강제 생성 없음. `PASS`.
- RELATIONSHIP: 호감 변화가 아니라 접근권·정보 공개권·대립/저지권·감시 채널·비밀 보존의 실제 권리 이동으로 기록. `PASS`.
- EVENT: ep332 위임 → ep335 행사 → ep339 경계 재설정 → ep350 확대의 상태 변경을 추적. 사건 연표 파일 중복 생성 없음. `PASS`.
- STORY: 정체 승인과 관계 권리 생성을 분리하고 후속 행동으로 독자 판정을 갱신하는 제시 순서를 기록. `PASS`.
- PROSE: 특정 문장 수집보다 공간 축소, 비공개 선택, 감시 장치 차단/복구, 제3자·기록 배제 같은 조건부 표현 결합을 Source Scene에서 보존. 기존 PSE/PVAR 재사용. `PASS`.
- TECHNIQUE: 기존 TH의 직접 후속 반복·변형으로 보강하며 신규 TH를 중복 생성하지 않음. `PASS`.

## 연결 사슬 감사

현재 동행자 A의 정체 주장과 주인공 A의 동일성 보류
→ ep332 현재 행동을 근거로 제한된 접근·정보·대립 역할 위임
→ ep335 대립 역할 실제 행사 + 사적 정보 비공개
→ ep339 외부 감시 적발 뒤 사적 질문/기한 정보 채널 유지
→ ep350 동일성 시험 실패에도 더 강한 사적 고백·기록 접근권 확대
→ 독자는 `과거 관계 복원`과 `현재 관계 권리 생성`을 별도 과정으로 판정.

- CHARACTER judgment → choice → EVENT → STORY presentation → PROSE/scene expression → reader reclassification → RELATIONSHIP rights change → next choice 사슬 복원. `PASS`.

## 반례·강등 감사

- `같은 이름/정체면 과거 관계 권리가 자동 복원된다`: 기존 `CONTRADICTED` 유지.
- `현재 관계 권리는 정체 확정 뒤에만 생긴다`: ep332-339 근거로 `CONTRADICTED`.
- `ep350 사적 공개는 마지막 장면 일회성 예외다`: ep332/335/339 후속 사슬로 `CONTRADICTED`.
- `신뢰는 반드시 상대를 내 편으로 편입하는 형태다`: 현재 관계에서는 대립/저지권 인정과 비밀 보존이 병존하므로 충분조건으로 사용할 수 없음. 작품 전체 일반화는 하지 않음.
- ep350 이후 장기 지속: `HOLD`.

## Source Scene 저장 감사

- `SC-REF47-0018`: 현재 권리 생성이라는 독립 상태 변화가 있어 저장 적합.
- `SC-REF47-0019`: 위임된 권리의 실제 행사와 비밀 보존이라는 독립 검증이 있어 저장 적합.
- `SC-REF47-0020`: 감시 적발 뒤 정보 경계 재설정이라는 독립 변형이 있어 저장 적합.
- `SC-REF47-0021`: 선행 권리 누적의 확대 회수와 기록 이전이 있어 저장 적합.
- observed chain을 recommended chain으로 승격하지 않음. `PASS`.

## 저장 억제 감사

- 신규 Macro: `NO`. REL+TH+SC에서 독립 집필 검색 가치가 손실 없이 복원됨.
- 신규 Micro: `NO`. 특정 표현을 떼면 사라지는 핵심보다 장면 행동 사슬이 중요함.
- 신규 PSE/PVAR: `NO`. ep350은 기존 PSE/PVAR로 충분하고 ep332/335/339은 Source Scene 수준이 적합.
- 신규 CHR/EVT/STORY 파일: `NO`. 연결을 위해 파일 수를 늘리지 않음.

## 익명성·원문 재진입 감사

- 일반 연구 파일에 실제 작품명·저자명·고유 인물명·검색 가능한 원문 장문을 새로 저장하지 않음.
- 역할 슬롯, source ID, episode, lines, normalized SHA로 재진입 가능.
- Source Scene 4건과 source bridge 양방향 좌표를 함께 갱신. `PASS`.

## 판정

- `PASS`: 이전 미확인 질문은 제공 source 범위 안에서 `ep350 일회성 예외` 가설을 반증할 만큼 후속 근거가 확보됨.
- `PASS`: 현재 행동으로 생성된 관계 권리가 여러 회차에서 행사·유지·확대됨.
- `HOLD`: ep350 이후 장기 상태.
- Schema v3 / 신규 TH / Macro / Micro 불필요.
