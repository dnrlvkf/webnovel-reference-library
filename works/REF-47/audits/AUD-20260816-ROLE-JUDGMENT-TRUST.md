# AUD-20260816-ROLE-JUDGMENT-TRUST

## 범위

- work: `REF-47`
- mode: `작품 전체 왕복 채굴 / 관계 역할 판단권과 신뢰 변형`
- BASE SHA: `ad2c42e8f9cb0059bee85ef582928154f31929d5`
- source: `SRC-DIRECT-001`
- reread: ep286-287,293,297,323-324,331-332,335,339,342-343 + 기존 관련 장면

## 정본·원문 검증

- canonical branch `main` / BASE HEAD 직접 확인.
- Project Source SOP v7.1 / Repository Contract v1 / Work Model Schema v2 lock `PASS`.
- raw source SHA-256 `95d22f155d582ec702142b906161f4b36241627a76cdf858ff9b39cd6d686a4e`, bytes `5927798`, UTF-16 `PASS`.
- 신규 full-episode/segment hashes 재현 `PASS`.

## 핵심 가설 감사

### `신뢰 = 반대 허용`
- `CONTRADICTED` as universal rule.
- 보호자/검 관계에서 신뢰는 강한 행동 정렬로 나타난다.

### `신뢰 = 복종/동조`
- `CONTRADICTED` as universal rule.
- 통치자 관계에서는 충성 때문에 조건부 명령 거절이 발생하고 실제 하옥 비용을 감수한다.
- 사제 관계에서는 전투·이탈 가능성이 남아 있어도 제자의 가능성·완성에 대한 신뢰가 유지된다.

### 정밀화된 판정
- `SUPPORTED`: 신뢰가 어떤 판단권을 남기는지는 관계가 지켜야 할 최고 기준과 역할 의무에 따라 달라진다.
- 상대가 그 기준대로 판단할 것이라는 확신이 있으면 거절·이탈·감시·저지·최종 판정권이 신뢰와 병존할 수 있다.
- 역할 최고 기준 자체가 특정 인물 보호에 정렬되면 신뢰는 행동 정렬을 강화할 수 있다.

## 여섯 트랙 품질 감사

- CHARACTER: `자율성을 존중한다` 같은 형용사로 축소하지 않고 관계별 최고 판단 기준의 차이를 기록. `PASS`.
- RELATIONSHIP: 명령·간언·거절·처벌·이탈·감시·저지·생명 판정권의 실제 배분과 비용을 기록. `PASS`.
- EVENT: ep297 하옥, ep323-324 대립 가능성/신뢰 재분류, 기존 저지·감시 행동으로 상태 변화 확인. `PASS`.
- STORY: 원칙→실행, 대립 준비→신뢰 선언→다음 회차 의미 확대, 정렬형 반례의 제시 순서를 사건과 구분. `PASS`.
- PROSE: 짧은 신뢰/거절 문구 자체를 수집하지 않고 앞뒤 장면 결합과 권리 결과를 분석. 신규 PSE/PVAR 억제 `PASS`.
- TECHNIQUE: 세 관계 변형 + 정렬형 반례가 떨어진 회차에서 확인되어 신규 TH의 VERIFIED_THREAD 조건 충족. `PASS`.

## TH 경계 감사

- `TH-REF47-01`: 정체·기억·누적 정보가 현재 관계 권리로 어떻게 이전/재검증되는가.
- `TH-REF47-02`: 관계 역할의 최고 기준이 신뢰 속 판단권 보존/정렬을 어떻게 결정하는가.
- 일부 Source Scene이 겹쳐도 해결 질문과 반례가 달라 병합하지 않는다. `PASS`.

## Source Scene 감사

- `SC-REF47-0022`: 조건부 거절 원칙.
- `SC-REF47-0023`: 실제 불복종과 하옥 비용.
- `SC-REF47-0024`: 전투 준비 상태의 신뢰 선언.
- `SC-REF47-0025`: 사제 관행과 완성 신뢰 설명.
- `SC-REF47-0026`: 보호/검 역할의 행동 정렬 반례.
- `SC-REF47-0027`: 통치자에게 최종 생명 판정권까지 남기는 장기 회수.
- 모두 source ID / episode / lines / normalized SHA로 재진입 가능. `PASS`.

## 저장 억제 감사

- Macro: 없음. TH/REL/SC보다 독립 집필 검색 가치가 추가되지 않음.
- Micro: 없음. 짧은 신뢰·거절 문구만 떼면 관계 조건과 비용이 사라짐.
- PSE/PVAR: 없음. 저수준 문법보다 장면 배열·권리 결과가 핵심.
- 신규 EVENT/STORY/CHR 파일: 없음. 기존 모델과 신규 REL/TH/SC 연결로 현재 질문이 손실 없이 복원됨.

## 익명성·템플릿 방화벽

- 일반 연구층에 실제 작품명·인물명·원문 장문을 새로 복제하지 않음.
- 역할 슬롯과 source 좌표로 재진입.
- `원칙→실행`, `대립 준비→신뢰 선언` 등의 배열은 observed chain이며 recommended chain이 아님.
- result: `PASS`.

## 판정

`TH-REF47-02`는 신규 VERIFIED_THREAD / SUPPORTED로 적합하다. 다만 적용 문구는 `신뢰하면 반대를 허용한다`가 아니라 `관계의 최고 기준에 따라 상대의 역할 적합 판단권이 보존되거나, 그 기준이 정렬형이면 행동 정렬이 강화된다`로 제한한다.
