# AUDIT-REF46-0008 · 직접 지휘 실패 비용 post-merge 감사

- work_id: `REF-46`
- official_mode: `작품 전체 왕복 채굴`
- source_boundary: `1~917화 / exact`
- source_sha256: `9cf9d175c228c02e960a04f3d721f29bb4362b380065f2fd200b828291ba1191`
- base_sha: `394a76ffd545d07cd54258a2c417f73034ceb98e`
- pr: `#17`
- research_content_sha: `49e1a1fe262bc14b9ecd697d697403fe30ad8528`
- identity_exposure: `sealed`
- result: `passed_post_merge`

## 원격 병합

- PR #17 squash merge 성공.
- expected head SHA `a45bec5469b263b87499f4ea8824d5814e67946c` 고정.
- merge SHA: `49e1a1fe262bc14b9ecd697d697403fe30ad8528`.
- merge 직전 canonical main은 BASE SHA와 동일함을 재확인.

## canonical CHARACTER 감사

`CHR-REF46-0003` main 재확인.

- `책임 소유 범위 확대`: `SUPPORTED` 유지.
- `책임 확대가 직접 지휘 실패→교정 학습 때문에 형성됨`: `NOT_OBSERVED_WITHIN_SOURCE_BOUNDARY`.
- 355화 후회는 자기 하향 명령의 오판이 아니라 상부 경고·설득 강도 부족으로 분리됨.
- 551~560화의 대규모 손실은 별도 사령관/부사령관의 작전 지휘 결과로 보존됨.
- 미장면화된 2년 6개월 군 경험 안에 실패가 있었을 가능성을 사실로 채우지 않음.

## 권리 방향 감사

- 부하 대상: 명령·위임·철수 지시.
- 상부 대상: 보고·경고·설득.
- 같은 `책임`이라는 말로 두 권리 방향을 합치지 않음.
- 따라서 355화의 실패 유형을 `직접 지휘 실패`로 과대평가하지 않음.

## EVENT / STORY 감사

- 208 결정권 이전 → 285 임시 지휘 → 354~364 제도 지휘의 장기 배열은 유지.
- 원문에 없는 `명령 실패로 성장하는 중간 아크`를 삽입하지 않음.
- 대규모 탐사 손실의 인과 귀속을 실제 명령권자에게 유지.

## PROSE 감사

- 355화의 짧은 사후 후회문을 `내 명령 때문에 사람이 죽었다`는 직접 자기책임 고백으로 확장하지 않음.
- 실제 발화 기능과 장면 권리 구조를 함께 보존.

## TECHNIQUE / 기록 억제 감사

- 신규 Source Scene: 0.
- 신규 TH: 0.
- 신규 Macro: 0.
- 신규 Micro: 0.
- 기존 CHARACTER와 index 보강만으로 질문 해결 가능.

## 익명성·재진입 감사

- 일반 연구층에 실제 작품명·인물명·조직명·기술명 없음.
- REF·회차·source SHA로 재진입 가능.
- identity exposure: sealed.

## 완료 판정

이번 질문은 current source boundary 안에서 닫을 수 있다.

> `마법사 장교 A의 책임 확대가 자기 직접 지휘 실패와 교정 학습에서 나왔는가?`

판정: **그 완전 사슬은 `NOT_OBSERVED_WITHIN_SOURCE_BOUNDARY`**.

이는 `그런 실패가 발생 불가능하다`는 뜻이 아니라, 1~917화 정본 원문 안에서 그 인과를 확인할 수 없다는 뜻이다.

result: `passed_post_merge`.
