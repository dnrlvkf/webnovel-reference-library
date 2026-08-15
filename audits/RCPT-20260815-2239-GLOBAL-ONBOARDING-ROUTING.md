# GLOBAL 연구 영수증

- receipt_id: `RCPT-20260815-2239-GLOBAL-ONBOARDING-ROUTING`
- date_time: `2026-08-15T22:39:00+09:00`
- work_id: `GLOBAL`
- mode: `repository maintenance / initial-reonboarding research routing`
- question: `성공한 참고작의 1화나 신규 온보딩 장면에서 발견한 표현을 전역 공식으로 만들지 않으면서, 각 작품의 서로 다른 첫 학습 문제와 선택 이유를 기존 여섯 트랙에 어떻게 독립적으로 누적하고 이후 비교할 것인가`
- source_scope: `no new source-text research claim; Project Source standards + current repository routing/contracts + sample-derived research question only`
- base_sha: `683826ba52dc9291a5cc695b322e6079a4848e09`
- research_content_sha: `037c61860d948fe40c55c39a41bacf7f182a1593`
- final_sha: `76b00b294a71208c87d6bc7e69ebc3974dfa2028`
- final_sha_mode: `self_excluding_receipt_finalization`
- remote_status: `ready_for_main_reflection`
- status: `complete`

## 표준 검증

- Project Source `REFERENCE_RESEARCH_ANALYSIS_SOP_v7.1.md` 직접 재독. 첫 제시·재온보딩과 이미 학습된 정보의 압축 회수를 같은 표면으로 일반화하지 않는 현행 원칙을 기준으로 삼음.
- Project Source `REFERENCE_RESEARCH_REPOSITORY_CONTRACT_v1.md` 직접 재독. 기존 파일 보강, 최소 변경, 영수증·인덱스·FINAL SHA 계약을 적용.
- Project Source `REFERENCE_WORK_MODEL_SCHEMA_v2.md` 직접 재독. STORY episode, reader information model, CHARACTER, RELATIONSHIP, EVENT, PROSE/PSE/PVAR 등 현행 필드로 목적을 충족할 수 있음을 확인.
- GitHub `REFERENCE_RESEARCH_STANDARD_SOURCE_LOCK_v1.yaml`에서 SOP v7.1 / Contract v1 / Schema v2 승인 잠금 상태 재확인.

## 조회한 기록

- `REPOSITORY_MANIFEST.yaml`
- `REFERENCE_RESEARCH_STANDARD_SOURCE_LOCK_v1.yaml`
- `REFERENCE_RESEARCH_REPOSITORY_CONTRACT_v1.4_PROJECT_SOURCE_ADDENDUM.md`
- `REFERENCE_RESEARCH_ANONYMITY_CONTRACT_v1.md`
- `AGENTS.md`
- `README.md`
- `indexes/scene_retrieval_contract.md`
- `indexes/expression_retrieval.md`
- `indexes/prose_realization_retrieval.md`
- `indexes/recent_receipts.md`
- 최근 `RCPT-20260815-2209-GLOBAL-SOURCE-REENTRY`

## 문제 확인

- 현행 SOP v7.1은 reader prior knowledge, 첫 제시/압축 회수 구분, 문장 경계 사슬 감사를 이미 지원한다.
- 현행 Schema v2는 첫 제시 연구를 기존 여섯 트랙과 PSE/PVAR에 저장할 수 있어 새 연구층이나 Schema v3가 필요하지 않다.
- 그러나 후속 연구자가 여러 성공작의 1화를 연속으로 볼 때 `좋은 1화는 X를 한다`는 전역 공식을 먼저 만들거나, 한 작품의 성공 선택을 다른 REF의 연구 질문으로 투영할 위험을 명시적으로 차단하는 전역 라우팅 진입점이 부족했다.
- 오리지널 샘플에서 확인한 문제는 전역 사실 근거가 아니며, 새 연구 질문을 발견한 실험 좌표로만 취급해야 한다.

## 변경

- `indexes/initial_onboarding_research.md` 신규.
  - `1화`를 독립 기법 유형으로 만들지 않고 작품 전체 첫 진입·신규 인물/관계/조직/공간/직업/능력/규칙·재온보딩을 같은 연구 질문군에서 다룸.
  - 각 REF에서 독자 학습 문제를 먼저 확인한 뒤 CHARACTER·RELATIONSHIP·EVENT·STORY·PROSE·TECHNIQUE로 분산 저장하도록 라우팅.
  - 첫 제시와 압축 회수의 비교, 같은 작품 내부의 후속 신규 온보딩·반례 왕복을 작품 간 비교보다 먼저 요구.
  - `캐릭터 선제시`, `사건 선제시`, `주인공 오판`, `단문`, `설명 축소` 등을 전역 집필 공식으로 컴파일하는 것을 금지.
  - 작품별 독립 근거가 성립한 뒤에만 `comparisons/`와 기존 MC/S2 절차로 넘어가도록 제한.
  - 집필 시에는 독자 학습 문제로 후보를 찾은 뒤 각 REF 원문으로 독립 재진입하고 native anchor에서 새 표현을 선택하도록 기존 source-reentry 계약과 연결.
