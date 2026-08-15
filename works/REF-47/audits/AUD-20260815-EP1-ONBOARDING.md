# AUD-20260815-EP1-ONBOARDING

## 범위

- REF-47
- `SRC-DIRECT-001 / ep1 lines 471-862`
- 다음 회차 즉시 회수 확인만 `ep2 lines 863-929`
- 질문: 첫 진입에서 독자 학습 문제와 여섯 트랙 선택이 어떻게 연결되는가.

## 원문·정본 검증

- source raw SHA-256: `95d22f155d582ec702142b906161f4b36241627a76cdf858ff9b39cd6d686a4e`
- raw bytes: `5927798`
- ep1 normalized SHA-256: `a4085b570676be7cd9fc2e59942651d7ad151d7c62286336445d7654460c1368`
- source bridge 기존 값과 일치.
- BASE SHA: `944a728d8e5b6a3feb13568730af8a41f74c2854`

## authority boundary 감사

- `catalog/`, `history/`: 연구 근거로 사용하지 않음.
- historical addenda v1.1-v1.3: bootstrap 권위로 사용하지 않음.
- 현행 manifest, standard source lock, SOP v7.1, Contract v1, Schema v2, 현행 indexes/works만 사용.
- 결과: `PASS`.

## 중복 감사

- 기존 ep1 expression-wave 연구가 이미 회차 전체 PROSE 파형을 보존하므로 신규 PSE/PVAR/PROSE 파일을 만들지 않음.
- 기존 표현 결론을 CHARACTER/STORY의 사실 근거로 대체하지 않고 원문을 다시 읽어 판정함.
- 결과: `PASS`.

## 트랙 품질 감사

- CHARACTER: 성격 형용사가 아니라 원인 검증 → 생존/정보 우선 → 정체성 저항 → 실제 행동 선택으로 기록. `PASS`.
- RELATIONSHIP: 호감도가 아니라 질문·명령·휴식 허용·업무 책임과 기대값 변화로 기록. 한 번의 칭찬을 관계 전환으로 과장하지 않음. `PASS`.
- EVENT: 줄거리 목록이 아니라 칩거 → 활동 재개의 발생 조건·촉발 선택·상태 변화를 기록. `PASS`.
- STORY: 사건 자체와 제시 순서를 분리하고 독자의 외부 오독 → 내부 재분류 → 화말/다음 화 회수를 기록. `PASS`.
- PROSE: 기존 `PRO-REF47-0005` 재사용, 신규 중복 없음. `PASS`.
- TECHNIQUE: 단일 회차에서 신규 TH/Macro/Micro를 만들지 않음. `PASS`.

## 일반화 방화벽

다음을 전역 규칙으로 승격하지 않음.

- 첫 화는 타인 시점/외부 대화로 시작해야 한다.
- 주인공의 진상을 늦게 공개해야 한다.
- 첫 화에는 반드시 오독이 있어야 한다.
- 신체 성격은 반드시 작은 친절 장면으로 검증해야 한다.
- 사회 복귀가 모든 빙의물 1화의 핵심 상태 변화다.

이들은 REF-47 ep1의 조건부 관찰일 뿐이다.

## 미확인·보류

- ep1의 제시 방식이 REF-47의 기본 온보딩 방식인지: `HOLD`, 후속 신규 온보딩 대조 필요.
- 시스템이 장기 사건 엔진의 중심인지: `HYPOTHESIS`.
- 부하 A와의 작은 기대값 변화가 장기 권리 변화로 이어지는지: `HYPOTHESIS`.
- ep2 전체 기능: 본 감사 범위 밖.

## 판정

- 신규 온보딩 라우팅 계약이 기존 여섯 트랙에 중복 없이 저장되는 실제 사례를 확보함.
- authority boundary도 실제 bootstrap에서 정상 작동함.
- 저장소 구조 추가 변경 필요성은 이번 배치에서 발견되지 않음.
