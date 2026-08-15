# AUD-20260815-PROSE-REALIZATION-SCHEMA · PSE/PVAR 스키마 확장 및 표준 승격 감사

- date_time: `2026-08-15T17:42:00+09:00`
- operation: `global schema audit / project-source standard promotion`
- question: `기존 PROSE가 실제 산문 실현 선택을 너무 빨리 추상화해 잃는 문제를 PSE/PVAR로 보존하되 새 문형 DB로 퇴행하지 않게 최소 확장할 수 있는가`
- base_sha: `920eb0d17a174400347da64f0813e202a01b302d`
- branch: `ops/promote-prose-realization-v7-20260815`
- status: `prepared_for_merge`

## 프로젝트 소스 직접 확인

프로젝트 소스에 추가된 승인 후보를 직접 읽고 바이트 기준으로 검증했다.

- `REFERENCE_RESEARCH_ANALYSIS_SOP_v7.md`
  - sha256: `21e870fe54e307ff826d0d030eb23904a4ad307dc60e05234de33fa95b046d88`
  - size_bytes: `116100`
- `REFERENCE_WORK_MODEL_SCHEMA_v2.md`
  - sha256: `8ed80e0684ab5fb2908004a7242548fdaac9dd02724f0456429cb68a8c44d7c4`
  - size_bytes: `19275`
- `REFERENCE_RESEARCH_REPOSITORY_CONTRACT_v1.md`
  - sha256: `8a6479621af6d1196433ca5760ae727eb5ccc1b876dea468df3faafc964e304e`
  - size_bytes: `12579`

## 조회한 기존 기록

- `REPOSITORY_MANIFEST.yaml`
- `REFERENCE_RESEARCH_STANDARD_SOURCE_LOCK_v1.yaml`
- `REFERENCE_RESEARCH_REPOSITORY_CONTRACT_v1.2_PROJECT_SOURCE_ADDENDUM.md`
- `REFERENCE_RESEARCH_ANONYMITY_CONTRACT_v1.md`
- `AGENTS.md`
- `README.md`
- `indexes/expression_retrieval.md`
- `audits/AUD-20260807-EXPRESSION-RETRIEVAL.md`
- `audits/AUD-20260808-WRITING-RETRIEVAL-VOICE-GATE.md`
- `works/REF-02/prose/PRO-REF02-0001.md`
- `works/REF-02/source_scenes/SOURCE-SCENES-REF02-0001-0004.md`
- 최근 연구 영수증 인덱스

## 이전 감사와의 관계

2026-08-07 감사는 당시 문제를 검색 라우팅 부족으로 판정해 새 표현 연구층을 만들지 않았다. 동시에 실제 A/B 테스트에서 검색 실패가 반복되고 구조적 필드 부족이 확인될 경우 스키마 확장을 재검토하도록 남겼다.

2026-08-08 감사는 대상 작품 native anchor와 POV·거리 호환성 게이트, 임시 장면 패킷을 추가했으나 기존 PROSE·Macro·Micro·TH 구조는 유지했다.

이후 프로젝트 측 장기 집필·재작성 테스트에서 다음 퇴행이 형태를 바꿔 반복되었다.

`자동 행동 지문 → 자동 판단문 → 문단 과분절 → 문장 결속 후 과밀 문단 → 다양성을 위한 기계적 시제·어미 섞기`

기존 PROSE는 장면 조건과 기능을 설명하지만, 같은 기능을 서로 다른 조사·부사·시제·양태·종결·문장 경계·문단 경계로 실현한 원문 사례들을 저수준에서 대조하기 어렵다. Source scene은 원문 재진입 좌표를 보존하지만 해당 차이를 검색 단위로 비교하지 않고, Micro는 모든 평범한 산문 선택을 저장하기에 의도적으로 너무 예외적이다.

## 스키마 변경 조건 판정

저장소 계약의 스키마 변경 조건을 다음과 같이 판정한다.

