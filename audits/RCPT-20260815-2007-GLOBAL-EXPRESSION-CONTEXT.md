# GLOBAL 연구 영수증 — expression retrieval episode context

- receipt_id: `RCPT-20260815-2007-GLOBAL-EXPRESSION-CONTEXT`
- date_time: `2026-08-15T20:07:00+09:00`
- researcher: `ChatGPT`
- work_id: `GLOBAL / REF-47 pilot basis`
- mode: `구간 정밀 분석 / expression-retrieval context audit`
- question: `문장·지문·문단의 국소 실현을 참고할 때 해당 회차 전체를 먼저 읽어야 압축·확대 선택 조건을 복원하고 단문화·과현장화 과교정을 줄일 수 있는가`
- source_scope: `REF-47 / SRC-DIRECT-001 / ep256 full episode / lines 136725-137318 / normalized sha256 f6635b42c4eb00612ebdf3267e9aef66f3dce5f8d91dad4251fc2f99c50f5466; SC-REF47-0007 local range reverified`
- base_sha: `082c065bc4068c335242793fa080354a4a41f878`
- branch: `research/expression-episode-context-20260815`
- research_content_sha: `db154cbb1b6133036ea84c2a99d9fc065a55bf01`
- final_sha: `5105d41ab3ceb27849dc6a463396bb635c1a39cf`
- final_sha_mode: `self_excluding_receipt_and_index_finalization`
- remote_status: `verified_on_main`
- status: `complete`

## 조회한 기록

- `REPOSITORY_MANIFEST.yaml`
- `REFERENCE_RESEARCH_STANDARD_SOURCE_LOCK_v1.yaml`
- project-source `REFERENCE_RESEARCH_ANALYSIS_SOP_v7.md`
- project-source `REFERENCE_RESEARCH_REPOSITORY_CONTRACT_v1.md`
- project-source `REFERENCE_WORK_MODEL_SCHEMA_v2.md`
- `REFERENCE_RESEARCH_REPOSITORY_CONTRACT_v1.3_PROJECT_SOURCE_ADDENDUM.md`
- `indexes/scene_retrieval_contract.md`
- `indexes/expression_retrieval.md`
- `indexes/prose_realization_retrieval.md`
- `works/REF-47/source_registry/SOURCE-BRIDGE-REF47.md`
- `works/REF-47/prose/evidence/PSE-REF47-0007.md`
- `works/REF-47/prose/variations/PVAR-REF47-0004.md`
- `audits/RCPT-20260815-1911-GLOBAL-SCENE-RETRIEVAL.md`
- REF-47 `SRC-DIRECT-001` ep256 전체 원문

## 표준 검증

프로젝트 소스 표준 3종을 잠금 파일과 대조했다.

- `REFERENCE_RESEARCH_ANALYSIS_SOP_v7.md`: SHA-256 `21e870fe54e307ff826d0d030eb23904a4ad307dc60e05234de33fa95b046d88`, 116100 bytes, 일치
- `REFERENCE_RESEARCH_REPOSITORY_CONTRACT_v1.md`: SHA-256 `8a6479621af6d1196433ca5760ae727eb5ccc1b876dea468df3faafc964e304e`, 12579 bytes, 일치
- `REFERENCE_WORK_MODEL_SCHEMA_v2.md`: SHA-256 `8ed80e0684ab5fb2908004a7242548fdaac9dd02724f0456429cb68a8c44d7c4`, 19275 bytes, 일치
- manifest의 `standard_source: project_source`, current addendum, canonical branch `main` 확인

## 원문 확인

- `SRC-DIRECT-001` 원본 SHA-256: `95d22f155d582ec702142b906161f4b36241627a76cdf858ff9b39cd6d686a4e`
- raw byte size: `5927798`
- raw encoding: `UTF-16`
- ep256 boundary: 136725행 header부터 137318행까지, 다음 ep257 header는 137319행
- ep256 normalized full-episode SHA-256: `f6635b42c4eb00612ebdf3267e9aef66f3dce5f8d91dad4251fc2f99c50f5466`
- 기존 `SC-REF47-0007`은 ep256 후반 국소 실현 증거로 재확인

## 작품 모델 갱신

