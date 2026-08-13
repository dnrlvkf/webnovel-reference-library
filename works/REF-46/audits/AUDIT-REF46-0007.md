# AUDIT-REF46-0007 · 직접 지휘 실패 비용 pre-merge 감사

- work_id: `REF-46`
- official_mode: `작품 전체 왕복 채굴`
- source_boundary: `1~917화 / exact`
- source_sha256: `9cf9d175c228c02e960a04f3d721f29bb4362b380065f2fd200b828291ba1191`
- base_sha: `394a76ffd545d07cd54258a2c417f73034ceb98e`
- branch: `research/ref46-command-failure-cost`
- identity_exposure: `sealed`
- result: `passed_pre_merge`

## 질문 경계 감사

찾는 사례를 `자기 지휘 결정 → 결정 실패 → 부하/임무 비용 → 자기책임 연결 → 후속 지휘 수정`으로 한정했다.

- 상부 경고를 더 강하게 하지 못한 후회: 별도 `상향 설득 실패`.
- 다른 사령관의 명령 아래 발생한 사망: 현재 인물 실패에서 제외.
- 적의 예측 불가능한 공격 자체: 명령 오판과 분리.
- 단순 전투 패배·부상: 직접 지휘 실패로 세지 않음.

## 원문 감사

- 285화 임시 지휘: 다음 행동 결정 성공, 직접 실패 비용 없음.
- 354~355화 부단장 지휘: 철수·위임·후방 차단·퇴로 설계. 상향 경고 후회는 있으나 본인 명령 피해 아님.
- 360~364화: 장교 소집·수색 편성·대기 운영. 자기 명령 유발 사망 미확인.
- 391화: 병단 관리 공백 방지를 이유로 개인 합류 포기.
- 551~560화: 대규모 사망은 별도 사령관/부사령관 지휘 아래 발생.
- 710화 이후: 다른 책임자 아래 전문 팀원 역할.

판정: `직접 지휘 실패→교정 학습`은 `NOT_OBSERVED_WITHIN_SOURCE_BOUNDARY`.

## 여섯 트랙 감사

- CHARACTER: 책임 확대의 근거와 학습 원인을 분리함.
- RELATIONSHIP: 상부 보고/설득권과 부하 명령/위임권을 혼합하지 않음.
- EVENT: 손실 사건의 실제 지휘 귀속 보존.
- STORY: 보이지 않은 실패 아크를 추정 삽입하지 않음.
- PROSE: 후회문을 과도한 자기책임 고백으로 확장하지 않음.
- TECHNIQUE: 신규 TH/Macro/Micro 불필요.

## 기록 억제 감사

- 신규 Source Scene 0.
- 신규 TH 0.
- 신규 Macro 0.
- 신규 Micro 0.
- 기존 `CHR-REF46-0003` 보강 우선.

## 익명성 감사

- derived research에 실제 작품명·인물명·조직명·기술 고유명 없음.
- 원천 재진입은 REF·회차·source SHA로 가능.

## 중복·상태 감사

- 신규 ID는 배치·영수증·감사만 생성.
- 기존 캐릭터 질문과 중복되는 별도 CHARACTER/TH 생성 없음.
- `NOT_OBSERVED_WITHIN_SOURCE_BOUNDARY`는 `발생 불가능`으로 일반화하지 않음.

## merge 전 판정

`passed_pre_merge`.
