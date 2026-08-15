# 연구 영수증

- receipt_id: `RCPT-20260815-2131-GLOBAL-SOP71-EXPRESSION`
- date_time: `2026-08-15T21:31+09:00`
- researcher: `ChatGPT`
- work_id: `GLOBAL`
- mode: `repository maintenance / standard promotion / expression-retrieval contract audit`
- question: `Project Source의 SOP v7.1을 정식 승인 표준으로 승격하고, 독자 선행 지식·온보딩 호환성과 의미·운동 사슬 문장 경계 감사를 기존 표현 검색 계약에 손실 없이 반영할 수 있는가?`
- source_scope: `no new reference-work source-text research claim; Project Source standards + repository contracts/indexes only`
- base_sha: `89d075f0fed9f4fbdcc0d68f6a7ea0999ced99c6`
- final_sha: `f3ae024a9f6ba26e40b2c9d25858a66fbd7347ba`
- status: `complete`

## 조회한 기록

- Project Source `REFERENCE_RESEARCH_ANALYSIS_SOP_v7.1.md`
- Project Source `REFERENCE_RESEARCH_REPOSITORY_CONTRACT_v1.md`
- Project Source `REFERENCE_WORK_MODEL_SCHEMA_v2.md`
- `REPOSITORY_MANIFEST.yaml`
- `REFERENCE_RESEARCH_STANDARD_SOURCE_LOCK_v1.yaml`
- `REFERENCE_RESEARCH_REPOSITORY_CONTRACT_v1.3_PROJECT_SOURCE_ADDENDUM.md`
- `indexes/expression_retrieval.md`
- `indexes/prose_realization_retrieval.md`
- `indexes/recent_receipts.md`
- current `main` HEAD

## 표준 원문 확인

세 Project Source 파일을 직접 읽고 원본 바이트 기준 SHA-256·크기를 재계산했다.

- SOP v7.1: `3803ff35ff9d68211aa2ab655b76dd387567f441a424f41e2a8e5884722fe8c5` / `120486` bytes
- Repository Contract v1: `8a6479621af6d1196433ca5760ae727eb5ccc1b876dea468df3faafc964e304e` / `12579` bytes
- Work Model Schema v2: `1e6f5188749130900349cc7f54a9c07f888946d912485124fe45c7b4f50563f8` / `19277` bytes

SOP v7.1에서 직접 확인한 신규 승인 보정은 다음이다.

- 표현 호환성에 reader prior knowledge / onboarding 상태를 포함한다.
- first introduction / re-onboarding과 callback/payoff 압축을 같은 표면 선택으로 일반화하지 않는다.
- `serial_position`은 보조 좌표이며 회차 번호를 기계적 우선순위로 사용하지 않는다.
- 문장 경계는 단문 수가 아니라 `관찰 → 예상 → 조정 → 결과`, `동작 시작 → 힘 전달 → 결과` 같은 의미·운동 사슬 기능으로 감사한다.
- 발견·판정·전환·화말의 기능적 독립 단문은 보존하고, 단문 감소를 위해 서로 다른 사고를 강제로 합치지 않는다.

## 작품 모델 갱신

- CHARACTER: 작품별 캐릭터 정사 변경 없음.
- RELATIONSHIP: 작품별 관계 정사 변경 없음.
- EVENT: 작품별 사건 정사 변경 없음.
- STORY: 작품별 스토리 정사 변경 없음.
- PROSE: 전역 검색 계약에 reader-prior/onboarding 및 문장 경계 사슬 감사를 명시적으로 보강.
- TECHNIQUE: 새 기법 ID 없이 기존 표현 검색·재독 절차의 선택 조건만 정밀화.

## 생성·수정·폐기

### 생성
- `REFERENCE_RESEARCH_REPOSITORY_CONTRACT_v1.4_PROJECT_SOURCE_ADDENDUM.md`
- 이 연구 영수증

### 수정
- `REPOSITORY_MANIFEST.yaml`
- `REFERENCE_RESEARCH_STANDARD_SOURCE_LOCK_v1.yaml`
- `indexes/expression_retrieval.md`
- `indexes/prose_realization_retrieval.md`
- `indexes/recent_receipts.md` (영수증 인덱스 봉인 단계)

### 신규 연구 ID
- 없음

### 스키마 변경
- 없음. `REFERENCE_WORK_MODEL_SCHEMA_v2` 유지.
- 새 영구 회차 DB 없음.
- 새 연구층 없음.
- Schema v3 없음.

### 폐기·강등
- 없음. v1.3 addendum은 역사 기록으로 보존하고 manifest만 현행 v1.4를 가리킨다.

## 반례·보류

- `1화는 1화만 참고`, `초반 회차 우선` 같은 수치 규칙은 채택하지 않았다.
- 단문 개수 감소를 품질 목표로 채택하지 않았다.
- 서로 다른 사고를 장문으로 합치는 방식도 교정 규칙으로 채택하지 않았다.
- Project Source 세 파일 무결성 검증이 모두 통과해 `HOLD_STANDARD_SOURCE`는 해제되었다.

## 감사 결과

- BASE 대비 연구 내용 diff: 5 files / additions only in retrieval contracts / standard pointer replacement in lock·manifest / new v1.4 addendum.
- 기존 expression/prose 검색 계약 본문 삭제 없음.
- first introduction vs callback, setup vs payoff, reader prior knowledge, onboarding load가 임시 envelope 조건으로 명시됨.
- `serial_position`은 보조 좌표로 명시됨.
- 문장 경계 감사가 단문 수가 아닌 의미·운동 사슬 기준으로 명시됨.
- 기능적 독립 단문 보존 및 강제 장문화 금지 확인.
- 새 DB·새 연구층·Schema v3 생성 없음.
- 커밋 직전 원격 `main` HEAD 재확인: `89d075f0fed9f4fbdcc0d68f6a7ea0999ced99c6`, BASE와 동일.

## 변경 파일

- `REFERENCE_RESEARCH_REPOSITORY_CONTRACT_v1.4_PROJECT_SOURCE_ADDENDUM.md`
- `REPOSITORY_MANIFEST.yaml`
- `REFERENCE_RESEARCH_STANDARD_SOURCE_LOCK_v1.yaml`
- `indexes/expression_retrieval.md`
- `indexes/prose_realization_retrieval.md`
- `audits/RCPT-20260815-2131-GLOBAL-SOP71-EXPRESSION.md`
- `indexes/recent_receipts.md`

## 다음 질문

정본 승격 완료 뒤 현재 수정 원고 「제1화. 낡은 망치가 길을 열었다」와 참고작 1화 원문을 직접 대조하여, 문장 수가 아니라 `대사 덩어리 길이 / 지문 개입 위치 / 설명 확대·압축 / 문단 밀도 / 회차 전체 표현 파형`이 장면 역할과 독자 선행 지식에 따라 어떻게 변하는지 검증한다.