- CHARACTER: 새 작품 정사 판정 없음. 표현 검색 시 국소 반응 형식보다 현재 인물의 판단 기준과 native anchor를 우선하는 기존 원칙 유지.
- RELATIONSHIP: 새 권리 판정 없음. Source Scene의 질문권·답변권을 대상 작품에 자동 이식하지 않는 기존 경계 유지.
- EVENT: 새 사건 모델 없음. 회차 전체 독해는 사건 추가가 아니라 표현 선택의 선행 제시량·전환 압력 확인에 사용.
- STORY: SUPPORTED — 같은 국소 표현도 회차 내 위치와 선행 제시량에 따라 압축·확대 이유가 달라질 수 있으므로 표현 선택 전에 회차 배열을 확인해야 함.
- PROSE: SUPPORTED — PSE/Source Scene 범위는 추출 단위이고 기본 독해 단위로는 부족함. ep256 전체 재독에서 후반 감각 단서의 압축이 회차 앞부분의 충분한 선행 제시와 결합되어 있음을 확인. `회차 전체 → 장면 블록 → 문단 → 문장 → 절/단어` 순으로 내려가는 검색을 두 인덱스에 반영.
- TECHNIQUE: 새 Source Scene·Macro·Micro·TH·PSE·PVAR 없음. `episode_context_envelope`는 영구 연구층이 아닌 집필/비교 직전 임시 독해 메모로 제한.

## 생성·수정·폐기

- 수정: `indexes/expression_retrieval.md`
  - `읽기는 크게, 추출은 작게` 명시
  - 표현 후보는 회차 전체 재독 후 국소 장면으로 내려가도록 순서 변경
  - 임시 `episode_context_envelope` 추가
  - 단문화·과현장화·선행 제시량 오판 감사 추가
- 수정: `indexes/prose_realization_retrieval.md`
  - PSE/Source Scene 저장 범위를 추출 단위로 재정의
  - 기존 `앞뒤 2~3문단` 기본 창을 `회차 전체 → 장면 블록 → 앞뒤 문단`으로 확장
  - `회차 맥락과 산문 파형` 비교축 추가
  - PVAR 선택 조건에 회차 역할·선행 제시량·압축/확대 위치 추가
- 신규 연구 ID·TH·Macro·Micro·PSE·PVAR: 없음
- schema v3 / 새 영구 episode record type: 생성하지 않음

## 반례·보류

- CONTRADICTED: `PSE 주변 2~3문단이면 산문 실현 선택 조건을 기본적으로 충분히 판정할 수 있다.`
- CONTRADICTED: `더 디테일한 표현 참고는 더 많은 단문·행동 비트·현장화를 뜻한다.`
- SUPPORTED: `같은 국소 압축이라도 앞 장면에서 이미 독자에게 충분히 경험시킨 정보인지 여부를 확인해야 한다.`
- SUPPORTED: `회차 전체를 읽고도 저장은 필요한 PSE/Source Scene/판단만 작게 유지할 수 있다.`
- HOLD: 영구 회차 연구층, 새 episode ID 체계, schema v3. 다른 REF에서도 같은 검색 실패가 반복되는지 추가 검증 전에는 확장하지 않음.

## 감사 결과

- `main` 재확인 시 BASE SHA와 동일하여 stale-base 충돌 없음.
- 변경은 전역 표현 검색 계약 두 파일에만 한정하고 기존 Source Scene 비강제 계약을 보존함.
- 실제 작품명·인물명·원문 문장을 신규 정본 규칙에 복사하지 않음.
- 회차 전체 독해를 새 요약 DB 생성으로 전환하지 않음.
- `episode_context_envelope`는 임시 컴파일/독해 메모로 명시해 스키마 확장 조건을 우회하지 않음.
- 기존 native anchor 우선, 표면 모방 금지, 대표/대비/실패 비교 원칙 유지.
- REF-47 ep256 전체 재독으로 국소 PSE만 읽었을 때 놓치는 선행 제시량과 산문 파형 조건을 실제 검증함.
- diff 감사 중 기존 REF-02 영수증 한 행의 우발 변경을 발견해 PR 전 원상복구함.
- PR #32 변경 파일 4개만 확인하고 병합함.
- research merge SHA: `5105d41ab3ceb27849dc6a463396bb635c1a39cf`.

## 변경 파일

- `indexes/expression_retrieval.md`
- `indexes/prose_realization_retrieval.md`
- `audits/RCPT-20260815-2007-GLOBAL-EXPRESSION-CONTEXT.md`
- `indexes/recent_receipts.md`

## 다음 질문

1. 다른 REF의 표현 후보 1~2개에서도 회차 전체 재독이 국소 선택 조건 판정을 실제로 바꾸는가.
2. 새 계약으로 현재 작품의 한 회차를 다시 다듬을 때 단문화·과현장화가 줄고 장면 연결·문장군 리듬이 개선되는가.
3. 반복 검증 후에도 현재 임시 envelope로 부족할 때만 스키마 확장을 재검토한다.
