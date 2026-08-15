# REFERENCE_RESEARCH_REPOSITORY_CONTRACT_v1.3_PROJECT_SOURCE_ADDENDUM

> **SUPERSEDED / HISTORICAL COMPATIBILITY RECORD — NON-AUTHORITATIVE**
>
> 이 문서는 SOP v7 / Schema v2 / PSE·PVAR 승격 시점의 역사 기록이다. 현재 연구·집필·부트스트랩 지침으로 사용하지 않는다. **현행 적용 부속서는 오직 `REPOSITORY_MANIFEST.yaml`의 `repository_contract_addendum_path`가 가리키는 문서다.** 이 역사 파일 안의 SOP·Schema·필수 루트 경로·검색 라우팅·당시 적용 버전 표기는 모두 과거 상태 기록이며 현재 권위를 갖지 않는다.

> v1.2의 프로젝트 소스 정본 운용을 유지하면서 분석 SOP v7과 작품 모델 스키마 v2, PROSE 저수준 증거층(PSE/PVAR)을 정본 표준으로 승격했던 시점의 기록.

## 적용 관계

이 문서는 당시 `REFERENCE_RESEARCH_REPOSITORY_CONTRACT_v1.md`와 함께 적용되었다. 연구 표준 문서의 저장 위치·무결성 검증·필수 루트 파일·승인 표준 버전에 관한 아래 내용은 역사적 상태 기록이며, 현재 권위 판정에는 사용하지 않는다.

루트에 남아 있는 v1.1·v1.2·v1.3 부속서는 모두 역사적 호환 기록이다. 현재 적용 관계는 반드시 `REPOSITORY_MANIFEST.yaml`에서 다시 확인한다.

## 프로젝트 소스 정본

다음 승인 문서의 원문 바이트는 당시 프로젝트 소스를 정본으로 삼았다.

- `REFERENCE_RESEARCH_ANALYSIS_SOP_v7.md`
- `REFERENCE_RESEARCH_REPOSITORY_CONTRACT_v1.md`
- `REFERENCE_WORK_MODEL_SCHEMA_v2.md`

GitHub에는 동일 전문을 중복 저장하지 않아도 된다.

## 잠금 검증

`REPOSITORY_MANIFEST.yaml`은 `standard_source: project_source`와 잠금 파일 경로, 승인된 표준 파일명을 지정한다. `REFERENCE_RESEARCH_STANDARD_SOURCE_LOCK_v1.yaml`은 각 표준의 파일명·SHA-256·바이트 크기·승인 상태를 기록한다.

연구 시작 시 프로젝트 소스 원문을 직접 읽고 잠금과 대조한다. 파일명·SHA-256·바이트 크기·매니페스트 버전 중 하나라도 불일치하면 `HOLD_STANDARD_SOURCE`로 연구 쓰기와 병합을 중단한다.

## PROSE 저수준 증거층

v2 스키마가 승인한 `PSE`와 `PVAR`는 새 최상위 기법 체계가 아니라 기존 `PROSE`의 하위 증거·비교층이다.

- `PSE`: 의미 단위가 실제 절·문장·지문·문단으로 실현된 선택을 원문 좌표와 함께 보존한다.
- `PVAR`: 같은 작품 안에서 동일하거나 가까운 기능을 서로 다른 표면으로 푼 PSE들을 비교한다.
- 기존 `PRO-*`, Macro, Micro, TH는 유지한다.
- 기존 PROSE 기록의 일괄 이관은 하지 않는다. 새 연구에서 저수준 선택 손실이 확인될 때만 PSE/PVAR를 생성한다.
- PSE/PVAR를 추천 어미·문형·모바일 글자 수 규칙 DB로 사용하지 않는다.

## 검색 라우팅

아래 검색 라우팅은 당시 상태 기록이다. 현재 연구에서는 `REPOSITORY_MANIFEST.yaml`이 가리키는 현행 경로만 권위로 사용한다.

- Source Scene을 집필 검색에 사용할 때는 `indexes/scene_retrieval_contract.md`를 먼저 적용한다. 실제 결합 사슬은 `observed_chain`이며 `recommended_chain`이 아니다. 장면 전체 일치를 요구하지 않고 부분 문제·불일치 경계·사용 가능한 판단·가져오지 말아야 할 요소를 분리한다.
- 장면 전체의 표현·POV·대사·정보 공개 문제는 `indexes/expression_retrieval.md`를 사용한다.
- 문장·지문·문단의 실제 실현 선택이 문제일 때는 `indexes/prose_realization_retrieval.md`에서 PVAR → PSE → source scene 순으로 재진입한다.

세 인덱스는 서로 대체 관계가 아니다. Source Scene의 관찰된 beat 수·순서·질문권·명령권·침묵·효과음 조합을 현행 집필 템플릿이나 자동 발동 규칙으로 해석하지 않는다.

## 정본 역할

- 프로젝트 소스: SOP·저장소 계약·작품 모델 스키마의 승인 원문
- GitHub `main`: 연구 기록·작품 모델·PSE·PVAR·원천 좌표·TH·인덱스·감사·영수증·커밋 상태
- GitHub 잠금 파일: 프로젝트 소스 표준의 무결성과 적용 버전

## 필수 루트 파일

아래 트리는 당시 상태 기록이다.

```text
/
├─ README.md
├─ REPOSITORY_MANIFEST.yaml
├─ REFERENCE_RESEARCH_STANDARD_SOURCE_LOCK_v1.yaml
├─ REFERENCE_RESEARCH_REPOSITORY_CONTRACT_v1.3_PROJECT_SOURCE_ADDENDUM.md
├─ REFERENCE_RESEARCH_ANONYMITY_CONTRACT_v1.md
├─ registry/
├─ works/
├─ comparisons/
├─ mc_candidates/
├─ indexes/
└─ audits/
```

BASE SHA·충돌 방지·검증·영수증·커밋 규칙은 기존 저장소 계약을 그대로 따른다.
