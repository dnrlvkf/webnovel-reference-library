# AUDIT-REF46-0024 · 공동체 대표권·정체 공개 전제 감사

- work_id: `REF-46`
- identity_exposure: `sealed`
- audit_type: `premise_correction / pre_merge`
- mode: `작품 전체 왕복 채굴`
- question: `후반 실제 정체 공개 뒤 공동체 A의 대표권이 유지되는가.`
- base_sha: `84ab9fad97a3eaff85897f25f6cb245261225dbf`
- source_id: `SRC-LEGACY-REF46`
- source_boundary: `1~917화 / exact`
- source_sha256: `9cf9d175c228c02e960a04f3d721f29bb4362b380065f2fd200b828291ba1191`
- status: `passed_pre_merge`

## 표준 잠금

- manifest canonical branch: `main`.
- SOP: `REFERENCE_RESEARCH_ANALYSIS_SOP_v7.1.md` / SHA·size lock match.
- repository contract: `REFERENCE_RESEARCH_REPOSITORY_CONTRACT_v1.md` / SHA·size lock match.
- work-model schema: `REFERENCE_WORK_MODEL_SCHEMA_v2.md` / SHA·size lock match.
- source bridge: `VERIFIED_MATCH`.

## 감사 대상 전제

기존 `ORG-REF46-0001`, `TH-REF46-01`의 다음 질문은 `후반 정체 공개 뒤 대표권 인정 기준`을 전제로 했다.

이번 감사는 결론을 찾기 전에 다음을 순서대로 분리했다.

1. 외부 권력이 정체를 공표했는가.
2. 공동체가 그 공표를 실제 사실로 믿었는가.
3. 당사자의 실제 정체가 공동체에 직접 수신·검증됐는가.
4. 그 정보 때문에 구성원·대표 권리가 실제로 바뀌었는가.

## 원문 감사

### 434화

- 국가 권력이 주인공 A를 악령이라고 공표: `DIRECT`.
- 공동체 핵심 구성원이 그 공표를 사실로 채택하지 않음: `DIRECT`.
- 가정상 정말 악령이면 기존 반악령 규범이 적용된다는 판단 유지: `DIRECT`.
- 따라서 `국가 공표 = 공동체의 실제 정체 승인`: `CONTRADICTED`.

### 449~452화

- 공동체가 주인공 A를 기존 구성원·전사로 계속 취급: `DIRECT`.
- 대표 도전·수락·승부·승리·공개 승계: `DIRECT`.
- 대표권의 관찰된 공식 생성 사슬: `SUPPORTED`.
- 이 승계가 `실제 악령임을 알고도 허용한 것`: 근거 없음.

### 490·521화

- 개인 고백 시도는 수신 실패: `DIRECT`.
- 후속 시점에 핵심 공동체 구성원이 실제 악령 정체를 모름: `DIRECT`.
- `고백 발화 = 정보 공개 완료`: `CONTRADICTED`.

### 867·872화

- 대표가 악령화된 구성원을 공개적으로 살리는 것 자체가 조직 비용이 될 수 있어 비밀 처리를 선택: `DIRECT`.
- 공적 반악령 규범과 대표 개인의 비밀 판단이 분리됨: `SUPPORTED`.
- 실제 외부 영혼 정체 비공개 상태에서 대표·성인식·교육 권한은 계속 행사: `DIRECT`.

### 873~917화

- 공동체 대상으로 실제 외부 영혼 정체가 공개·검증·승인되는 관련 장면: `NOT_OBSERVED_WITHIN_SOURCE_BOUNDARY`.

## 핵심 판정

- `실제 정체 공개 뒤 대표권 유지`: **관찰되지 않음**.
- `실제 정체가 공동체에 공개됐는가`: **`NOT_OBSERVED_WITHIN_SOURCE_BOUNDARY`**.
- `실제 정체가 알려질 경우 대표권이 유지되는가`: **`HOLD / UNTESTED`**.
- `외부 공표 뒤에도 구성원·대표 권리가 유지됨`: `DIRECT`, 단 공동체가 공표를 믿지 않았기 때문.
- `대표권의 실제 공식 생성 기준`: `인정된 공동체 구성원 자격 + 공식 도전 수락 + 승리 + 공개 승계` — `DIRECT / SUPPORTED`.
- `강함·판단력·누적 행동`: 높은 사회적 지지를 보강하는 근거 — `SUPPORTED`.
- `누적 책임이 알려진 실제 악령 정체를 압도하는 최종 기준`: **사용 금지 / 미검증**.

## 여섯 트랙 감사

- CHARACTER: 새 독립 캐릭터 판정 필요 없음 — PASS.
- RELATIONSHIP: 공동체 전체의 미보유 정보를 기존 관계에 소급하지 않음 — PASS.
- EVENT: 대표 승계를 새 사건 파일로 중복 생성하지 않음 — PASS.
- STORY: 새 독립 STORY 없이 정보 상태 배열을 ORG/TH에서 보강 — PASS.
- PROSE: 저수준 실현 질문이 아니므로 PSE/PVAR 0 — PASS.
- TECHNIQUE: Source Scene 2, 기존 TH 2 보강, 신규 TH/Macro/Micro 0 — PASS.
- ORGANIZATION: 대표권 생성·정체 정보·공적 규범의 권리 구조를 `ORG-REF46-0001`에 통합 — PASS.

## 중복·익명성 감사

- 새 Source Scene은 기존 `SC-0029`의 행정 구조와 다른 질문을 해결함: PASS.
- 새 장면은 원문 문장 장기 복사 없이 회차·행·SHA·상태 변화만 보존: PASS.
- 실제 작품명·인물명·조직명·원천 파일명 노출 없음: PASS.
- `공표 / 수신 / 승인 / 권리 변화`를 하나로 뭉개지 않음: PASS.

## HOLD

- 실제 외부 영혼 정체를 공동체가 검증·수용한 뒤 대표권 유지 여부.
- 대표권을 도전 패배 외에 제한·회수하는 공식 조건.
- 정책 실패·지지 하락·외부 압력·내부 반대의 권리 회수 효과.

## 결론

기존 질문은 답을 얻은 것이 아니라 **질문의 전제가 틀렸음이 확인**됐다. source boundary 안에서 공동체 A는 주인공 A의 실제 외부 영혼 정체를 공인 정보로 획득하지 않는다. 따라서 대표권의 정당성을 `혈통 vs 영혼 vs 누적 책임`만으로 비교하지 않고, 직접 관찰된 **내부 구성원 인정 + 공식 도전·승계 절차**를 별도 제도 기준으로 추가한다.

다음 질문은 실제로 관찰 가능한 대표권의 회수 조건으로 이동한다.
