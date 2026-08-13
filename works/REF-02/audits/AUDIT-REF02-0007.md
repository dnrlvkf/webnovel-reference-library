# AUDIT-REF02-0007 · 51~60화 v6.1 pre-merge 감사

- work_id: `REF-02`
- mode: `구간 정밀 분석`
- source_scope: `SRC-COL2-027 / 51~60화 / 19453~23466행`
- base_sha: `61dbce24784e3bdc1082e99c820d1d66055bedd3`
- branch: `research/ref02-episodes-51-60-v61`
- identity_exposure: `sealed`
- standard: `REFERENCE_RESEARCH_ANALYSIS_SOP_v6.1.md`
- result: `passed_pre_merge`

## 정본·표준 감사

- `REPOSITORY_MANIFEST.yaml` canonical branch: `main`
- manifest schema: `1.4`
- SOP: `REFERENCE_RESEARCH_ANALYSIS_SOP_v6.1.md`
- repository contract: `REFERENCE_RESEARCH_REPOSITORY_CONTRACT_v1.md`
- work model schema: `REFERENCE_WORK_MODEL_SCHEMA_v1.md`
- project-source filename·SHA-256·byte size: lock와 일치
- contract addendum: `REFERENCE_RESEARCH_REPOSITORY_CONTRACT_v1.2_PROJECT_SOURCE_ADDENDUM.md`
- source whole SHA-256: `17b0f41b6b64eefe6f3d1354d22e2d75529be153b1f0f7fd71f00a016f96b766`
- source segment SHA-256: `14459ef08a6bc5126a3b2d7daf4d059c05ff0959cea06b8fda02047b0747defd`

## 변경 범위 감사

pre-audit compare 시점:

- branch ahead: 16 commits
- changed files: 16
- branch behind base: 0
- 기존 파일 수정:
  - `registry/source_inventory.yaml`
  - `CHR-REF02-0001`
  - `TH-REF02-CHR-06`
  - `TH-REF02-TEC-05`
- 신규 파일:
  - 원천 장면 1
  - 연구 배치 1
  - 관계 1
  - 조직 2
  - 사건 1
  - 스토리 1
  - 문체 1
  - Payoff 1
  - Macro 1
  - TH 2

감사 파일·영수증·인덱스는 이 감사 이후 추가한다.

## ID·경로 감사

신규 경로는 기존 `main`에 존재하지 않는 경로로 생성되었으며, 파일 ID와 파일명이 일치한다.

- `REL-REF02-0004`
- `ORG-REF02-0003`
- `ORG-REF02-0004`
- `EVT-REF02-0004`
- `STY-REF02-0004`
- `PRO-REF02-0004`
- `PAY-REF02-0001`
- `MAC-REF02-0002`
- `TH-REF02-REL-06`
- `TH-REF02-TEC-06`

기존 `TH-REF02-TEC-05`는 신규 생성하지 않고 같은 질문의 후속 근거를 보강해 `VERIFIED_THREAD`로 승격했다.

## 여섯 트랙 연결 감사

### CHARACTER

성격 형용사보다 다음 판단 변화가 기록되어 있다.

- 새 도구를 기존 탐색 경험과 연결해 기능 확장
- 소비 보상보다 생산 자산 선호
- 실제 기여와 명시 계약을 별도 판정
- 불특정 협업 거부와 검증된 동료 선택을 구분
- 생산 제약을 적 전략 예측에 사용
- 타인의 호의적 성격 판정을 객관 사실과 분리

### RELATIONSHIP

관계 변화는 친밀도보다 권리·의무·행동으로 기록했다.

- 직접 동료 선택권
- 역할 분담
- 비밀을 캐묻지 않을 권리
- 상호 구조 행동
- 동료 측 관계 욕망과 미성립 상호 복수 의무의 구분
- 동맹 외부 고용자의 이탈권
- 작전 자율권

### EVENT

사건을 줄거리 목록이 아니라 인과로 연결했다.

생산 시설 반복 파괴
→ 적 생산량 감소
→ 장기전 시한 발생
→ 적 수뇌부의 결전 전환
→ 외부 산 유인
→ 독진 중추 파괴
→ 지상전 우세
→ 수장전 패배와 합격진 회수

