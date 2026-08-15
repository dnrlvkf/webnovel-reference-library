# REFERENCE_RESEARCH_REPOSITORY_CONTRACT_v1.4_PROJECT_SOURCE_ADDENDUM

> v1.3의 프로젝트 소스 정본 운용과 PROSE 저수준 증거층(PSE/PVAR)을 유지하면서 분석 SOP v7.1의 독자 선행 지식·온보딩 호환성, 문장 경계 사슬 감사, 집필 직전 원문 재진입 권한을 현행 승인 표준으로 승격한다.

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

## 집필 직전 원문 재진입 권한

표현 품질이 필요한 집필·개작에서 파생 연구층은 **검색 좌표**이며 원문을 대신하는 실행 원천이 아니다.

- `PROSE`, `PSE`, `PVAR`, Source Scene, Macro, Micro, TH, 표현 facet, `episode_context_envelope`, 임시 표현 패킷은 관련 원문을 다시 찾기 위한 좌표·비교 메모로 사용한다.
- 파생 기록의 `작동 원리`, `전개 구조`, `선택 이유`, `사용 가능한 판단`만 읽고 곧바로 문장·대사·지문을 생성하지 않는다. 이 경로는 원문의 어휘 결합·절 연결·주어 생략·종결·문장 길이 분포·대사/지문/효과음 교대·회차 파형을 손실할 수 있다.
- 표현 생성 또는 표현 개작 전에, 실제로 사용할 후보의 **원문 회차 전체를 직접 재독**한다. 후보의 선택이 전후 회차의 선행 제시·관계 축적·회수와 결합하면 필요한 인접 회차까지 확장한다.
- 한 REF의 한 회차만으로 작품의 기본 표현법이나 현재 장면의 정답 표면을 확정하지 않는다. 현재 문제와 가까운 **복수 회차**에서 변형·예외·복귀를 확인하고, 다른 REF를 함께 사용할 때는 각 작품을 먼저 독립적으로 원문 재독한 뒤 비교한다.
- 복수 REF·복수 회차는 고정 할당량이 아니다. 같은 표면만 반복 확인되면 추가 수집을 중단하고 다른 실현·반례·장면 조건을 찾는다. 현재 문제의 선택 폭과 경계가 확보되면 더 읽는 양을 연구 성과로 간주하지 않는다.
- 회차 전체 독해는 `대사 / 지문 / 내면 / 설명 / 행동 / 효과음 / UI / 문단 / 문장`을 분리 목록으로 세는 작업이 아니다. 한 회차에서 이 채널들이 어떤 순서와 밀도로 교대하고, 각 채널 안에서 실제 어휘·문법·생략·절 결합·문장 경계가 어떻게 달라지는지 함께 본다.
- 특히 `사고 단위`, `문장 단위`, `문단 단위`, `화면 블록`을 동일시하지 않는다. 짧은 화면 문단을 짧은 문장 규칙으로, 의미 사슬을 여러 독립 단문으로 자동 변환하지 않는다.
- 집필 직전 임시 패킷은 원문 좌표·호환성·불일치 경계·주의사항을 좁히는 용도다. **패킷의 추상 요약만 남기고 원문을 닫은 뒤 그 요약에서 산문을 복원하는 방식은 금지한다.** 실제 초고 판단 시에는 이번 실행에서 직접 재독한 원문 회차와 대상 작품 native anchor의 표면 운용을 함께 참조한다.
- 참고작 원문의 고유 문장·말버릇·고유명·사건 배열을 복제하지 않는다. 원문을 직접 재독하는 목적은 표면 복사가 아니라, 추상화 과정에서 사라지는 선택 폭과 한국어 결속을 잃지 않은 상태에서 대상 작품의 새 표현을 선택하기 위함이다.
- 원문을 직접 확인할 수 없는 후보는 `원문 재독 완료`로 취급하지 않으며, 특정 작품의 실제 표현을 근거로 한 산문 선택이라고 보고하지 않는다.

이 절은 `indexes/expression_retrieval.md`와 `indexes/prose_realization_retrieval.md`의 임시 패킷·참고작 종료 문구보다 우선한다. 두 인덱스의 패킷은 원문 재진입을 종료시키는 컴파일본이 아니라 재독 범위를 좁히는 검색 메모로 해석한다.

## 검색 라우팅

검색 라우팅은 `REPOSITORY_MANIFEST.yaml`의 현행 경로를 따른다.

- Source Scene을 집필 검색에 사용할 때는 `indexes/scene_retrieval_contract.md`를 먼저 적용한다. 실제 결합 사슬은 `observed_chain`이며 `recommended_chain`이 아니다. 장면 전체 일치를 요구하지 않고 부분 문제·불일치 경계·사용 가능한 판단·가져오지 말아야 할 요소를 분리한다.
- 장면 전체의 표현·POV·대사·정보 공개 문제는 `indexes/expression_retrieval.md`를 사용한다.
- 문장·지문·문단의 실제 실현 선택이 문제일 때는 `indexes/prose_realization_retrieval.md`에서 PVAR → PSE → source scene 순으로 재진입한다.
- 표현 생성 단계에서는 위 검색 결과를 종착점으로 쓰지 않고, 본 부속서의 `집필 직전 원문 재진입 권한`에 따라 실제 원문 회차로 다시 내려간다.

세 인덱스는 서로 대체 관계가 아니다. Source Scene의 관찰된 beat 수·순서·질문권·명령권·침묵·효과음 조합을 현행 집필 템플릿이나 자동 발동 규칙으로 해석하지 않는다.

## 정본 역할

- 프로젝트 소스: SOP·저장소 계약·작품 모델 스키마의 승인 원문
- GitHub `main`: 연구 기록·작품 모델·PSE·PVAR·원천 좌표·TH·인덱스·감사·영수증·커밋 상태
- GitHub 잠금 파일: 프로젝트 소스 표준의 무결성과 적용 버전
- 파생 연구층: 집필 시 원문 재독 위치와 비교 질문을 제공하는 검색·검증 좌표
- 실제 표현 판단: 현재 실행에서 직접 재독한 참고작 원문 회차 + 대상 작품 native anchor

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
