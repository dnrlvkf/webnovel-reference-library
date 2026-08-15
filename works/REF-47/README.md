# REF-47 연구 허브

- identity exposure: sealed
- primary source: `SRC-DIRECT-001`
- source bridge: `source_registry/SOURCE-BRIDGE-REF47.md`
- current mode: 작품 전체 왕복 채굴 / integrated scene-chain pilot
- current question: 한 장면에서 캐릭터 판단·관계 권리·사건 운동·대사/지문 실현·독자 그림이 어떻게 한 사슬로 결합되는가

## 파일셋 1 — 추론 범위 제한

- source scenes: `source_scenes/SOURCE-SCENES-REF47-0001-0004.md`
- prose model: `prose/PRO-REF47-0001.md`
- prose evidence: `prose/evidence/PSE-REF47-0001.md` ~ `0004.md`
- variation set: `prose/variations/PVAR-REF47-0001.md`
- receipt: `research_receipts/RCPT-20260815-1753-REF47.md`

## 파일셋 2 — 대사·지문 업무 분담

- source scenes: `source_scenes/SOURCE-SCENES-REF47-0005-0008.md`
- prose model: `prose/PRO-REF47-0002.md`
- prose evidence: `prose/evidence/PSE-REF47-0005.md` ~ `0008.md`
- variation set: `prose/variations/PVAR-REF47-0002.md`
- batch: `research_batches/BATCH-20260815-DIALOGUE-NARRATION.md`
- audit: `audits/AUD-20260815-DIALOGUE-NARRATION.md`
- receipt: `research_receipts/RCPT-20260815-1807-REF47.md`

## 파일셋 3 — 효과음의 정보 턴 배분

- source scenes: `source_scenes/SOURCE-SCENES-REF47-0009-0013.md` + 기존 `SC-REF47-0008`
- prose model: `prose/PRO-REF47-0003.md`
- prose evidence: `prose/evidence/PSE-REF47-0009.md` ~ `0013.md` + 기존 `PSE-REF47-0008` 보강
- variation set: `prose/variations/PVAR-REF47-0003.md`
- batch: `research_batches/BATCH-20260815-SOUND-EFFECT.md`
- audit: `audits/AUD-20260815-SOUND-EFFECT.md`
- receipt: `research_receipts/RCPT-20260815-1819-REF47.md`

## 파일셋 4 — 대화 결속과 비기계적 문답

- source scenes: `source_scenes/SOURCE-SCENES-REF47-0014-0017.md` + 기존 `SC-REF47-0007`
- prose model: `prose/PRO-REF47-0004.md`
- prose evidence: `prose/evidence/PSE-REF47-0014.md` ~ `0017.md` + 기존 `PSE-REF47-0007` 대비
- variation set: `prose/variations/PVAR-REF47-0004.md`
- batch: `research_batches/BATCH-20260815-DIALOGUE-COHESION.md`
- audit: `audits/AUD-20260815-DIALOGUE-COHESION.md`
- receipt: `research_receipts/RCPT-20260815-1846-REF47.md`

## 파일셋 5 — 통합 Source Scene 사슬 파일럿

- integrated scene index: `indexes/source_scenes.md`
- reread scenes: `SC-REF47-0005`, `0007`, `0015`, `0017`
- beat address: `SC-REF47-XXXX#B1` 형식의 장면 내부 주소만 사용
- batch: `research_batches/BATCH-20260815-INTEGRATED-SCENE-PILOT.md`
- audit: `audits/AUD-20260815-INTEGRATED-SCENE-PILOT.md`
- receipt: `research_receipts/RCPT-20260815-1900-REF47.md`
- status: schema promotion `HOLD` — drafting test로 실제 검색 개선을 확인하기 전 v3를 만들지 않음

## 공통 인덱스

- `indexes/source_scenes.md` — 집필 상황에서 캐릭터 판단·관계 권리·사건 운동·독자 그림을 함께 찾는 상위 진입점
- `indexes/prose.md`
- `indexes/prose_evidence.md`
- `indexes/prose_variations.md`

현재 REF-47은 작품 전체 문체 모델 완성이 아니라 실제 집필 실패를 원문으로 역추적해 검색 구조를 검증하는 단계다. 파일럿 동안 Source Scene을 `포착/관찰 → 판단 → 대사·지문·행동·침묵·효과음 → 상대 수용/재판단 → 관계·사건 상태 변화 → 독자 그림`의 cross-track 허브로 사용한다. PSE/PVAR는 이 사슬의 저수준 실현을 다시 읽는 하위 증거층으로 둔다. 다른 트랙은 독립 장기 질문이 확인될 때만 별도 ID로 승격한다.
