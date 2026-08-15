# REF-47 integrated scene-chain pilot 감사

- base_sha: `63d070243ce234810d93135bcc26739a4799153d`
- branch: `research/ref47-integrated-scene-pilot`
- mode: 작품 전체 왕복 채굴

## 정본/원문 감사
- [x] project-source SOP v7 / repository contract v1 / schema v2 파일명·크기·SHA 잠금 일치
- [x] GitHub manifest / anonymity contract / REF-47 README / 기존 PSE·Source Scene 직접 재조회
- [x] ep238,256,298,331 원문 직접 재독
- [x] 네 구간의 normalized segment SHA가 기존 Source Scene 레지스트리와 재일치

## 구조 감사
- [x] 새 일곱 번째 트랙 생성하지 않음
- [x] 새 독립 scene-beat ID 체계 생성하지 않음; `SC#B` 내부 주소만 사용
- [x] Source Scene을 PROSE 요약이 아니라 cross-track 재진입 허브로 보강
- [x] CHARACTER를 성격 형용사가 아니라 무엇을 먼저 포착하고 어떤 비용을 우선하는지로 기록
- [x] RELATIONSHIP을 호감도가 아니라 질문/반대/차단/결정/보고 권리와 책임으로 기록
- [x] EVENT를 줄거리 목록이 아니라 장면 전후 목표·선택지·행동 상태 변화로 기록
- [x] PROSE는 대사/지문 각각의 역할이 아니라 다음 판단을 발생시키는 결합 사슬로 기록
- [x] 각 beat마다 reader_picture가 물리/상황/캐릭터/관계/사건 중 무엇을 새로 보게 하는지 기록

## 판정
- DIRECT: 네 장면 모두 `포착/관찰 → 판단 → 표현 → 상대 수용/반발 → 사건/관계 상태 변화`의 연결 구간을 원문에서 확인할 수 있다.
- SUPPORTED: Source Scene을 결합 허브로 확장하면 기존 PSE의 `related_characters/relationships/events`가 비어 있어도 장면 자체의 cross-track 연결을 먼저 보존할 수 있다.
- SUPPORTED: 같은 정보 교환이라도 각 인물이 먼저 보는 것과 우선 비용이 달라 대사·지문 실현과 사건 진행이 달라지는 사례가 있다.
- HYPOTHESIS: 이 검색 순서가 실제 새 원고에서 캐릭터 고유성 및 사건 진행 체감을 개선하는지는 다음 drafting test가 필요하다.
- HOLD: 스키마 v3 승격 여부. 파일럿 테스트 전에는 구조 변경 효과가 충분히 검증되지 않았다.

## 실패 경계
- `모든 Source Scene에 beat를 붙인다`로 기계화하지 않는다.
- `reader_picture`를 장면 미사여구나 시각 묘사량 평가로 축소하지 않는다.
- CHARACTER/RELATIONSHIP/EVENT 파일을 장면마다 새로 만드는 방식으로 수를 늘리지 않는다.
- beat 수를 연구 진척으로 세지 않는다.

## 다음 검증
새 테스트 원고를 작성할 때 PSE/PVAR부터 조회하지 않고 `indexes/source_scenes.md → 통합 SC beat → 필요 PSE/PVAR` 순으로 사용하고, 이전 테스트와 캐릭터 교체 가능성·사건 운동·독자 그림을 비교한다.
