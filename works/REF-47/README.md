# REF-47 연구 허브

- identity exposure: sealed
- primary source: `SRC-DIRECT-001`
- source bridge: `source_registry/SOURCE-BRIDGE-REF47.md`
- current mode: 구간 정밀 분석 / full-episode expression waveform
- current question: 한 회차 전체에서 대사·지문·내면·설명·행동·효과음·UI·문단·문장이 어떤 파형으로 교대하며, 각 장면의 실제 한국어가 어떤 문법·어휘·생략·배열로 그 교대를 실현하는가

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
- global retrieval contract: `../../indexes/scene_retrieval_contract.md`
- reread scenes: `SC-REF47-0005`, `0007`, `0015`, `0017`
- beat address: `SC-REF47-XXXX#B1` 형식의 장면 내부 주소만 사용
- batch: `research_batches/BATCH-20260815-INTEGRATED-SCENE-PILOT.md`
- audit: `audits/AUD-20260815-INTEGRATED-SCENE-PILOT.md`
- receipt: `research_receipts/RCPT-20260815-1900-REF47.md`
- status: schema promotion `HOLD` — drafting test로 실제 검색 개선을 확인하기 전 v3를 만들지 않음

## 파일셋 6 — 회차 전체 표현 파형

- prose model: `prose/PRO-REF47-0005.md`
- source scope: `SRC-DIRECT-001 / ep1 / lines 471-862`
- batch: `research_batches/BATCH-20260815-EP1-EXPRESSION-WAVE.md`
- audit: `audits/AUD-20260815-EP1-EXPRESSION-WAVE.md`
- receipt: `research_receipts/RCPT-20260815-2151-REF47.md`
- method: `회차 전체 → 장면 → 표현 채널 배열 → 문단 → 문장 → 절·어휘`
- note: 이번 배치에서는 회차 파형 손실을 피하기 위해 새 PSE/PVAR를 기계적으로 만들지 않음

## 공통 인덱스

- `indexes/source_scenes.md` — cross-track observed chain을 보존하되 부분 문제로 검색하는 상위 진입점
- `../../indexes/scene_retrieval_contract.md` — `observed_chain ≠ recommended_chain`, 부분 일치, 불일치 경계, 결합 강제 감사 계약
- `indexes/prose.md`
- `indexes/prose_evidence.md`
- `indexes/prose_variations.md`

현재 REF-47은 작품 전체 문체 모델 완성이 아니라 실제 집필 실패를 원문으로 역추적해 검색 구조를 검증하는 단계다. Source Scene의 결합 사슬은 작가가 그 장면에서 실제로 한 선택을 복원하기 위해 보존하지만, 집필에서는 그 결합을 재현하지 않는다. 표현 연구에서는 국소 문장을 바로 실행 공식으로 바꾸지 않고 해당 회차 전체를 다시 읽어 장면별 대사·지문·내면·설명·행동·효과음·UI 파형을 먼저 확인한 뒤 문단·문장·절·어휘로 내려간다.
