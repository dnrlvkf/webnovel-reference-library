# AUDIT-REF02-0009 · 61~120화 적응형 pre-merge 감사

- work_id: `REF-02`
- official_mode: `구간 정밀 분석`
- operating_unit: `적응형 대구간 순회`
- source_scope: `SRC-COL2-027 / 61~120화 / 23467~46482행`
- source_segment_sha256: `8bd5ce4d5867874d36b1470da79921a821294b51be0b899c678facb78693855c`
- base_sha: `47d3b856e348694cb9964a56058b3f6464fcb421`
- branch: `research/ref02-episodes-61-120-adaptive-v61`
- identity_exposure: `sealed`
- standard: `REFERENCE_RESEARCH_ANALYSIS_SOP_v6.1.md`
- result: `passed_pre_merge`

## 정본·표준 감사

- canonical branch: `main`
- manifest schema: `1.4`
- project-source SOP: `REFERENCE_RESEARCH_ANALYSIS_SOP_v6.1.md`
- repository contract: `REFERENCE_RESEARCH_REPOSITORY_CONTRACT_v1.md`
- work-model schema: `REFERENCE_WORK_MODEL_SCHEMA_v1.md`
- contract addendum: `REFERENCE_RESEARCH_REPOSITORY_CONTRACT_v1.2_PROJECT_SOURCE_ADDENDUM.md`
- standard lock filename·SHA-256·byte size: matched
- source whole SHA-256: `17b0f41b6b64eefe6f3d1354d22e2d75529be153b1f0f7fd71f00a016f96b766`
- source boundary: `1~284화 / exact`
- source 61~120 segment hash: matched local direct-read bytes

## 적응형 독해 범위 감사

61~120화 60개 회차 전체를 직접 읽었다. Source Scene을 회차 수에 맞춰 만들지 않고 변화 밀집 구간 10개로 압축했다.

- `SC-REF02-0053` — 61~65
- `SC-REF02-0054` — 66~72
- `SC-REF02-0055` — 73~83
- `SC-REF02-0056` — 84~89
- `SC-REF02-0057` — 90~94
- `SC-REF02-0058` — 95~100
- `SC-REF02-0059` — 101~107
- `SC-REF02-0060` — 108~113
- `SC-REF02-0061` — 114~116
- `SC-REF02-0062` — 117~120

각 구간은 원문 줄 범위와 SHA-256을 보존한다. 저변화 반복은 배치·작품 모델에서 압축했고 원문 독해 자체를 생략하지 않았다.

## 변경 범위 감사

compare 기준:

- branch ahead: `19 commits`
- branch behind base: `0`
- changed files: `18`

### 신규 연구 파일

- `SOURCE-SCENES-REF02-0053-0062.md`
- `BATCH-REF02-0007.md`
- `EVT-REF02-0005.md`
- `STY-REF02-0005.md`
- `PRO-REF02-0005.md`
- `TH-REF02-TEC-07.md`
- `PAY-REF02-0002.md`
- `MAC-REF02-0003.md`

### 기존 파일 보강

- `CHR-REF02-0001.md`
- `REL-REF02-0001.md`
- `REL-REF02-0004.md`
- `TH-REF02-CHR-02.md`
- `TH-REF02-CHR-06.md`
- `TH-REF02-REL-04.md`
- `TH-REF02-REL-06.md`
- `TH-REF02-TEC-02.md`
- `registry/source_inventory.yaml`
- `works/REF-02/indexes/research.md`

신규 조직 모델은 만들지 않았다. 조직 변화가 기존 작품 연구 질문을 넘어 독립 재독 단위가 되지 않아 사건·관계·스토리 모델에 흡수했다.

## 원천 레지스트리 오류 감사

브랜치에서 `registry/source_inventory.yaml`을 갱신하는 과정에 기존 9~10화 segment SHA가 잘못 입력된 중간 커밋이 한 번 발생했다.

