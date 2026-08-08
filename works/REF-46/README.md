# REF-46 연구 정본층

- identity: `sealed`
- boundary: `1~917화 / exact (legacy registry corrections applied)`
- research_mode: `traversal`
- migration_status: `targeted works-layer bridge`
- legacy_catalog_retained: `true`

## 목적

REF-46의 기존 대량 연구는 `catalog/` 레거시층에 남아 있다. 이 디렉터리는 레거시 전량을 복사하지 않고, 새 SOP·작품 모델 스키마로 다시 검증한 고해상도 연구부터 `works/` 정본층에 누적한다.

동일 근거를 새 파일에 전량 재작성하지 않는다. 기존 TH나 장면이 같은 질문을 이미 해결하면 ID를 보존해 브리지하거나 본문에서 레거시 좌표를 연결한다.

## 원천

- source bridge: `source_registry/SOURCE-BRIDGE-REF46.md`
- source identity: sealed
- source boundary and SHA: legacy `catalog/tables/reference-registry.csv`와 source bridge에서 재검증

## 현재 작품 모델

### CHARACTER

- `CHR-REF46-0001` — 신참 마법사 A: 사회적 인정·실제 능력 자기평가·최종 관계 비용
- `CHR-REF46-0002` — 베테랑 안내자 A: 관찰 정확도와 정체 오판, 현장 전문성의 교육 역할 전환
- `CHR-REF46-0003` — 마법사 장교 A: 영역 적합성·책임 구조·규범 override·복귀

### STORY

- `STY-REF46-0001` — 기본 1인칭 흐름에서 제한적 3인칭을 정보 경첩으로 삽입하는 배열

### PROSE

- `PRO-REF46-0001` — 시점 정보권과 캐릭터 판단을 대사·지문 형태로 번역하는 운용

### TECHNIQUE

- `TH-REF46-01` — 기존 VERIFIED_THREAD 브리지 및 인격/존재론 판정 경계 보강
- `TH-REF46-05` — 기존 VERIFIED_THREAD 브리지 및 증거/해석 오류 경계 보강
- `MIC-REF46-0001` — 인정 충족 직후 감정 분절과 말하지 않은 욕망

## 이번 배치의 미생성 판정

- 신규 Macro: 없음. 오늘 장면은 작품 모델·원천 장면·기존 TH와 신규 Micro가 검색 가치를 이미 보존하며, 별도 Macro를 추가하면 중복 가능성이 높다.
- 신규 TH: 없음. POV 정보권과 마법사 장교 A의 연구 욕구 경계는 반복·반례를 더 확인한 뒤 승격한다.
- 신규 RELATIONSHIP/EVENT 단독 파일: 없음. 오늘 질문에서 새로 확인한 관계·사건 상태 변화는 원천 장면과 CHARACTER/STORY/PROSE에 연결하되, 독립 장기 질문이 확인되기 전 별도 파일을 늘리지 않는다.

## 시작점

- `indexes/research.md`
- `source_scenes/SOURCE-SCENES-REF46-0001-0010.md`
- `research_receipts/RCPT-20260808-2330-REF46.md`