1. **기존 구조에서 실제 근거 손실:** PASS — PROSE 요약에서 저수준 문법·문장·문단 선택이 소실됨.
2. **기존 필드 확장으로 해결 불가:** PASS — PRO 파일 하나에 수십·수백 연속 구간을 넣으면 비교와 재진입이 무너짐.
3. **검색·검증·집필 활용 가치:** PASS — 같은 기능의 다른 실현을 원문으로 다시 읽어 자동 문형 회귀를 검증할 수 있음.
4. **기존 기록 이관 방안:** PASS — 일괄 이관하지 않고 기존 PRO/Macro/Micro/TH를 유지하며 새 연구에서 필요할 때만 PSE/PVAR를 생성함.
5. **매니페스트·스키마 동시 갱신:** PASS — manifest 1.5, SOP v7, work-model schema v2, project-source addendum v1.3을 같은 승격 단위로 변경함.
6. **감사·영수증:** PASS — 본 감사와 글로벌 승격 영수증을 남김.

## 승인 구조

기존 `works/REF-XX/prose/` 아래에만 확장한다.

- `PRO-*`: 기존 문체 누적 모델 유지
- `prose/evidence/PSE-*`: 산문 실현 증거
- `prose/variations/PVAR-*`: 동일/유사 기능의 변형 비교

새 최상위 표현 트랙, 기법 ID 체계, 추천 문형 DB, 영구 태그 DB는 만들지 않는다.

## 검색 라우팅

- 장면 전체 표현·POV·대사·정보 공개: 기존 `indexes/expression_retrieval.md`
- 문장·지문·문단 실제 실현: 신규 `indexes/prose_realization_retrieval.md`
- 산문 실현 검색은 `PVAR → 서로 다른 PSE → source scene → 원문`을 기본 재진입 순서로 한다.
- 대상 작품 native anchor는 모든 외부 표현 참고보다 우선한다.

## 실패 방지

다음을 새 규칙으로 금지한다.

- `판단 유보 = -지만 + -니까`
- `~다 반복 회피 = 현재형 섞기`
- 접속 어미 순환으로 표면 다양성 만들기
- 문단 글자 수·모바일 줄 수 고정 임계값
- 모든 문단의 PSE 등록
- PVAR를 추천 문형 목록으로 사용

## 익명성 감사

- 신규 일반 파일에 실제 작품명·저자명·인물명·조직명·기술명 없음
- 프로젝트 테스트의 원문·샘플 문장을 저장소 규칙으로 복사하지 않음
- PSE/PVAR도 정확 표면은 source 좌표 재독을 원칙으로 함

## 이관 판정

기존 PROSE·Macro·Micro·TH는 수정·이관하지 않는다. 기존 자료에서 저수준 선택을 다시 연구해야 할 때만 원문 재독 뒤 PSE/PVAR를 신규 생성한다. 자동 백필은 금지한다.

## 변경 파일

- `REFERENCE_RESEARCH_STANDARD_SOURCE_LOCK_v1.yaml`
- `REPOSITORY_MANIFEST.yaml`
- `REFERENCE_RESEARCH_REPOSITORY_CONTRACT_v1.3_PROJECT_SOURCE_ADDENDUM.md`
- `AGENTS.md`
- `README.md`
- `indexes/prose_realization_retrieval.md`
- `audits/AUD-20260815-PROSE-REALIZATION-SCHEMA.md`
- `audits/RCPT-20260815-1742-GLOBAL-PROSE-SCHEMA.md`
- `indexes/recent_receipts.md`

## 판정

`PASS_FOR_MERGE`

이번 변경은 표현 자료를 더 많이 저장하기 위한 확장이 아니라, 기존 PROSE와 원문 사이에서 반복적으로 손실된 `의미 단위 → 실제 산문 실현 → 작품 내부 변형`을 재검증 가능하게 만드는 최소 하위층 확장이다.