- 잘못된 값은 같은 브랜치에서 즉시 발견함.
- 원래 정본 값 `0b375e2b59c23d4b0925b12b57c68780600d561f7dfb764390a5782acbd6320e`로 복구함.
- 현재 branch 파일을 다시 fetch해 기존 1~10화 값과 신규 61~120화 값이 모두 정확함을 확인함.
- 잘못된 중간 값은 `main`에 병합되지 않음.

따라서 최종 diff에는 기존 9~10화 체크섬 변화가 없다.

## CHARACTER 감사

성격 형용사 대신 경쟁 판단 기준과 반례를 갱신했다.

- 안전한 선택 vs 자기 성장 경로
- 대응책 있는 위험 수용 vs 자존심형 무모함
- 조직 외부 독립 vs 조직 자원의 제한적 이용
- 과거 지식의 관계 기대 vs 현재 당사자 선택
- 통합 욕망 vs 외부/별도 저장과 기능 분할
- 현재 선공 대기 vs 적대 근거·조건 능동 조립

기존 모델을 지우지 않고 1~120화 장기 지도에 누적했다.

## RELATIONSHIP 감사

호감도 대신 권리·비용 변화를 기록했다.

- 동업자 A: 비밀을 캐묻지 않을 권리, 각자 이동권, 미래 협업권
- 검증 동료 A·B: 재선택, 위험 역할 보수, 계약 외 성장 자원 투자, 독립 기술 소유권
- 우호 조직 A: 가입 없이 개인 비경·신물 접근권
- 관계 상대 C: 주인공 A가 원하지 않는 조직 전쟁을 만들지 않을 의사를 실제 행동으로 존중

`동료의 생명 단위 도움 의향 = 상호 무제한 의무`로 승격하지 않았다.

## EVENT 감사

줄거리 목록이 아니라 다음 상태 변경 사슬을 복원했다.

생산망 유격전 누적
→ 적 수장 약화
→ 상위 포식자 법보 회수
→ 외부 오행 저장
→ 위험 상계 유물/동업자 재결합
→ 원영 후기 행동시간 한계 확인
→ 상계 힘 별도 저장
→ 몸 수련 필요
→ 결단 자원 갈등 의도적 선택
→ 우호 조직 제한 계약
→ 극음·극양 자원 확보
→ 결단
→ 귀수성 이탈
→ 제도권 가짜 신분
→ 상위 조직의 역고용/초빙 유도

## STORY 감사

- 보상마다 새 사용 조건·결핍을 즉시 붙임.
- 82~83화: 비상 능력 실패처럼 보인 뒤 시간 조건으로 재판정.
- 101~104화: 실패 공격을 구조 진단으로 재판정.
- 105~107화: 적 조직 내부 과신/경고 POV 차이 → 현재 선택 확인.
- 117~120화: 후계자 → 부친/조직 → 주인공 계획의 3단 POV로 동일 접촉 의미 재분류.
- `PAY-REF02-0002`: 초기 깊은 체질 흔적이 106화에 장기 신원 부채로 회수됨.

## PROSE 감사

SOP v6.1의 정보 접근권·미시 연결 기준을 적용했다.

- 기술 지문은 위력보다 흐름·선행 기울기·순환·시간층을 본다.
- 관계 변화는 감정명보다 `묻지 않음·추가 지급·떠나게 둠·미래 약속` 행동으로 확인한다.
- 109~110화 결단은 넓은 개념 설명 → 가까운 죽음 감각 → 자기 선택 → 다시 세계 구조 통합으로 거리 변화.
- 117~120화 대사는 명령 거절→보수→즉시 지급→자유 욕망 자극이라는 행동 기능으로 기록했다.

## TECHNIQUE 감사

### 신규 `TH-REF02-TEC-07`

71~74, 80~81, 91~93, 101~104, 107, 119화에서 서로 다른 기술 계열에 `노출 → 구조 관찰 → 파훼 → 재현 → 개량 → 타 분야 합성`이 반복된다.

