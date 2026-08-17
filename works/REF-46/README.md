# REF-46 연구 정본층

- identity: `sealed`
- boundary: `1~917화 / exact (legacy registry corrections applied)`
- research_mode: `traversal`
- migration_status: `targeted works-layer bridge`
- legacy_catalog_retained: `true`

## 목적

REF-46의 기존 대량 연구는 `catalog/` 레거시층에 남아 있다. 이 디렉터리는 레거시 전량을 복사하지 않고, 최신 SOP·작품 모델 스키마로 다시 검증한 고해상도 연구부터 `works/` 정본층에 누적한다.

동일 근거를 새 파일에 전량 재작성하지 않는다. 기존 TH나 장면이 같은 질문을 이미 해결하면 ID를 보존해 브리지하고, 독립 캐릭터·관계·조직·스토리 질문이 확인될 때만 작품 모델 파일을 추가한다.

## 원천

- source bridge: `source_registry/SOURCE-BRIDGE-REF46.md`
- source identity: sealed
- source boundary and SHA: legacy registry와 source bridge에서 재검증
- current transport: access-controlled private source / `VERIFIED_MATCH`

## 현재 작품 모델

### CHARACTER

- `CHR-REF46-0001` — 신참 마법사 A: 사회적 인정·실제 능력 자기평가·최종 관계 비용
- `CHR-REF46-0002` — 베테랑 안내자 A: 관찰 정확도와 정체 오판, 역할별 자기평가, 교육 전환, 마지막 호송 책임
- `CHR-REF46-0003` — 마법사 장교 A: 영역 적합성·책임 구조·제도 권한·규범 override·복귀

### RELATIONSHIP

- `REL-REF46-0001` — 베테랑 안내자 A ↔ 행정 담당자 A: 생전 관계권 한계와 사후 정보·애도 정당성
- `REL-REF46-0002` — 주인공 A ↔ 베테랑 안내자 A: 정체 질문·유료 교육·시혜 거절·구조와 보호 방향 역전
- `REL-REF46-0003` — 주인공 A ↔ 마법사 장교 A: 전문 판단권·정체 정보·공적 보고 의무의 교차

### ORGANIZATION

- `ORG-REF46-0001` — 종족 공동체 A: 전사·장로 권위와 전문 행정·재정·교육·고용 기능의 분리
- `ORG-REF46-0002` — 군 조직 A: 보고·명령·위임 권한이 책임 자원이자 개인 행동 제약으로 작동하는 병단

### STORY

- `STY-REF46-0001` — 기본 1인칭 흐름에서 제한적 타인 시점을 정보 경첩으로 삽입하는 배열
- `STY-REF46-0002` — 조연의 죽음을 미래 가치·관계 정보·기술·비교 기준으로 분산 회수하는 외적 유산 배열

### PROSE

- `PRO-REF46-0001` — 시점 정보권과 캐릭터 판단을 대사·지문 형태로 번역하는 조건부 운용
- 현재 REF-46에는 독립 저수준 손실을 확인한 PSE/PVAR가 없어 기계적 생성을 억제한다.

### TECHNIQUE

- `TH-REF46-01` — 사회적 가면이 구성원 책임과 제도적 역할로 굳어지는 장기 스레드
- `TH-REF46-05` — 다중 신분 증거 누적과 해석 오류·정보 권리 스레드
- `MAC-REF46-0001` — 미완 관계를 사후 고백으로 강제 완성하지 않고 애도 정당성만 교정하는 재독 단위
- `MIC-REF46-0001` — 인정 충족 직후 감정 분절과 말하지 않은 욕망
- `MIC-REF46-0002` — 시혜 가능성을 조건절로 먼저 분류하고 실제 전문 수요에서 수락하는 표현 단위
- Source Scene: `SC-REF46-0001~0030`

## 편중 감사 원칙

`BATCH-REF46-0012`에서 RELATIONSHIP / ORGANIZATION 작품 모델 편중을 감사했다.

- 감사 전 standalone 분포: CHARACTER 3 / RELATIONSHIP 1 / ORGANIZATION 0.
- 신규 파일은 숫자를 맞추기 위해 만들지 않았다.
- 기존 CHARACTER·TH·Source Scene에 반복 근거가 있고, 별도 권리·조직 질문으로 재독해야 하는 네 공백만 `REL-REF46-0002~0003`, `ORG-REF46-0001~0002`로 보강했다.
- 신참 마법사 A의 미완 감정 관계와 기타 정체 네트워크·조직은 현재 독립 권리 질문이 충분하지 않아 미생성 상태를 유지한다.

## 현재 보류와 다음 연구 방향

현재 가장 선명한 미확인 조직 질문은 다음이다.

> 후반 공개 정체 뒤 종족 공동체 A는 주인공 A의 대표·자원·접근·교육 결정권을 계속 인정하는가. 인정한다면 혈통·영혼·현재 행동·누적 책임 중 무엇이 대표 자격의 최종 기준으로 작동하는가.

군 조직 A에서는 마법사 장교 A의 이탈 뒤 과거 보고망·부하 관계·공적 신뢰가 실제 접근 자원으로 남는지가 별도 HOLD다. 구체 원문 질문으로 열 때만 후속 채굴한다.

## 시작점

- `indexes/research.md`
- `source_registry/SOURCE-BRIDGE-REF46.md`
- `source_scenes/`
- `research_receipts/RCPT-20260817-1523-REF46.md`