- `REPOSITORY_MANIFEST.yaml`
  - `initial_onboarding_research_path`를 추가해 새 라우팅 계약을 안정 진입점으로 노출.
  - schema_version은 `1.6` 유지. 새 연구 스키마를 만들지 않음.
- `AGENTS.md`
  - 첫 제시·재온보딩 연구 시 라우팅 계약을 먼저 적용하고 작품별 독립 연구 후 비교하도록 루트 작업 규칙에 추가.
- `README.md`
  - 연구 시작점에 동일 라우팅을 설명하고 `좋은 1화`의 공통 문형·사건 템플릿 문서가 아님을 명시.
- `indexes/recent_receipts.md`
  - 본 영수증을 최상단에 추가하고 연구 내용 SHA `037c61860d948fe40c55c39a41bacf7f182a1593`를 연결.

## 변경하지 않은 것

- SOP v7.1 승인 원문 수정 없음.
- Repository Contract v1 승인 원문 수정 없음.
- Work Model Schema v2 수정 없음.
- v1.4 Project Source addendum 수정 없음.
- 새 DB, 새 연구 트랙, 새 Technique ID 체계, Schema v3 생성 없음.
- 기존 작품별 연구 파일을 일괄 이관하거나 재해석하지 않음.
- 오리지널 샘플의 결함·개선안을 참고작 연구 정본에 사실로 저장하지 않음.

## 여섯 트랙 영향

- CHARACTER: 첫 제시의 행동·판단을 장기 성격으로 조기 일반화하지 않고 후속 변형·복귀와 대조.
- RELATIONSHIP: 첫 대면의 질문권·거절권·거리·정보 공개를 초기 상호 분류와 후속 권리 변화로 연결.
- EVENT: 소개를 위해 사건이 멈추는지, 사건 진행 안에서 소개가 해결되는지와 실제 상태 변화를 구분.
- STORY: 독자의 첫 학습 순서, 보류 정보, 첫 보상·전환·화말을 회차 기능에 저장.
- PROSE: 첫 제시 비용과 reader prior knowledge가 시점·서술 거리·채널 배열·문장/문단 선택에 미친 조건을 추적. 필요한 경우에만 PSE/PVAR 생성.
- TECHNIQUE: 원천 장면·Macro·Micro·TH를 첫 제시 공식 태그가 아니라 여섯 트랙 선택의 재독 증거로 유지.

## 반례·보류

- `성공작 여러 편의 1화를 보면 공통 공식부터 만들 수 있다`: 채택하지 않음. 작품별 독립 연구가 선행되어야 함.
- `1화는 캐릭터를 먼저 보여줘야 한다`: 전역 규칙으로 채택하지 않음.
- `설명에는 항상 캐릭터 목소리가 강하게 들어가야 한다`: 전역 규칙으로 채택하지 않음. 중립 서술도 작품·정보 문제에 따라 조건부 선택일 수 있음.
- `주인공은 초반에 오판해야 한다`: 전역 규칙으로 채택하지 않음.
- 실제 각 REF에서 어떤 첫 제시 선택이 성공했는지는 아직 작품별 원문 연구가 필요하며 본 영수증은 그 결과를 선취하지 않는다.

## 감사 결과

- 기존 SOP/Schema가 이미 목적을 수용하므로 새 영구 연구층 대신 라우팅 계약만 추가하는 최소 변경.
- 샘플 작품의 문제를 전역 기준으로 승격하지 않도록 fail-closed 금지문을 포함.
- `1화`라는 숫자보다 첫 제시·재온보딩·압축 회수의 역할 차이를 연구하게 함.
- 작품 내부 비교가 작품 간 비교보다 우선되도록 기존 격리 원칙과 일치.
- source-reentry 계약을 유지하여 파생 연구 기록이 산문 생성기가 되지 않도록 함.
- recent receipt index seal SHA: `76b00b294a71208c87d6bc7e69ebc3974dfa2028`.

## 변경 파일

- `indexes/initial_onboarding_research.md`
- `REPOSITORY_MANIFEST.yaml`
- `AGENTS.md`
- `README.md`
- `audits/RCPT-20260815-2239-GLOBAL-ONBOARDING-ROUTING.md`
- `indexes/recent_receipts.md`

## 다음 질문

서로 다른 REF의 첫 진입을 작품별로 독립 연구할 때, 각 작품의 독자 학습 문제와 첫 제시/후속 재온보딩/압축 회수의 차이가 기존 STORY·reader information·PROSE/PSE/PVAR에 중복 없이 충분히 저장되는지 실제 배치로 검증한다.
