# REFERENCE_RESEARCH_REPOSITORY_CONTRACT_v1.2_PROJECT_SOURCE_ADDENDUM

> **SUPERSEDED / HISTORICAL COMPATIBILITY RECORD — NON-AUTHORITATIVE**
>
> 이 문서는 SOP v6.1 시점의 프로젝트 소스 정본 운용을 보존하는 역사 기록이다. 현재 연구·집필·부트스트랩 지침으로 사용하지 않는다. **현행 적용 부속서는 오직 `REPOSITORY_MANIFEST.yaml`의 `repository_contract_addendum_path`가 가리키는 문서다.** 이 역사 파일 안의 SOP·Schema·필수 루트 경로·당시 적용 버전 표기는 모두 과거 상태 기록이며 현재 권위를 갖지 않는다.

> v1.1 부속서의 프로젝트 소스 정본 운용을 유지하면서 최신 SOP 참조를 v6.1로 동기화한다.

## 적용 관계

이 문서는 `REFERENCE_RESEARCH_REPOSITORY_CONTRACT_v1.md`와 함께 적용한다. 연구 표준 문서의 저장 위치·무결성 검증·필수 루트 파일에 관해서는 이 부속서가 우선한다.

## 프로젝트 소스 정본

다음 승인 문서의 원문 바이트는 프로젝트 소스를 정본으로 삼는다.

- `REFERENCE_RESEARCH_ANALYSIS_SOP_v6.1.md`
- `REFERENCE_RESEARCH_REPOSITORY_CONTRACT_v1.md`
- `REFERENCE_WORK_MODEL_SCHEMA_v1.md`

GitHub에는 동일 전문을 중복 저장하지 않아도 된다.

## 잠금 검증

`REPOSITORY_MANIFEST.yaml`은 `standard_source: project_source`와 잠금 파일 경로, 승인된 표준 파일명을 지정한다. `REFERENCE_RESEARCH_STANDARD_SOURCE_LOCK_v1.yaml`은 각 표준의 파일명·SHA-256·바이트 크기·승인 상태를 기록한다.

연구 시작 시 프로젝트 소스 원문을 직접 읽고 잠금과 대조한다. 파일명·SHA-256·바이트 크기·매니페스트 버전 중 하나라도 불일치하면 `HOLD_STANDARD_SOURCE`로 연구 쓰기와 병합을 중단한다.

## 정본 역할

- 프로젝트 소스: SOP·저장소 계약·작품 모델 스키마의 승인 원문
- GitHub `main`: 연구 기록·작품 모델·원천 좌표·TH·인덱스·감사·영수증·커밋 상태
- GitHub 잠금 파일: 프로젝트 소스 표준의 무결성과 적용 버전

## 필수 루트 파일

```text
/
├─ README.md
├─ REPOSITORY_MANIFEST.yaml
├─ REFERENCE_RESEARCH_STANDARD_SOURCE_LOCK_v1.yaml
├─ REFERENCE_RESEARCH_REPOSITORY_CONTRACT_v1.2_PROJECT_SOURCE_ADDENDUM.md
├─ REFERENCE_RESEARCH_ANONYMITY_CONTRACT_v1.md
├─ registry/
├─ works/
├─ comparisons/
├─ mc_candidates/
├─ indexes/
└─ audits/
```

BASE SHA·충돌 방지·검증·영수증·커밋 규칙은 기존 저장소 계약을 그대로 따른다.
