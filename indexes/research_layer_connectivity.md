# 참고작 연구층 연결 계약

> 목적: 기존 Source Scene·작품 모델 5트랙·PSE/PVAR·Macro·Micro·TH를 새 태그 DB로 만들지 않고, 원문에서 작가 선택까지 올라가고 집필 문제에서 원문까지 다시 내려갈 수 있는 양방향 연구 그래프로 운용한다.

## 1. 새 연구층이 아니다

이 문서는 `REFERENCE_WORK_MODEL_SCHEMA_v2`가 이미 허용한 관계 필드와 기존 ID를 어떻게 함께 갱신할지 정하는 운영 계약이다.

- Schema v3를 만들지 않는다.
- 새 Technique 계층을 만들지 않는다.
- edge 수나 링크 수를 연구 성과로 간주하지 않는다.
- 기존 파일을 보강할 수 있으면 새 파일을 만들지 않는다.

## 2. 기준 사슬

가능한 장면에서는 다음 연결을 복원한다.

```text
원문 Source
→ Source Scene
→ CHARACTER 판단 기준
→ 선택
→ EVENT 발생·변형
→ STORY 제시 순서·정보 배분
→ PROSE / PSE 실제 실현
→ 독자 해석
→ RELATIONSHIP·정보·권한·목표 변화
→ 다음 CHARACTER 판단
```

`TECHNIQUE`는 이 사슬 밖의 별도 태그 묶음이 아니라 Source Scene·Macro·Micro·TH가 이 연결을 어떻게 구현했는지 설명한다.

모든 장면이 모든 노드를 가져야 하는 것은 아니다. 원문 근거가 없는 연결은 `HYPOTHESIS` 또는 `HOLD`로 두고 억지로 채우지 않는다.

## 3. Source Scene을 근거 허브로 둔다

Source Scene은 장면 요약이 아니라 원문 재진입과 상태 변화 확인의 허브다.

가능한 경우 Source Scene에서 다음을 찾을 수 있어야 한다.

- `source_id` 또는 작품 source bridge
- episode / line / offset / segment SHA 등 원문 좌표
- 연결 CHARACTER 기록
- 연결 RELATIONSHIP 기록
- 연결 EVENT 기록
- 연결 STORY 기록
- 연결 PROSE 기록
- 필요한 경우 PSE/PVAR
- 필요한 경우 Macro/Micro/TH
- 실제 `observed_chain`

`observed_chain`은 그 원문 장면에서 함께 일어난 순서이지 `recommended_chain`이 아니다.

## 4. 작품 모델 5트랙의 최소 연결

### CHARACTER

판단·선택을 성격표로 남기지 않는다.

최소한 가능한 범위에서:

`CHARACTER → 선택 근거 Source Scene → EVENT 결과 → RELATIONSHIP/정보/권한 변화 → 후속 선택`

을 추적한다.

### RELATIONSHIP

호감도가 아니라 실제 권리·책임 변화를 연결한다.

`RELATIONSHIP 변화 → 그것을 발생시킨 선택/EVENT → 증명 행동 Source Scene → 후속 권리 행사`

를 찾는다.

### EVENT

줄거리 항목이 아니라 상태 변경 단위다.

`발생 조건 → 촉발 선택 → 결과/비용 → 관계·정보·권한·자원·목표 변화 → 후속 EVENT`

의 근거 장면을 연결한다.

### STORY

실제 사건 순서와 제시 순서를 구분한다.

`EVENT → 작가의 제시/생략/압축/지연 선택 → 독자 정보 상태 → 재분류/화말/다음 문제`

를 연결한다.

### PROSE

표현을 장식으로 분리하지 않는다.

`장면 조건/판단 → 반응 채널 → 실제 대사·지문·문장·문단 선택 → 상대/독자 해석 → 상태 변화`

를 연결하고, 저수준 선택이 요약에서 사라질 때만 PSE/PVAR로 내려간다.

## 5. PSE/PVAR 연결

- PSE는 반드시 정확한 `source_locations`와 가능한 경우 `source_scenes`를 가진다.
- PSE는 관련 PROSE 모델로 올라갈 수 있어야 한다.
- PVAR는 비교하는 PSE ID를 명시하고, 각 PSE의 source location으로 다시 내려갈 수 있어야 한다.
- PVAR는 같은 기능의 다른 실현을 보여 주는 비교층이며 TH가 아니다.
- PSE/PVAR의 표면을 집필 공식으로 직접 컴파일하지 않는다.

## 6. Macro/Micro/TH 연결

### Macro

- 원문 위치와 Source Scene을 연결한다.
- 어떤 CHARACTER/RELATIONSHIP/EVENT/STORY/PROSE 문제 때문에 다시 읽을 가치가 있는지 명시한다.
- 현재 작품에 가져올 것은 `usable_judgment`, 가져오지 말아야 할 것은 `do_not_import`로 분리한다.

### Micro

