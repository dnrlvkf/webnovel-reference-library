# GLOBAL 연구 영수증

- receipt_id: `RCPT-20260815-2209-GLOBAL-SOURCE-REENTRY`
- date_time: `2026-08-15T22:09:00+09:00`
- work_id: `GLOBAL`
- mode: `repository maintenance / expression source-reentry contract audit`
- question: `참고작 연구층을 최대한 보존하면서도 파생 요약이 실제 원문의 어휘·문법·문장 호흡·회차 표현 파형을 대신해 기계적인 산문을 생성하는 손실 압축 경로를 어떻게 차단할 것인가`
- source_scope: `no new source-text research claim; Project Source standards + current repository contracts/indexes + recent REF-47 expression failure audit`
- base_sha: `ac25336e6be91fbd959bed3cc157d15ae88fe41f`
- branch: `research/global-source-reentry-contract-20260815`
- research_content_sha: `cb8e758ad494e312baad098405d3764fdd3df598`
- final_sha: `406113e663379ad2aa8ea841e592978ffda75bdd`
- final_sha_mode: `self_excluding_receipt_finalization`
- remote_status: `ready_for_main_reflection`
- status: `complete`

## 표준 검증
- Project Source `REFERENCE_RESEARCH_ANALYSIS_SOP_v7.1.md` SHA-256 `3803ff35ff9d68211aa2ab655b76dd387567f441a424f41e2a8e5884722fe8c5`, 120486 bytes 직접 재검증.
- Project Source `REFERENCE_RESEARCH_REPOSITORY_CONTRACT_v1.md` SHA-256 `8a6479621af6d1196433ca5760ae727eb5ccc1b876dea468df3faafc964e304e`, 12579 bytes 직접 재검증.
- Project Source `REFERENCE_WORK_MODEL_SCHEMA_v2.md` SHA-256 `1e6f5188749130900349cc7f54a9c07f888946d912485124fe45c7b4f50563f8`, 19277 bytes 직접 재검증.
- GitHub standard source lock과 파일명·SHA-256·바이트 크기 일치.

## 조회한 기록
- `REPOSITORY_MANIFEST.yaml`
- `REFERENCE_RESEARCH_STANDARD_SOURCE_LOCK_v1.yaml`
- `REFERENCE_RESEARCH_REPOSITORY_CONTRACT_v1.4_PROJECT_SOURCE_ADDENDUM.md`
- `README.md`
- `AGENTS.md`
- `indexes/expression_retrieval.md`
- `indexes/prose_realization_retrieval.md`
- `indexes/recent_receipts.md`
- 최근 `RCPT-20260815-2151-REF47`

## 문제 확인
- 기존 계약은 PSE/Source Scene을 추출 단위로 제한하고 회차 전체 재독까지 요구하고 있었다.
- 그러나 `episode_context_envelope`와 임시 표현 패킷으로 다시 선택 이유를 압축한 뒤 참고작을 닫고 새 문장을 생성하는 경로가 남아 있었다.
- 이 경로에서는 원문에 있던 어휘 결합, 절 연결, 주어 생략, 종결, 중·장문과 단문의 배열, 대사·지문·효과음·UI의 회차 내 교대가 다시 추상 원리로 축소될 수 있다.
- 최근 REF-47 기반 샘플 개작에서 이러한 손실 압축이 실제로 `짧은 화면 블록 → 짧은 문장`, `의미 사슬 → 체크리스트식 독립 단문`으로 회귀한 사례를 확인했다.

## 변경
- `REFERENCE_RESEARCH_REPOSITORY_CONTRACT_v1.4_PROJECT_SOURCE_ADDENDUM.md`
  - `집필 직전 원문 재진입 권한` 신설.
  - 파생 연구층을 검색 좌표로 한정하고, 표현 생성 전 실제 원문 회차 전체 직접 재독을 요구.
  - 한 REF·한 회차로 기본 표현법을 확정하지 못하게 하고 복수 회차·필요 시 복수 REF를 작품별 독립 재독 후 비교하도록 보정.
  - 복수 사례 수를 고정 할당량으로 만들지 않고 선택 폭·반례 확보를 기준으로 중단.
  - 임시 패킷을 원문 재독 종료용 실행 컴파일본으로 사용하는 경로를 금지.
  - `사고 단위 ≠ 문장 단위 ≠ 문단 단위 ≠ 화면 블록`을 명시.
