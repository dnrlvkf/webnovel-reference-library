# REFERENCE_RESEARCH_REPOSITORY_CONTRACT_v1.1_PROJECT_SOURCE_ADDENDUM

> **SUPERSEDED / HISTORICAL COMPATIBILITY RECORD**
>
> 이 문서는 과거 프로젝트 소스 정본 전환 시점의 호환 기록이다. 현재 연구·집필·부트스트랩 지침으로 사용하지 않는다. 현행 적용 부속서는 `REPOSITORY_MANIFEST.yaml`의 `repository_contract_addendum_path`가 가리키는 문서이며, 현재 매니페스트는 `REFERENCE_RESEARCH_REPOSITORY_CONTRACT_v1.3_PROJECT_SOURCE_ADDENDUM.md`를 가리킨다. 아래의 SOP v6 / schema v1 참조는 역사적 출처 정보일 뿐 현행 표준이 아니다.

> 프로젝트 소스 정본 문서와 GitHub 연구 기록 정본을 분리하기 위한 저장소 계약 부속서

## 1. 적용 관계

이 부속서는 `REFERENCE_RESEARCH_REPOSITORY_CONTRACT_v1.md`에 추가하여 적용한다. 충돌하는 경우 이 부속서가 다음 항목에 한해 우선한다.

- 연구 표준 문서의 저장 위치
- 표준 문서의 무결성 검증
- 필수 루트 파일 목록

연구 판단, GitHub 연구 기록의 정본성, BASE SHA, 충돌 방지, 검증, 연구 영수증, 커밋 규칙은 기존 계약을 그대로 따른다.

## 2. 표준 문서 정본 위치

다음 세 문서의 승인된 원문 바이트는 프로젝트 소스를 정본으로 삼을 수 있다.

- `REFERENCE_RESEARCH_ANALYSIS_SOP_v6.md`
- `REFERENCE_RESEARCH_REPOSITORY_CONTRACT_v1.md`
- `REFERENCE_WORK_MODEL_SCHEMA_v1.md`

이 경우 GitHub 저장소에 동일한 전문 사본을 중복 저장할 의무는 없다.

## 3. GitHub 잠금 파일

`REPOSITORY_MANIFEST.yaml`은 다음을 지정해야 한다.

- `standard_source: project_source`
- `standard_source_lock_path`
- 승인된 각 표준의 파일명

잠금 파일은 각 문서의 다음 값을 포함해야 한다.

- 파일명
- SHA-256
- 바이트 크기
- 승인 상태

연구 시작 시 프로젝트 소스의 실제 파일을 직접 읽고 잠금 값과 대조한다.

## 4. 실패 닫힘

다음 중 하나라도 발생하면 연구 쓰기와 병합을 `HOLD_STANDARD_SOURCE`로 중단한다.

- 프로젝트 소스에서 필수 문서를 찾을 수 없음
- 파일명이 잠금과 다름
- SHA-256이 잠금과 다름
- 바이트 크기가 잠금과 다름
- 매니페스트와 잠금 파일이 서로 다른 버전을 가리킴

## 5. 정본 역할 분리

- 프로젝트 소스: SOP·저장소 계약·작품 모델 스키마의 승인된 원문 정본
- GitHub `main`: 연구 기록·작품 모델·원천 좌표·TH·인덱스·감사·영수증·커밋 상태의 정본
- GitHub 잠금 파일: 프로젝트 소스 표준의 무결성과 적용 버전을 고정하는 정본 장부

이전 채팅, 로컬 임시 수정본, 체크섬이 다른 사본은 정본이 아니다.

## 6. 기존 계약 조항 대체

기존 계약의 `# 2. 필수 루트 파일`은 다음으로 대체한다.

```text
/
├─ README.md
├─ REPOSITORY_MANIFEST.yaml
├─ REFERENCE_RESEARCH_STANDARD_SOURCE_LOCK_v1.yaml
├─ REFERENCE_RESEARCH_REPOSITORY_CONTRACT_v1.1_PROJECT_SOURCE_ADDENDUM.md
├─ REFERENCE_RESEARCH_ANONYMITY_CONTRACT_v1.md
├─ registry/
├─ works/
├─ comparisons/
├─ mc_candidates/
├─ indexes/
└─ audits/
```

표준 전문은 프로젝트 소스에서 직접 읽고 잠금으로 검증한다.
