# AUDIT-REF02-0001 · 필수 정본 문서 누락과 21~30화 HOLD 감사

- work_id: `REF-02`
- date_time: `2026-08-06T18:54:00+09:00`
- mode: `repository prerequisite audit + precision batch audit`
- base_sha: `2c7c78f567e8bbdfd00141367696d8d729cab4d8`
- branch: `research/ref02-episodes-21-30-hold`
- status: `HOLD_STANDARD_RESTORE`

## 발견한 정본 결함

`REPOSITORY_MANIFEST.yaml`은 다음 세 경로를 필수 연구 표준으로 지정한다.

- `REFERENCE_RESEARCH_ANALYSIS_SOP_v6.md`
- `REFERENCE_RESEARCH_REPOSITORY_CONTRACT_v1.md`
- `REFERENCE_WORK_MODEL_SCHEMA_v1.md`

세 파일 모두 현재 `main`에서 404로 확인됐다. 매니페스트와 실제 저장소 상태가 불일치한다.

## 확인한 로컬 승인본

이전 프로젝트 작업에서 생성된 로컬 산출물을 직접 읽고 체크섬을 확인했다.

| 문서 | 로컬 SHA-256 | 행 수 |
|---|---|---:|
| SOP v6 | `d83c28d809fcad738e134282af4ffe8f4d668cde40a65d1ac83fd457e667bd9b` | 1864 |
| repository contract v1 | `8a6479621af6d1196433ca5760ae727eb5ccc1b876dea468df3faafc964e304e` | 424 |
| work model schema v1 | `825324e6b2e4d3cdafce6decf1919c80aac1d9d59863c237960d49be64f79121` | 616 |

로컬 문서에서 작업 시작·BASE SHA·여섯 트랙·원천 장면·TH 상태·근거 판정·diff 감사·FINAL SHA·연구 영수증 규칙을 직접 확인했다.

## 원문 감사

- source: `SRC-COL2-027`
- sealed identity map: 확인
- source whole-file SHA-256: `17b0f41b6b64eefe6f3d1354d22e2d75529be153b1f0f7fd71f00a016f96b766`
- range: `21~30화 / 7163~11202행`
- segment SHA-256: `22fb54aec4da732d1268161d18ef22a861e39130ccf11cf096e97ae6861e403a`
- episode boundaries: 21~30화 연속 exact
- direct reading: 완료

## 21~30화 연구 품질 감사

### CHARACTER

성격 형용사가 아니라 비상 능력 사용 조건, 상대 욕망 이용, 회복 시간, 전리품 기능 재배치, 보호 통제 기준을 기록했다.

### RELATIONSHIP

호감도가 아니라 거주권·정보 접근권·방법 비공개권·시설 사용권·보호 통제권·자원 소유권 변화를 기록했다.

### EVENT

상위 적 제거, 비경 자원 회수, 보물 탈취, 연단 인프라 획득, 마도 비경 잠입을 발생 조건·촉발 선택·결과·비용·새 선택지로 분리했다.

### STORY

승리 뒤 정산, 생활 관계, 다음 위험의 교차 배열과 화말의 시험 조건을 기록했다.

### PROSE

상대 시점, 관찰 정보층, 설명 위치, 감정 체류, 기술 발동 리듬의 조건부 운용을 기록했다.

### TECHNIQUE

기존 TH 3건을 보강하고 `TH-REF02-TEC-02` 승격 후보와 `TH-REF02-EVT-03` 신규 스레드를 준비했다.

## ID·링크 감사

- 신규 원천 장면: `SC-REF02-0013~0022`
- 신규 작품 모델: `REL-REF02-0001`, `EVT-REF02-0001`, `STY-REF02-0001`
- 신규 TH: `TH-REF02-EVT-03`
- 기존 파일 보강: `CHR-REF02-0001`, `PRO-REF02-0001`, `TH-REF02-CHR-02`, `TH-REF02-REL-04`, `TH-REF02-TEC-02`
- 신규 배치: `BATCH-REF02-0003`
- 중복 신규 ID: 현재 변경 내 없음
- 원천 장면 범위 중복: 기능상 겹치는 연속 구간은 있으나 각 장면의 연구 질문과 상태 변화가 구분됨
- 실제 작품명·인물명·조직명·기술명 노출: 일반 연구층 변경에서 없음

## HOLD 판정

연구 내용 자체는 원문과 검증된 로컬 표준을 기준으로 준비했지만, 정본 필수 문서 3종이 매니페스트 경로에 없으므로 다음을 금지한다.

- PR의 `main` 병합
- 1~30화를 정본 완료 범위로 보고
- 연구 내용 SHA 또는 FINAL SHA를 완료 값으로 기록
- 31화 이후 정본 연속 작업 시작

## HOLD 해제 조건

1. 필수 문서 3종이 매니페스트 경로에 커밋되어야 한다.
2. 복구 문서의 내용 또는 승인 체크섬을 확인해야 한다.
3. 복구 이후 `main` HEAD를 새 BASE SHA로 기록해야 한다.
4. 이 브랜치를 최신 `main`과 비교하고 충돌·스키마·익명성을 재감사해야 한다.
5. 통과 후에만 병합하고 영수증 상태를 `complete`로 변경한다.
