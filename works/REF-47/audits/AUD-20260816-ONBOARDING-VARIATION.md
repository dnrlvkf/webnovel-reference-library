# AUD-20260816-ONBOARDING-VARIATION

## 범위

- work: `REF-47`
- mode: `작품 전체 왕복 채굴 / 초기 제시·압축 회수 변형`
- BASE SHA: `5d241129a4a2e0677823f4735fe800e7c5dee7c9`
- source: `SRC-DIRECT-001`
- full reread: ep1 baseline, ep235, ep269, ep275, ep318, ep350

## 정본·원문 검증

- canonical branch: `main`.
- Project Source standard files: filename / SHA-256 / byte size lock `PASS`.
- raw source SHA-256: `95d22f155d582ec702142b906161f4b36241627a76cdf858ff9b39cd6d686a4e`.
- raw source bytes: `5927798`.
- raw source encoding: UTF-16.
- source identity: `VERIFIED_MATCH`.
- target episodes 235/269/275/318/350 are inside the already verified 167-350 header boundary; current batch rechecked each full episode boundary.

## authority boundary

- `catalog/`, `history/`: research evidence로 사용하지 않음.
- historical addenda v1.1-v1.3: bootstrap authority로 사용하지 않음.
- current manifest / v1.4 addendum / SOP v7.1 / Contract v1 / Schema v2 / active `works/`, `registry/`, `indexes/`만 사용.
- result: `PASS`.

## 여섯 트랙 품질 감사

- CHARACTER: ep1 성격표를 반복하지 않고 ep235 직접 내부 판정과 ep350 외부 관계 판정을 분리해 장기 기준 변화를 기록. `PASS`.
- RELATIONSHIP: ep269의 직무/신분 권리를 신규 장기 관계로 과장하지 않고, ep350의 감정 주체 재분류도 후속 권리 변화가 없으므로 독립 관계 전환으로 등록하지 않음. `PASS`.
- EVENT: 후보 회차를 줄거리 목록으로 만들지 않고 온보딩/회수 정보가 현재 업무·적대·관계 판단을 발생시키는지에만 사용. `PASS`.
- STORY: ep1의 실제 제시 순서와 후속 first-presentation/callback의 다른 배열을 분리해 `고정 템플릿` 가설을 반증. `PASS`.
- PROSE: 짧은 설명/긴 설명의 평균값을 규칙화하지 않고 reader prior knowledge와 현재 판단 기능의 차이로 기록. 신규 PSE/PVAR 남발 없음. `PASS`.
- TECHNIQUE: 현재 작품 모델 보강으로 충분한 근거를 Source Scene/Macro/Micro/TH로 중복 복사하지 않음. `PASS`.

## 반례·경계 감사

- `첫 제시는 외부 오독 뒤 내부 진상을 보여 준다`: `CONTRADICTED` by ep269/ep275.
- `새 정보는 길게 설명한다`: `CONTRADICTED` by ep275.
- `callback은 단순 요약이다`: `CONTRADICTED` by ep318/ep350; 회수 정보가 현재 적대·관계 재분류의 전제로 작동.
- `과거 자아 보존 vs 신체 성격 침식`이 장기 고정 이분법이다: `CONTRADICTED` by ep235; ep350은 외부 지원 근거.
- `설명 밀도는 현재 선택/관계 비용에 비례한다`: 아직 `HYPOTHESIS`; 실패·재설명 비용 장면이 필요.

## 원문 재독 가치

- ep269: 새 인물의 직무·신분·가족/조직 압력이 어떤 순서로 첫 행동을 만드는지 다시 확인할 가치가 있음.
- ep275: 제도 전체가 아니라 현재 평가권만 설명하는 경계를 확인할 가치가 있음.
- ep318: 이미 학습된 파국 규칙이 현재 적대 판단으로 전환되는 압축 회수를 확인할 가치가 있음.
- ep235/350: 같은 정체성 정보가 초기 방어 문제에서 자기 통합·관계 주체 판정으로 어떻게 다른 질문을 여는지 비교할 가치가 있음.

## 저장 억제 감사

- 신규 PSE/PVAR: `NO` — 저수준 문법 변형이 이번 질문의 독립 손실 지점이 아님.
- 신규 Source Scene: `NO` — full-episode source bridge와 work model 좌표로 현재 재진입 목적 충족.
- 신규 Macro/Micro: `NO` — 기존 작품 모델보다 독립적인 집필 검색 단위로 분리해야 할 추가 판단이 아직 없음.
- 신규 TH: `NO` — 메커니즘 후보는 보이지만 실패·비용·재설명 반례가 부족해 현재는 reader information의 `SUPPORTED/HYPOTHESIS` 경계로 보존.

## 익명성 감사

- 일반 연구 파일에 실제 작품명·저자명·원천 파일명 미기재.
- 실제 인물·조직·지명·기술 고유명 대신 기능 역할명 사용.
- 검색 가능한 길이의 독특한 원문 문장 미복사.
- source ID / episode / line / hash로 재진입 가능.
- result: `PASS`.

## 판정

- ep1 초기 제시 표면의 작품 전체 기본 템플릿 가설은 닫을 수 있다.
- 작품 내부에서 더 안정적으로 남는 것은 `reader prior knowledge와 현재 재분류 문제에 따라 확대/압축 대상을 바꾼다`는 경계다.
- 다만 `왜 그 정도 분량인가`의 비용 함수까지 확정하지 않는다. 다음 배치는 압축 실패·재설명·오판 비용을 우선 추적한다.
