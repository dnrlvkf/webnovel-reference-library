# REFERENCE_RESEARCH_REPOSITORY_CONTRACT_v1.4_PROJECT_SOURCE_ADDENDUM

> v1.3의 프로젝트 소스 정본 운용과 PROSE 저수준 증거층(PSE/PVAR)을 유지하면서 분석 SOP v7.1의 독자 선행 지식·온보딩 호환성과 문장 경계 사슬 감사를 현행 승인 표준으로 승격한다.

## 적용 관계

이 문서는 `REFERENCE_RESEARCH_REPOSITORY_CONTRACT_v1.md`와 함께 적용한다. 연구 표준 문서의 저장 위치·무결성 검증·필수 루트 파일·승인 표준 버전에 관해서는 이 부속서가 우선한다.

루트에 남아 있는 `REFERENCE_RESEARCH_REPOSITORY_CONTRACT_v1.1_PROJECT_SOURCE_ADDENDUM.md`, `v1.2_PROJECT_SOURCE_ADDENDUM.md`, `v1.3_PROJECT_SOURCE_ADDENDUM.md`는 역사적 호환 기록이며 현행 운영 권위를 갖지 않는다. 현행 적용 부속서는 `REPOSITORY_MANIFEST.yaml`의 `repository_contract_addendum_path`가 가리키는 이 문서다.

## 프로젝트 소스 정본

다음 승인 문서의 원문 바이트는 프로젝트 소스를 정본으로 삼는다.

- `REFERENCE_RESEARCH_ANALYSIS_SOP_v7.1.md`
- `REFERENCE_RESEARCH_REPOSITORY_CONTRACT_v1.md`
- `REFERENCE_WORK_MODEL_SCHEMA_v2.md`

GitHub에는 동일 전문을 중복 저장하지 않아도 된다.

## 잠금 검증

`REPOSITORY_MANIFEST.yaml`은 `standard_source: project_source`와 잠금 파일 경로, 승인된 표준 파일명을 지정한다. `REFERENCE_RESEARCH_STANDARD_SOURCE_LOCK_v1.yaml`은 각 표준의 파일명·SHA-256·바이트 크기·승인 상태를 기록한다.

연구 시작 시 프로젝트 소스 원문을 직접 읽고 잠금과 대조한다. 파일명·SHA-256·바이트 크기·매니페스트 버전 중 하나라도 불일치하면 `HOLD_STANDARD_SOURCE`로 연구 쓰기와 병합을 중단한다.

## SOP v7.1 표현 호환성 보정

SOP v7.1의 표현 연구 보정은 새 영구 연구층을 만들지 않고 기존 검색·PROSE 운용 계약에 반영한다.

- 표현 호환성은 장면 기능뿐 아니라 해당 시점까지의 `reader prior knowledge`와 onboarding 상태를 함께 확인한다.
- 회차 번호와 `serial_position`은 검색 보조 좌표일 뿐 기계적 우선순위가 아니다.
- 첫 제시·재온보딩과 이미 학습된 정보의 callback/payoff 압축을 같은 표면 선택으로 일반화하지 않는다.
- 문장 경계는 단문 수가 아니라 하나의 의미·동작 사슬을 왜 끊거나 잇는지로 감사한다.
- 발견·판정·전환·화말의 기능적 독립 단문은 보존할 수 있다.
- 단문 수를 줄이기 위해 서로 다른 판단·시간·행동을 장문으로 강제 결합하지 않는다.
- 새 영구 회차 DB, 새 연구층, Schema v3는 만들지 않는다.

## PROSE 저수준 증거층

v2 스키마가 승인한 `PSE`와 `PVAR`는 새 최상위 기법 체계가 아니라 기존 `PROSE`의 하위 증거·비교층이다.

- `PSE`: 의미 단위가 실제 절·문장·지문·문단으로 실현된 선택을 원문 좌표와 함께 보존한다.
- `PVAR`: 같은 작품 안에서 동일하거나 가까운 기능을 서로 다른 표면으로 푼 PSE들을 비교한다.
- 기존 `PRO-*`, Macro, Micro, TH는 유지한다.
- 기존 PROSE 기록의 일괄 이관은 하지 않는다. 새 연구에서 저수준 선택 손실이 확인될 때만 PSE/PVAR를 생성한다.
- PSE/PVAR를 추천 어미·문형·모바일 글자 수 규칙 DB로 사용하지 않는다.

## 검색 라우팅

검색 라우팅은 `REPOSITORY_MANIFEST.yaml`의 현행 경로를 따른다.

- Source Scene을 집필 검색에 사용할 때는 `indexes/scene_retrieval_contract.md`를 먼저 적용한다. 실제 결합 사슬은 `observed_chain`이며 `recommended_chain`이 아니다. 장면 전체 일치를 요구하지 않고 부분 문제·불일치 경계·사용 가능한 판단·가져오지 말아야 할 요소를 분리한다.
- 장면 전체의 표현·POV·대사·정보 공개 문제는 `indexes/expression_retrieval.md`를 사용한다.
- 문장·지문·문단의 실제 실현 선택이 문제일 때는 `indexes/prose_realization_retrieval.md`에서 PVAR → PSE → source scene 순으로 재진입한다.

세 인덱스는 서로 대체 관계가 아니다. Source Scene의 관찰된 beat 수·순서·질문권·명령권·침묵·효과음 조합을 현행 집필 템플릿이나 자동 발동 규칙으로 해석하지 않는다.

## 정본 역할

- 프로젝트 소스: SOP·저장소 계약·작품 모델 스키마의 승인 원문
- GitHub `main`: 연구 기록·작품 모델·PSE·PVAR·원천 좌표·TH·인덱스·감사·영수증·커밋 상태
- GitHub 잠금 파일: 프로젝트 소스 표준의 무결성과 적용 버전

## 필수 루트 파일

```text
/
├─ README.md
├─ REPOSITORY_MANIFEST.yaml
├─ REFERENCE_RESEARCH_STANDARD_SOURCE_LOCK_v1.yaml
├─ REFERENCE_RESEARCH_REPOSITORY_CONTRACT_v1.4_PROJECT_SOURCE_ADDENDUM.md
├─ REFERENCE_RESEARCH_ANONYMITY_CONTRACT_v1.md
├─ registry/
├─ works/
├─ comparisons/
├─ mc_candidates/
├─ indexes/
└─ audits/
```

BASE SHA·충돌 방지·검증·영수증·커밋 규칙은 기존 저장소 계약을 그대로 따른다.