### STORY

- 첫 생산 시설 습격은 장면화, 반복 습격은 압축
- 반복 결과는 적 수뇌부 회의의 전략 변화로 확대
- 57화 관계 욕망은 주인공 부재 POV에서 독자에게만 공개
- 60화 초반 암살의 목적은 합격진이 실제 필요해진 순간까지 지연
- 화말은 완성된 역전 계획이 아니라 새 술식 연구 질문으로 닫음

### PROSE

v6.1 정보 접근권을 분리했다.

- 57화: 동료 관계 욕망은 독자만 알고 주인공 A는 모름
- 58화: 상위자 A의 냉정함 판정은 상대 해석이며 객관 사실 아님
- 60화: 적의 인물 분석 대사가 주인공 A의 다음 창안 입력으로 전환

판단 → 반응 채널 → 실제 표현 위치 → 상대/독자 해석 → 상태 변화 연결을 기록했다.

### TECHNIQUE

- `TH-REF02-TEC-05`: 별도 조직전 반복으로 `VERIFIED_THREAD` 승격
- `TH-REF02-REL-06`: 임시 협업 → 직접 선택 → 실제 상호 보완 → 구조의 반복·비용 확인
- `TH-REF02-TEC-06`: 첫 육사독 비용 → 자료 수집·실험 → 다른 육사독의 대응 준비 실전 검증
- `MAC-REF02-0002`: 주인공 부재 POV의 관계 욕망과 실제 구조 행동을 재독하기 위한 독립 Macro
- 신규 Micro: 없음. 한 발화보다 POV·위기·구조 전체 배열이 핵심이므로 억제함

## 반례·비용 감사

- 동료가 없었다면 독포자 대응이 어려웠던 실제 실패 조건을 기록함.
- 생산망 파괴가 적의 결전을 앞당긴 비용을 미완으로 보존함.
- 중추 파괴가 지상전 우세를 만들었어도 수장전 패배로 전체 승리를 보장하지 못한 반례를 기록함.
- 육사독 대응 재료 자체의 정상 정기 손상 비용을 기록함.
- 동료의 복수 의향을 상호 약속으로 과대 승격하지 않음.
- 60화 말 새 술식 성공 여부를 미확인으로 유지함.

## 익명성 감사

일반 연구층의 신규·수정 파일은 작품·인물·조직·기술의 실제 고유명을 사용하지 않고 `REF/SRC 코드 + 기능명`으로 기록했다.

실제 신원은 봉인 레지스트리에만 존재하며 연구 본문·커밋 메시지·PR 제목에 복사하지 않는다.

## Macro·Micro 감사

`MAC-REF02-0002`는 기존 `MAC-REF02-0001`과 다른 연구 문제를 가진다.

- 0001: 상대 내면을 열지 않고 거래 언어로 감정 협상
- 0002: 상대 내면을 열되 주인공에게는 차단해 독자 우위 관계 욕망을 만듦

57화는 특정 문장 하나보다 전체 POV 배열이 핵심이므로 Micro를 만들지 않았다.

## 표면 작업 퇴행 감사

1. 원문 재독 이유: 각 원천 장면·Macro에 있음.
2. 장면 표현 외 새 근거: 생산망 인과, 동료 권리 변화, 조직 사람 분류, 장기 Payoff가 있음.
3. 변형·실패·반례: 동료 보완, 결전 조기화, 지상전 우세/수장전 패배, 독 대응 비용이 있음.
4. 향후 검색 상황: Macro/TH에 명시함.
5. 원문 범위: 대사 순서·POV·장면 종료를 재관찰할 회차 전체 좌표를 보존함.

중단 조건 없음.

## 커밋 전 조건

- PR 생성 직전 `main` HEAD를 다시 확인한다.
- BASE SHA와 달라졌으면 `registry/source_inventory.yaml`, `works/REF-02/**`, 전역 인덱스의 중첩 변경을 다시 읽는다.
- 충돌이 없을 때만 병합한다.
- 병합 뒤 post-merge audit와 영수증 FINAL SHA를 별도로 봉인한다.
