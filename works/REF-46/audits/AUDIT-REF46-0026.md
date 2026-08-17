# AUDIT-REF46-0026 · 대표직 존속·실행 제약 pre-merge 감사

- work_id: `REF-46`
- identity_exposure: `sealed`
- audit_type: `rights_durability / pre_merge`
- mode: `작품 전체 왕복 채굴`
- question: `도전 패배 외 정책 실패·낮은 지지·외부 정치 압력·내부 반대가 대표권을 회수하는가.`
- base_sha: `889a6c60f06afb0e0030a955e168d42c9dce11c7`
- source_id: `SRC-LEGACY-REF46`
- source_boundary: `1~917화 / exact`
- source_sha256: `9cf9d175c228c02e960a04f3d721f29bb4362b380065f2fd200b828291ba1191`
- status: `passed_pre_merge`

## 표준·원천 잠금

- canonical branch: `main`.
- SOP: `REFERENCE_RESEARCH_ANALYSIS_SOP_v7.1.md` / Project Source lock match.
- repository contract: `REFERENCE_RESEARCH_REPOSITORY_CONTRACT_v1.md` / lock match.
- work-model schema: `REFERENCE_WORK_MODEL_SCHEMA_v2.md` / lock match.
- source bridge: `VERIFIED_MATCH`.
- local 1~917 source SHA/size: canonical source bridge와 일치.

## 원문 감사

### 452화
- 지지도 효과: 통솔력·반대 세력·정책 성공률·지시 수행률 — `DIRECT`.
- 공식 대표직의 직접 회수 경로로 도전 패배가 제시됨 — `DIRECT`.
- `지지 않는 한 내려갈 일이 없다`는 주인공 A의 제도 해석 — `DIRECT as character interpretation`.
- 후속 구간에서 이 해석을 깨는 자동 해임 사례: `NOT_OBSERVED_WITHIN_SOURCE_BOUNDARY`.

### 455화
- 새 성인식 정책과 전통 사이 내부 이견: `DIRECT`.
- 이견이 현 대표 결정을 즉시 무효화·해임하지 않음: `DIRECT`.
- 장기 변경 경로로 미래 대표 승계가 제시됨: `DIRECT`.
- 공식 투표·불신임 절차 존재: `HOLD`.

### 494~495화
- 내부 대표는 대규모 공동체 동원권과 높은 지지를 행사: `DIRECT`.
- 외부 전문 조직의 적법한 영역을 대표 직함만으로 자동 중단시킬 수 없음: `DIRECT`.
- 왕국 기관도 현장 권한 범위가 제한됨: `DIRECT`.
- 외부 관할 제약을 내부 대표직 회수로 볼 근거: 없음.

### 641화
- 다른 종족 대표·왕가 균형 논리가 정치 압력으로 작동: `DIRECT`.
- 다른 종족 대표가 공동체 A 대표의 상급자·내부 명령권자임: `CONTRADICTED BY SCENE`.
- 왕실이 `작위를 가진 종족 대표` 상태 자체를 이미 문제 삼지 않기로 함: `DIRECT`.

### 780~781화
- 집단 기대를 거절하면 지지도가 하락할 수 있다는 계산: `DIRECT`.
- 직위 상실이 예상 비용으로 제시됨: `NOT_OBSERVED`.
- 선택 조정의 직접 이유는 구성원의 정서 비용: `DIRECT`.

### 861~862화
- 약 한 달 칩거: `DIRECT`.
- 행정 담당자가 실무를 사실상 떠맡음: `DIRECT`.
- 전사 불안 누적: `DIRECT`.
- 자동 해임·재선임: `NOT_OBSERVED`.
- 직위를 가져가겠다는 표현 뒤 결투·도전 전통을 호출: `DIRECT`.
- 복귀 뒤 대표 호칭·업무 책임 지속: `DIRECT`.

### 896화와 873~917 후속
- 후반 내부 공간에서 대표 호칭 지속: `DIRECT`.
- 정책 실패·지지 하락·외부 압력·내부 반대에 의한 자동 대표직 해임 장면: `NOT_OBSERVED_WITHIN_SOURCE_BOUNDARY`.

## 여섯 트랙 감사

- CHARACTER: 신규 파일 필요 없음 — PASS.
- RELATIONSHIP: 정책 이견을 독립 관계 전환으로 과대승격하지 않음 — PASS.
- EVENT: 새 사건 ID보다 기존 권리 경계의 변형·반례로 처리 — PASS.
- STORY: 새 독립 STORY 없이 장기 배열을 TH/ORG에 연결 — PASS.
- PROSE: 저수준 산문 질문이 아니므로 PRO/PSE/PVAR 0 — PASS.
- TECHNIQUE: Source Scene 2, 기존 TH-REF46-01 보강, 신규 TH/Macro/Micro 0 — PASS.
- ORGANIZATION: 대표직 존속·실행 효율·실무 수행·외부 관할을 분리 — PASS.

## 중복·경계 감사

- `SC-REF46-0033`은 `SC-0029`의 행정 분화와 달리 지지도·부재·정책 이견이 **직위 회수인지 실행 비용인지**를 해결함 — PASS.
- `SC-REF46-0034`는 외부 법·정치 관할이 내부 대표권과 어떻게 다른지 해결함 — PASS.
- `TH-REF46-05`는 정체 정보 스레드이므로 이번 배치에서 미수정 — PASS.
- 신규 TH를 만들지 않고 `TH-REF46-01`의 제도 책임 경계 보강 — PASS.

## 핵심 판정

`정책 실패 / 낮은 지지 / 외부 정치 압력 / 내부 반대`는 모두 **대표직 자동 회수 조건으로 관찰되지 않는다**.

다만 이것은 `아무 비용도 없다`는 뜻이 아니다.
- 낮은 지지: 정책 성공률·지시 수행률·집단 정서 비용.
- 정책 문제: 위임·조정·실무 비용.
- 장기 부재: 실무 과부하·집단 불안.
- 외부 압력: 외부 사안의 관할·협상 제약.

직접 확인된 대표직 변경 언어는 계속 공식 도전·패배 쪽에 묶여 있다.

## HOLD

- 실제 외부 영혼 정체 승인 뒤 대표권 변화.
- 도전권자의 정확한 자격.
- 도전 수락 의무와 절차.
- 부재·무능·지지 하락이 실제 도전을 촉발하는지.
- 도전 외 공식 불신임·해임 절차.
- 917화 이후 제도 안정성.

## 결론

`passed_pre_merge`. 이번 배치는 대표권을 `강한 권력` 하나로 뭉개지 않고 **직위 존속 / 지지도와 정책 실행 / 실무 수행 / 외부 관할** 네 층으로 분리했다. 네 회수 후보는 자동 해임으로 닫히지 않았고, 다음 질문은 실제 직위 변경 통로인 `도전권`의 자격·촉발·강제성으로 이동한다.