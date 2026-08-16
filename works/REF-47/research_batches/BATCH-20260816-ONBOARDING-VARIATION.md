# BATCH-20260816-ONBOARDING-VARIATION

- work_id: `REF-47`
- mode: `작품 전체 왕복 채굴 / 초기 제시·압축 회수 변형`
- question: `ep1의 초기 제시 선택이 같은 작품의 후속 신규 인물·규칙 온보딩과 압축 회수에서 어떻게 반복·변형·반례화되는가`
- base_sha: `5d241129a4a2e0677823f4735fe800e7c5dee7c9`
- source: `SRC-DIRECT-001`
- full_episode_scope: `ep1 baseline + ep235 + ep269 + ep275 + ep318 + ep350`

## 부트스트랩 검증

- `REPOSITORY_MANIFEST.yaml`에서 canonical branch `main`, 현행 addendum v1.4, SOP v7.1, Repository Contract v1, Work Model Schema v2를 다시 확인했다.
- Project Source 표준 3종의 파일명·SHA-256·byte size가 `REFERENCE_RESEARCH_STANDARD_SOURCE_LOCK_v1.yaml`과 일치했다.
- `catalog/`, `history/`, historical addenda v1.1-v1.3은 연구 근거에서 제외했다.
- `SRC-DIRECT-001` 업로드 원문은 canonical metadata의 SHA-256 `95d22f155d582ec702142b906161f4b36241627a76cdf858ff9b39cd6d686a4e`, byte size `5927798`, UTF-16과 일치했다.

## 전체 회차 직접 재독

- ep1 baseline: `471-862`; 기존 직접 검증 full-episode hash 유지.
- ep235: `126555-126972`; normalized full-episode SHA-256 `5dd3a8e2f60155d8d0681f1f24f0b52647bec32c17216614a34464fd9c84b2b9`.
- ep269: `143231-143724`; normalized full-episode SHA-256 `02cc2a442c3c1d1fe9e3c4001ae8ad2ef415add4c08a89d1b3a09005323e34c5`.
- ep275: `146201-146834`; normalized full-episode SHA-256 `546da03584812072642e1ed5759d120f0fd7cd66c389d6f07cd9e3a9fe668946`.
- ep318: `169913-170380`; normalized full-episode SHA-256 `c96ab603a4e912101fc962a630002dc1790c97197f8856f972417bceed5c53b6`.
- ep350: `185225-185651`; normalized full-episode SHA-256 `40a14817adc65dee5143a9acbd7706b7419b2656bc4ce42e098122a039d32701`.

## 비교 질문별 판정

### 1. ep1의 표면 배열이 작품 기본 온보딩 방식인가

- `CONTRADICTED`.
- ep269의 신규 인물 A는 외부 인물의 오독으로 시작하지 않는다. 최소 국가 정보 뒤 본인의 출근 준비·가족 대화·직무 마찰·강제된 업무 배정으로 판단 기준과 권리 경계가 먼저 보인다.
- ep275의 신규 제도는 현재 심사 권한을 이해할 만큼만 짧게 설명된다.
- 따라서 `외부 분류 → 오독 → 내부 진상`은 ep1의 문제 조건에 맞는 한 실현이지 작품 전체의 고정 제시 골격이 아니다.

### 2. 후속 회수는 무엇을 남기고 무엇을 생략하는가

- `SUPPORTED`.
- ep318은 이미 학습된 파국 규칙을 짧게 회수하고 즉시 관찰자 A의 현재 적대 판단으로 연결한다.
- ep350은 과거 자아의 이름 하나로 누적된 정체성 지식을 호출하고, 설명 대신 현재 관계의 감정 주체를 재분류한다.
- ep235도 과거 자아의 직업·세계 제작 지식을 짧게 회수한 뒤 `현재 나는 누구의 기준으로 선택하는가`라는 새 판단 문제로 이동한다.

### 3. ep1의 정체성 갈등은 장기적으로 같은 이분법을 유지하는가

