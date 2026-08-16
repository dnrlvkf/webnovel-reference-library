# AUD-20260816-PRIOR-KNOWLEDGE-RECLASSIFICATION

## 범위

- work: `REF-47`
- mode: `작품 전체 왕복 채굴 / 독자 선행 지식 압축 실패·재온보딩 비용`
- BASE SHA: `476ca2a9d4271de54fce65cee1c446c6a08381f7`
- source: `SRC-DIRECT-001`
- full reread: ep297-298, ep320, ep327-328, ep330-331, ep350

## 정본·원문 검증

- canonical branch `main` / BASE HEAD 직접 확인.
- Project Source standard files filename / SHA-256 / byte size lock `PASS`.
- raw source SHA-256 `95d22f155d582ec702142b906161f4b36241627a76cdf858ff9b39cd6d686a4e`.
- raw source bytes `5927798`.
- raw source encoding UTF-16.
- source identity `VERIFIED_MATCH`.
- 모든 대상은 verified `167-350` header 범위 안이며 각 회차 시작/다음 header 또는 EOF를 다시 확인했다.

## 여섯 트랙 품질 감사

- CHARACTER: 이번 질문의 중심이 아닌 기존 주인공 모델을 억지로 수정하지 않음. ep331의 현재 인물 A 판단은 TH/PSE 근거로만 사용. `PASS`.
- RELATIONSHIP: 정체 주장과 감정 고백을 호감 변화로 처리하지 않고 말투·증명 요구·사적 정보 공개·접근권 변화로 기록. `PASS`.
- EVENT: 후보 회차를 사건 연표로 복제하지 않고 정체 주장·기억 구현·사적 공개가 선택을 바꾸는 조건만 TH에 연결. `PASS`.
- STORY: reader prior knowledge와 character prior knowledge를 분리하고, 압축 실패가 어느 연결부에서 발생하는지 비교. `PASS`.
- PROSE: 문장 길이 평균이 아니라 `-는 줄 알았다` 반복, 짧은 전환문, 짧은 질문+긴 정체성 블록, 짧은 부정/긍정 관계 대비의 조건 차이를 PSE/PVAR로 보존. `PASS`.
- TECHNIQUE: TH는 ep297-350의 떨어진 반복·변형과 실패/비용/반례가 있어 `VERIFIED_THREAD` 조건 충족. Macro/Micro/Source Scene 중복 생성 없음. `PASS`.

## 문장·문단 연구 감사

- `PSE-0018`: 과거 오독 여러 문장을 하나의 장문으로 합치지 않고 반복 완결문으로 쌓은 이유와, 짧은 전환문이 판정 시점을 바꾸는 기능을 기록.
- `PSE-0017`: 기존 기록을 재사용하되 짧은 질문과 긴 판단 블록이 왜 함께 필요한지 새로운 PVAR에서 비교.
- `PSE-0019`: 높은 관계 비용에도 재분류 핵심이 짧은 독립문으로 수렴하는 반례를 기록.
- `PVAR-0005`: `짧게/길게` 규칙이 아니라 누락 연결의 종류와 reader prior knowledge가 문장·문단 경계를 바꾸는 조건을 보존.
- 결과: `PASS`.

## 반례·강등 감사

- `독자가 이미 알면 압축하면 된다`: `CONTRADICTED` as sufficient condition.
- `오분류 비용이 클수록 설명이 길어진다`: `CONTRADICTED` as scalar rule by ep350.
- `같은 이름/정체면 과거 관계 권리가 복원된다`: `CONTRADICTED` by ep327-328/350.
- `재온보딩은 긴 회상이다`: `CONTRADICTED`; ep350은 짧은 관계 주체 대비.
- 기존 ep318은 누적 규칙과 현재 분류가 호환될 때 짧은 callback으로 충분한 반례로 유지.

## TH 승격 감사

- 떨어진 반복/변형: ep297-298,320,327-328,330-331,350.
- 실패: ep327-328 정체 주장만으로 관계 권리 이전 실패.
- 비용: ep320/331 기억 불연속으로 현재 관계 주체가 과거 권리를 자동 소유하지 못함.
- 성공: ep350 현재 발화 주체 재분류 뒤 사적 정보·응답·기록 전달.
- 적용 경계/반례: ep318의 압축 회수 성공, ep275의 짧은 신규 제도 설명.
- 결과: `TH-REF47-01 VERIFIED_THREAD` 적합.

## 익명성 감사

- 일반 연구 파일에 실제 작품명·저자명·원천 파일명 미기재.
- 실제 인물·조직·지명·기술 고유명 대신 역할 슬롯 사용.
- 검색 가능한 길이의 원문 문장을 복사하지 않음.
- 문법 연구에 필요한 `-는 줄 알았다`, `-가 아니라`, `-니까` 등 기능적 표면만 보존.
- source ID / episode / line / SHA로 원문 재진입 가능.
- result: `PASS`.

## 저장 억제 감사

- 신규 Source Scene: `NO` — 기존 SC-0017과 full-episode/PSE 좌표로 현재 사슬 재진입 가능.
- 신규 Macro/Micro: `NO` — 새 TH/REL/PROSE보다 독립 집필 검색 가치가 추가되지 않음.
- 신규 EVT/CHR: `NO` — 이번 질문을 위해 중복 모델을 만들 필요 없음.
- 신규 REL/TH/PSE/PVAR/PRO: 필요한 독립 손실 지점이 있어 생성.

## 판정

- `reader prior knowledge`는 압축 가능성의 충분조건이 아니라 **현재 분류 과제와의 호환성 조건**으로 정밀화됨.
- 재온보딩은 전체 설정 재설명이 아니라 현재 인과·기억·관계 주체 중 어긋난 연결부를 다시 여는 방식으로 확인됨.
- 문장·문단 길이는 비용 크기보다 누락 연결 종류와 선행 축적에 따라 다르게 실현됨.
