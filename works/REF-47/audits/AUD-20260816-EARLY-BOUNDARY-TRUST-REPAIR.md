# AUD-20260816-EARLY-BOUNDARY-TRUST-REPAIR

## 범위
- work: `REF-47`
- mode: 작품 전체 왕복 채굴
- BASE: `a5e0b288fb5f01a7d3a3b3543ca7d26cfa59afdf`
- original: `SRC-DIRECT-001`

## 원문/표준 감사
- raw SHA-256 `95d22f155d582ec702142b906161f4b36241627a76cdf858ff9b39cd6d686a4e`, bytes `5927798`, UTF-16 일치.
- SOP v7.1 / contract v1 / schema v2 SHA·byte size가 source lock과 일치.
- ep1-166: 166개 연속 경계 검증, line 92262의 explicit ep167 anchor 확인.
- nonstandard boundary ep25/62/68/157/158 직접 보정.
- boundary core SHA `58d92a04b52dc661e4bbc8d7f4567280cf770976c58a47e8b916d9feb874ff52`.
- boundary fullmap SHA `4b707c2c1ee217c280529a258eee15ba8668a0510839c9459da2e24b1a7303d2`.

## 판정 감사
- ep78: 상대의 적대 가능성·진심 불확실성을 주인공 A가 이미 알고 있음. 숨은 정체 후속을 오독 증거로 소급하지 않음 — PASS.
- ep124: 이탈·대립 준비와 지원 지속·통상 벌점을 함께 보존 — PASS.
- ep132: 잘못·배신과 제자 역할 유지의 후속 인식 — PASS.
- ep163: protagonist-side 감정/관계 상태 오독은 DIRECT, 역할 최고 기준 오독은 아님 — PASS.
- protagonist-side `역할 최고 기준 오독→판단권 오배분→직접 수정`: 미확인, HOLD 유지 — PASS.
- `판단권 전면 회수`를 반복 메커니즘으로 억지 생성하지 않음 — PASS.

## 중복/스키마 감사
- 기존 TH-02가 이미 신뢰 실패 분류를 해결하므로 신규 TH 없음.
- ep124/132는 기존 REL-0004의 장기 전사 보강으로 처리.
- SC-0034~0037은 각각 불확실성 위임 / 역할 유지+국소 규율 / 후속 역할 유지 / 관계 상태 오독 경계로 기능이 달라 중복 아님.
- 신규 Macro/Micro/PSE/PVAR 없음.
- Schema v3 승격 필요 없음.

## 복구 메커니즘 감사
현재 검증군에서 확인된 조정:
- 역할 유지 + 국소 규율
- 현재 판단 반박 + 관계 신뢰 유지
- 실행 실패 뒤 독립 분석권 유지
- 정보 범위 부분 조정
- 과거 잘못 뒤 교정 책임 추가

`SUPPORTED`: 관계 전체 즉시 철회보다 실패한 층의 국소 조정이 반복된다.
`HOLD`: 전면 판단권 회수가 독립적 반복 메커니즘인지 미확인.

## 운영 감사
- main 쓰기 전 remote HEAD를 BASE와 재확인해야 함.
- content commit 후 BASE→content diff 파일 목록을 직접 감사.
- receipt seal 전 remote HEAD 재확인.
- FINAL SHA remote 반영 확인 전 완료 보고 금지.
- 도구 점검 중 생성된 비정본 임시 refs `__ignore_tmp`, `__ignore_tmp2`는 main 내용과 무관하다. 현재 connector에는 branch delete action이 없어 삭제하지 못한 운영 housekeeping HOLD로 별도 보고해야 한다.
