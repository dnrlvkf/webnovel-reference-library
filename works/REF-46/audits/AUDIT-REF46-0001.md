# AUDIT-REF46-0001 · 병합 전 연구 감사

- work_id: `REF-46`
- date_time: `2026-08-08T23:42:00+09:00`
- mode: `traversal batch audit`
- base_sha: `7ae170db7dc0c8d379bc3b18ebac82e4ebe48eb3`
- branch: `research/ref46-20260808-character-prose-pov`
- audited_branch_sha: `d239b21e6e2ba10e33ab07a3199ccfa4f382ac18`
- status: `reviewed_on_branch`

## 표준·원문

- manifest canonical branch: `main`
- 승인 표준은 lock이 지정한 SOP v6 / repository contract v1 / work-model schema v1을 사용함.
- REF-46 boundary: `1~917화 / exact`
- source SHA-256: `9cf9d175c228c02e960a04f3d721f29bb4362b380065f2fd200b828291ba1191`
- 직접 재검증 10개 구간 combined SHA-256: `305f634dc2cc415413d7a1fbaf8652958c0545de95a60a30fbd1c9a323a0618b`

## diff

BASE 대비 receipt 생성 전 compare에서 branch는 `ahead`, `behind_by: 0`이었다. REF-46 연구층과 `registry/works.yaml`의 REF-46 등록만 변경했다.

## 여섯 트랙

- CHARACTER: `CHR-REF46-0001~0003`이 고정 성격표가 아니라 판단 기준·오판·override·복귀를 기록함.
- RELATIONSHIP: 신규 단독 파일 없음. 독립 장기 권리 질문이 확인되기 전 파일 수를 늘리지 않음.
- EVENT: 신규 단독 파일 없음. 상태 변화는 source scene에 보존함.
- STORY: `STY-REF46-0001`이 POV 전환과 비전환을 정보 제시 순서로 기록함.
- PROSE: `PRO-REF46-0001`이 정보 접근권·서술 거리·캐릭터 판단→문장 형태 연결을 기록함.
- TECHNIQUE: 신규 Macro 0, 신규 Micro 1, 신규 TH 0. 기존 TH 01/05만 보강함.

## 중복·경계

- `SC-REF46-0004`는 legacy `SCENE-15`와 원천이 겹치지만 관찰 정확도/정체 결론 오류와 표현을 재진입하는 별도 질문임.
- `SC-REF46-0005`는 legacy `SCENE-41`과 원천이 겹치지만 마법사 장교 A의 발화 붕괴·결정권 이전이 별도 질문임.
- `TH-REF46-01`, `TH-REF46-05`는 신규 ID가 아니라 레거시 안정 ID의 works-layer bridge임.
- `MIC-REF46-0001`과 같은 143화 표현 단위는 기존 expression-units에서 확인되지 않았음.

## 보류

- 208→360을 성장으로 확정하지 않음.
- 연구 욕구가 항상 규범을 이긴다고 확정하지 않음.
- 449화 개입 거부 동기를 자존심으로 확정하지 않음.
- POV 정보권 패턴을 신규 VERIFIED_THREAD로 승격하지 않음.

## 익명성·품질

- 신규 일반 연구 파일에 실제 작품명·저자명·인물명·조직명·기술명을 사용하지 않음.
- 원문 문장을 장기 복사하지 않고 재독 좌표와 작동 배열을 기록함.
- 작품 모델 front matter는 schema 공통 필드를 사용함.
- 줄거리 목록·성격 형용사·평균 문체 감상으로 퇴행하지 않음.

## 병합 전 조건

1. `main` HEAD 재확인.
2. BASE와 같으면 branch tip을 fast-forward.
3. 병합 뒤 receipt·작품 인덱스·global recent receipts·post-merge audit 갱신.
4. 완료 상태 커밋을 FINAL SHA로 기록하고 별도 SEAL에서 봉인.