- `AGENTS.md`
  - 집필 작업 진입점에서 동일 권한을 즉시 적용하도록 강화.
  - 이유 없는 연속 단문화와 파생 요약 기반 산문 생성 감사를 추가.
- `README.md`
  - 라이브러리의 집필 역할을 `실행 규칙 공급`이 아니라 `원문 재진입 좌표 공급`으로 명확화.
  - 집필 직전 원문 회차·native anchor 동시 참조와 복수 회차/복수 REF 독립 재독 원칙을 반영.
- `indexes/recent_receipts.md`
  - 본 감사 영수증과 연구 내용 SHA를 최근 인덱스에 추가.

## 변경하지 않은 것
- SOP v7.1 승인 원문은 수정하지 않음.
- Repository Contract v1 승인 원문은 수정하지 않음.
- Work Model Schema v2는 수정하지 않음.
- `REPOSITORY_MANIFEST.yaml` 경로·schema_version은 유지.
- PSE/PVAR/PROSE/Source Scene/Macro/Micro/TH 기존 ID·파일 구조는 유지.
- 새 DB, 새 영구 표현층, Schema v3는 만들지 않음.
- 기존 작품별 연구 기록은 일괄 이관하지 않음.

## 여섯 트랙 영향
- CHARACTER: 변경 없음. 표현 시 캐릭터 판단을 파생 요약만으로 복원하지 않고 원문/native anchor와 함께 보게 함.
- RELATIONSHIP: 변경 없음. 대사 권리·호칭 표면은 원문 회차 재독에서 확인하도록 강화.
- EVENT: 변경 없음.
- STORY: 변경 없음. 회차 전체 제시 파형을 표현 판단에 유지하도록 강화.
- PROSE: 집필 검색 권한 변경. 파생층은 검색 좌표, 실제 표현 판단은 현재 실행에서 직접 재독한 원문 회차 + 대상 작품 native anchor.
- TECHNIQUE: Macro/Micro/TH를 실행 문장 생성기로 사용하지 않는 기존 원칙을 강화.

## 반례·보류
- `복수 REF를 많이 읽을수록 품질이 오른다`: 채택하지 않음. 고정 할당량과 무한 수집을 금지하고 선택 폭·반례 확보를 종료 기준으로 둠.
- `모든 집필에서 복수 REF가 필수다`: 채택하지 않음. 특정 작품의 좁은 콜백/정사 연속성 작업은 native anchor와 해당 원문이 우선할 수 있음. 다만 외부 참고에서 일반 표현 결론을 만들 때 한 REF·한 회차로 확정하지 않음.
- `긴 문장이 좋다` 또는 `짧은 문장이 나쁘다`: CONTRADICTED. 문장 경계는 의미·운동 사슬과 회차 내 위치로 판정.

## 감사 결과
- 기존 구조를 폐기하지 않고 권한만 교정하는 최소 변경.
- 새 스키마 없이 현행 v1.4 부속서와 루트 진입점으로 집필 경로를 교정.
- 표면 복제 방화벽은 유지하면서 추상화 손실 방화벽을 추가.
- 원문을 직접 읽지 못한 후보는 특정 작품 표현 근거로 보고할 수 없도록 fail-closed.
- recent receipt index seal SHA: `406113e663379ad2aa8ea841e592978ffda75bdd`.

## 다음 질문
새 계약을 적용해 현재 오리지널 1화를 다시 샘플 개작할 때, 복수 작품·복수 회차의 실제 문장 호흡과 표현 채널 파형을 유지한 상태에서 기존의 연속 단문 회귀가 실제로 감소하는지 검증한다.