재현 직후 신체 손상, 현재 이해 범위를 넘는 상계 힘의 비재현 비용도 확인되어 `VERIFIED_THREAD`가 적절하다.

### 기존 TH 수정

- `TH-REF02-CHR-02`: `원영경 후기 이상 불가` 경지 고정 상한 하위 가설을 `CONTRADICTED`; 행동시간/대상 지정 접근성으로 수정.
- `TH-REF02-CHR-06`: `현재 장면에서 상대 선공 필수` 하위 가설을 `CONTRADICTED`; 현재 선택·과거 이력·조직 역할·능동적 조건 조립으로 범위 수정.
- `TH-REF02-TEC-02`: `활동 신원과 실제 신원 영구 분리` 해석을 106화 깊은 정보 재연결로 반박하고, 116~120화 제도권 가짜 신분 변형 추가.
- `TH-REF02-REL-04`, `TH-REF02-REL-06`: 소속 없는 깊은 접근권과 검증 동료 장기 투자 보강.

## Macro·Micro 감사

- `MAC-REF02-0003`: 105~107화의 `과거 지식상 구원 가능성 → 현재 선택 질문 → 현재 충성 선택 → 기억 기대 폐기 → 전투 학습`은 기존 Macro와 다른 독립 재독 문제를 가진다.
- 특정 한 발화보다 POV·선택·전투 전환 전체 배열이 핵심이므로 신규 Micro를 만들지 않았다.

## 중복·포화 감사

- 기존 TH로 흡수 가능한 근거는 신규 TH를 만들지 않고 보강했다.
- 신규 TH는 `TEC-07` 1건뿐이다.
- 신규 Source Scene 파일은 60화에 대해 1파일/10구간으로 압축했다.
- 60화 동안 신규 Macro 1, Payoff 1, Micro 0.
- 같은 메커니즘 반복만 있는 구간은 배치/기존 모델 좌표로 압축했다.

적응형 전환의 목적대로 파일 수를 회차 수와 분리했다.

## 익명성 감사

일반 연구층 신규·수정 파일은 실제 작품명·인물명·조직명·기술 고유명을 사용하지 않고 `REF/SRC + 역할/기능명`만 사용한다.

실제 식별자는 봉인 레지스트리와 원문에만 존재한다.

## 반례·HOLD 감사

- 원영경 후기 고정 상한: 하위 가설 `CONTRADICTED`.
- 현재 선공 필수: 하위 가설 `CONTRADICTED`.
- 영구 신원 분리: 106화로 `CONTRADICTED`.
- 동료 무제한 상호 의무: `HOLD`.
- 동업자 A의 감정적 특별성: `HOLD`.
- 상위 후계자 A의 자유 욕망을 장기 통제 가능한가: `HYPOTHESIS`.
- 가짜 신분 B의 내부 검증 통과: `HOLD`.

## 표면 작업 퇴행 감사

- 줄거리 요약만 하지 않았음: 여섯 트랙과 연결 사슬 존재.
- 캐릭터 성격표가 아님: 경쟁 기준·반례·복귀 조건 기록.
- 관계 호감도표가 아님: 질문권·비밀권·이동권·접근권·보수권 기록.
- 사건 연표가 아님: 발생 조건·촉발 선택·비용·후속 선택 연결.
- 문체 감상문이 아님: POV 정보권·지문 관찰 대상·대사 기능·서술 거리 조건 기록.
- Macro/Micro 남발 없음.
- 기존 판정을 보호하지 않고 후속 반례로 두 하위 가설을 명시적으로 무너뜨림.

## 커밋 전 조건

- PR 생성 직전 `main` HEAD를 다시 확인한다.
- BASE SHA와 달라졌으면 중첩 파일을 다시 읽고 충돌 여부를 검증한다.
- 변경 파일·원천 체크섬·링크·익명성 감사 통과 후에만 병합한다.
- 병합 뒤 `AUDIT-REF02-0010`, 영수증 확정, global recent receipts, FINAL SHA seal을 작성한다.
