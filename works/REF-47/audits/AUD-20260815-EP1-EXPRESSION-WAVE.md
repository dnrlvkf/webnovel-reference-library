# REF-47 audit — ep1 expression waveform

- work_id: `REF-47`
- date_time: `2026-08-15T21:51:00+09:00`
- mode: `구간 정밀 분석`
- source_scope: `SRC-DIRECT-001 / ep1 / lines 471-862`
- base_sha: `b9ce1c84b384ee2ff4b2c2548d7467453a2a1ab2`
- audited_branch_head_before_receipt: `435a5b7a2a4aa897c2ad3dd740536b90e2448515`

## 표준·원천 검증
- Project Source SOP v7.1 SHA-256: `3803ff35ff9d68211aa2ab655b76dd387567f441a424f41e2a8e5884722fe8c5`
- repository contract v1 SHA-256: `8a6479621af6d1196433ca5760ae727eb5ccc1b876dea468df3faafc964e304e`
- work model schema v2 SHA-256: `1e6f5188749130900349cc7f54a9c07f888946d912485124fe45c7b4f50563f8`
- source raw SHA-256: `95d22f155d582ec702142b906161f4b36241627a76cdf858ff9b39cd6d686a4e`
- source raw bytes: `5927798`
- ep1 header: line 471
- next ep2 header: line 863
- ep1 full normalized SHA-256: `a4085b570676be7cd9fc2e59942651d7ad151d7c62286336445d7654460c1368`

## 질문 적합성 감사
사용자 요구는 개별 문장·문단의 표현 수집이 아니라 한 회차 안에서 대사·지문·내면·설명·행동·효과음·UI를 함께 보고, 그 전체 파형 속에서 실제 단어·문법·생략·배열을 연구하는 것이다.

이번 기록은 다음 순서를 지켰다.
`회차 전체 → 장면 → 표현 채널 배열 → 문단 → 문장 → 절·어휘`

## 과추상화 감사
- `짧은 문장을 쓴다`로 요약하지 않음.
- `대사 비중을 높인다`로 요약하지 않음.
- `효과음을 독립시킨다`로 요약하지 않음.
- 실제로 같은 회차 안에서 채널과 문법 밀도가 바뀌는 위치를 보존함.
- 같은 성격 정보가 설명 블록과 후반 사회적 상호작용에서 서로 다른 표면으로 재현되는 사례를 함께 기록함.

## 국소 표본 과잉 감사
- 새 PSE/PVAR를 만들지 않음.
- 이유: 이번 질문의 핵심 증거는 회차 전체 파형이며, 짧은 문장 표본으로 분리하면 장면 간 대비와 채널 전환 정보가 손실됨.
- 기존 PSE/PVAR는 삭제·강등하지 않음. 그 층은 국소 재진입이 필요한 다른 질문에 계속 유효함.

## 여섯 트랙 감사
- CHARACTER: 주인공의 성격 전염/자기정체성 충돌이 중반 설명과 후반 대화 검증으로 표현 채널을 바꿔 나타나는 점만 연결. 장기 캐릭터 신규 판정 없음.
- RELATIONSHIP: 하인/방문자/보조자와의 권리 차이가 종결·머뭇거림·짧은 명령·반응에서 드러나는 점만 표현 근거로 기록. 장기 관계 신규 판정 없음.
- EVENT: 방문, 강연 결정, 이동이라는 사건이 채널 전환을 촉발하는 위치를 기록. 신규 사건 모델 없음.
- STORY: 외부 오해 → 내부 진상/온보딩 → 사회적 검증 → 새 공간 화말의 제시 순서를 표현 파형과 연결.
- PROSE: `PRO-REF47-0005` 신규.
- TECHNIQUE: 신규 Source Scene/Macro/Micro/TH 없음.

## 반례·보류
- `첫 화는 외부 대화로 시작한다`: 일반화 금지.
- `화말은 시각 묘사로 끝낸다`: 일반화 금지.
- `효과음은 독립 문단이 좋다`: 일반화 금지.
- `짧은 문장이 강하다`: 길이가 아니라 앞선 축적과 위치 조건이 필요하며, 다른 회차 대조 전에는 작품 상수로 확정하지 않음.

## 변경 파일 감사
branch compare 기준 5개 의도 파일만 변경됨.
- `works/REF-47/README.md`
- `works/REF-47/indexes/prose.md`
- `works/REF-47/prose/PRO-REF47-0005.md`
- `works/REF-47/research_batches/BATCH-20260815-EP1-EXPRESSION-WAVE.md`
- `works/REF-47/source_registry/SOURCE-BRIDGE-REF47.md`

이 감사 파일과 영수증/최근 영수증 인덱스는 sealing 단계에서 추가한다.

## 다음 검증
현재 집필 원고 1화를 같은 방식으로 `회차 전체 → 장면 → 표현 채널 → 문단 → 문장 → 절·어휘` 순서로 읽고, 논리 기능이 아니라 실제 표현 밀도·채널 전환·문법 결속의 격차를 대조한다.