- 반드시 `직전 배치 → 표현 → 직후 배치 → 작동 결과 → 없으면 사라지는 것`이 성립한다.
- 해당 Micro가 속한 Source Scene/Macro와 원문 위치를 잃지 않는다.

### TH

- member evidence를 떨어진 Source Scene들로 연결한다.
- 반복뿐 아니라 변형·실패·비용·반례의 역할을 구분한다.
- 한 Source Scene만으로 `VERIFIED_THREAD`를 만들지 않는다.
- TH에서 관련 작품 모델 항목으로 올라갈 수 있고, 작품 모델에서도 관련 TH를 역링크한다.

## 7. 양방향 링크 원칙

Schema v2의 기존 필드가 양쪽 파일에 모두 존재한다면 안정된 관계는 가능한 한 양쪽에 기록한다.

예:

```text
CHARACTER.related_events ↔ EVENT.related_characters
PROSE.related_prose_evidence ↔ PSE.related_prose_profiles
PSE.related_prose_variations ↔ PVAR.related_prose_evidence
작품 모델.related_threads ↔ TH의 관련 모델 ID
Source Scene의 관련 ID ↔ 각 모델의 source_scenes
```

다만 단순히 역링크를 채우기 위해 판단을 복제하지 않는다. 상세 근거는 한 곳에 두고 다른 파일에서는 ID와 짧은 관계 설명으로 연결한다.

## 8. 링크의 의미를 과도하게 스키마화하지 않는다

`causes / reveals / changes / constrains / implements` 같은 관계어는 본문에서 작동 사슬을 설명하는 데 사용할 수 있지만, 지금 단계에서 새 영구 edge taxonomy DB를 만들지 않는다.

중요한 것은 링크의 수가 아니라 다음 질문에 답할 수 있는가다.

- 무엇이 원인이고 무엇이 결과인가.
- 어떤 판단이 어떤 선택을 만들었는가.
- 어떤 표현이 독자/상대의 해석을 바꿨는가.
- 실제 상태 변화가 어디에서 증명되는가.
- 반례가 어느 기존 판정을 무너뜨리는가.

## 9. 집필 검색의 하행 경로

집필 문제에서 참고작을 찾을 때:

1. 현재 작품의 CHARACTER/RELATIONSHIP/EVENT/POV/native anchor를 먼저 잠근다.
2. 현재 문제를 필요한 연구 트랙으로 분해한다.
3. 작품 모델·TH·PVAR·Macro 등에서 후보를 찾는다.
4. 후보에서 Source Scene/PSE/source location으로 내려간다.
5. `indexes/source_reentry_contract.md`에 따라 `source_id → canonical identity → transport → VERIFIED_MATCH`를 만든다.
6. 실제 원문 full episode를 재독한다.
7. 현재 작품과의 mismatch boundary를 확인한다.
8. 현재 작품 조건으로 새 장면을 선택한다.

파생층에서 원문으로 내려가지 못하면 그 작품의 실제 표현을 참고했다고 주장하지 않는다.

## 10. 연구의 상행 경로

새 원문을 연구할 때:

1. 원문 위치와 Source Scene을 먼저 고정한다.
2. 장면에서 확인된 판단·선택·상태 변화를 5트랙에 연결한다.
3. 저수준 산문화 선택이 손실될 때만 PSE를 만든다.
4. 같은 기능의 다른 실현이 실제로 모였을 때만 PVAR를 만든다.
5. 향후 집필 검색 가치가 독립적으로 있을 때만 Macro를 만든다.
6. Macro로 사라지는 결정적 표현만 Micro로 만든다.
7. 떨어진 반복·변형·실패·반례가 모일 때 TH를 보강한다.
8. 생성한 모든 상위 판단이 Source Scene/원문으로 다시 내려가는지 감사한다.

## 11. 연결 감사

새 연구 배치 또는 기존 기록 보강 시 확인한다.

- Source Scene에서 실제 source identity로 내려갈 수 있는가.
- CHARACTER가 성격 형용사만 남지 않았는가.
- RELATIONSHIP 변화가 권리·책임의 실제 행동으로 증명되는가.
- EVENT 결과가 관계·정보·권한·목표 변화와 연결되는가.
- STORY가 EVENT 요약을 복사한 것에 그치지 않는가.
- PROSE가 PSE/PVAR 또는 구체 Source Scene과 연결되는가.
- Macro/Micro/TH가 원문 재독 좌표를 잃지 않았는가.
- 필요한 양방향 링크가 한쪽에서 끊기지 않았는가.
- `observed_chain`을 집필용 `recommended_chain`으로 바꾸지 않았는가.
- 반례가 들어왔을 때 기존 링크·판정도 함께 강등/수정되는가.

## 12. 완료 판정

연결 구조가 작동한다고 말하려면 두 방향이 모두 가능해야 한다.

```text
원문 → 장면 → 판단/사건/표현 → 장기 모델/TH
집필 문제 → 모델/기법 후보 → Source Scene/PSE → 실제 원문
```

한쪽만 가능하면 연구 저장 또는 집필 검색 중 하나가 끊긴 상태다.