- `CONTRADICTED` as fixed binary / `SUPPORTED` as changing arc.
- ep1은 과거 자아 이름을 반복해 신체 성격의 침식과 거리를 둔다.
- ep235은 두 정체성을 모두 자신으로 포함하고, 신체 성격에서 유래했다고 인식한 책임 기준도 현재 선택으로 승인한다.
- ep350은 외부 관찰자가 과거 자아 이름으로 반응을 시험하고, 현재 관계 감정의 주체를 현재 신체 인물 A로 재분류한다.
- 단, ep350 외부 시점만으로 과거 자아 기억의 완전 소멸은 확정하지 않는다.

## 여섯 트랙 갱신

### CHARACTER

- `CHR-REF47-0001` 보강.
- 초기 `과거 자아 보존 vs 신체 성격 침식`을 고정 공식에서 장기 변화의 출발점으로 내렸다.
- ep235에서 `두 정체성을 포함한 현재 자신`과 책임 선택이 직접 확인되어 장기 아크를 `SUPPORTED`로 정밀화했다.

### RELATIONSHIP

- 신규 관계 파일 없음.
- ep269은 신규 인물의 직무·귀족 신분·조직 배정권이 첫 제시를 떠받치는 근거로 사용했지만, 이 배치에서 특정 관계의 장기 권리 이동까지 추적하지 않았으므로 독립 REL을 만들지 않았다.
- ep350은 관계 해석의 주체가 재분류되는 근거를 reader information과 CHARACTER에 연결했으나, 후속 권리 변화는 source boundary 밖이므로 관계 전환으로 과장하지 않았다.

### EVENT

- 신규 EVT 없음.
- ep269의 업무 배정·도난 긴급 소집, ep318의 장치 수리 관찰, ep350의 이름 시험·사적 대화는 각 온보딩/회수 선택이 즉시 현재 사건을 발생시키는지 확인하는 근거로만 사용했다.

### STORY

- `EP-0001` 보강.
- ep1의 제시 순서를 고정 템플릿으로 일반화하던 가능성을 후속 첫 제시·callback 반례로 닫았다.
- 현재 SUPPORTED 경계는 `독자가 지금 새로 분류해야 하는 판단은 확대하고, 이미 학습한 정보는 현재 선택의 전제로 압축 회수한다`이다.

### PROSE

- 신규 PRO/PSE/PVAR 없음.
- ep1 기존 `PRO-REF47-0005`의 회차 파형은 그대로 보존하고, 후속 비교에서는 full-episode 정보 밀도·시점·대사/설명 이동을 reader information 모델에서 조건부로 연결했다.
- 국소 문형이나 어미 변형이 이번 질문의 핵심이 아니므로 저수준 증거를 기계적으로 늘리지 않았다.

### TECHNIQUE

- 신규 Source Scene/Macro/Micro/TH 없음.
- 현재 발견은 작품 모델의 기존 `reader_information_model`, `CHR-REF47-0001`, `EP-0001`을 보강하면 원문 재진입과 판단 경계가 손실되지 않는다.
- `설명 밀도 = 현재 선택 비용`이라는 더 강한 메커니즘은 아직 실패·재설명·오판 비용 반례가 부족하므로 TH로 승격하지 않는다.

## 핵심 연결 사슬

독자 선행 지식 상태
→ 지금 새로 분류해야 할 인물·권리·규칙·정체성 문제 선택
→ 필요한 정보만 확대하거나 기존 정보를 압축 회수
→ 현재 인물의 질문·업무·적대·관계 판정으로 즉시 연결
→ 독자가 과거 정보 자체가 아니라 현재 선택의 의미를 재분류
→ 다음 사건·관계 판단이 열린다.

## 다음 연구

압축 회수 또는 최소 온보딩이 충분하지 않아 실제 재설명·오판·관계 비용이 발생하는 장면을 찾는다. 성공 사례만 추가 수집하지 않고 실패·비용·반례를 우선해 현재 SUPPORTED 경계의 적용 조건을 좁힌다.
