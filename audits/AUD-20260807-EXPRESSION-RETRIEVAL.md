# AUD-20260807-EXPRESSION-RETRIEVAL · 집필 직전 표현 검색 연결 감사

- date_time: `2026-08-07T12:14:00+09:00`
- mode: `repository routing audit`
- question: `기존 PROSE·Macro·반례 구조를 새 표현 연구층 없이 실제 집필 직전 검색 시스템으로 연결할 수 있는가`
- base_sha: `3f9e4a4b78bdba98904205bf598d688f3d440210`
- branch: `research/expression-retrieval-routing-20260807`
- status: `prepared_for_merge`

## 표준 검증

프로젝트 소스 표준 3종을 잠금 파일과 대조했다.

- `REFERENCE_RESEARCH_ANALYSIS_SOP_v6.md`: SHA-256 일치, 78408 bytes
- `REFERENCE_RESEARCH_REPOSITORY_CONTRACT_v1.md`: SHA-256 일치, 12579 bytes
- `REFERENCE_WORK_MODEL_SCHEMA_v1.md`: SHA-256 일치, 11902 bytes
- 프로젝트 소스 계약 부속서와 익명성 계약 확인

## 조회한 기록

- `REPOSITORY_MANIFEST.yaml`
- `REFERENCE_RESEARCH_STANDARD_SOURCE_LOCK_v1.yaml`
- `REFERENCE_RESEARCH_REPOSITORY_CONTRACT_v1.1_PROJECT_SOURCE_ADDENDUM.md`
- `REFERENCE_RESEARCH_ANONYMITY_CONTRACT_v1.md`
- `AGENTS.md`
- `README.md`
- `catalog/INDEX.md`
- `catalog/tables/anonymous-expression-scenes.csv`
- `catalog/tables/expression-units.csv`
- `works/REF-02/prose/PRO-REF02-0001.md`
- `works/REF-02/prose/PRO-REF02-0002.md`
- `works/REF-02/indexes/research.md`
- 최근 REF-02 연구 영수증과 병합 후 감사
- 초기 이관 커밋의 레거시 색인 구조

## 감사 결과

### 1. PROSE 연구층은 존재한다

현재 PROSE 기록에는 이미 다음이 포함되어 있다.

- 적용 조건
- 시점과 서술 초점
- 서술 거리와 감정 제시
- 정보 설명 위치
- 대사·지문 배열
- 문장·문단 리듬
- 대표 근거
- 대비 근거
- 이탈·반례
- 없으면 사라지는 것

따라서 별도 최상위 표현 연구층을 새로 만들 필요는 확인되지 않았다.

### 2. 레거시 표현 장면은 검색 가능한 필드를 이미 가진다

레거시 색인에는 익명 표현 장면 139건과 표현 단위 25건이 존재한다. 표현 장면은 장면 조건, 대사·행동 배열, 정보 공개 순서, 장면 종료 방식, 대표성, 표현 목적, 표면 모방 위험, 후속 회수 등을 가지고 있다.

따라서 기존 139건을 새 태그 DB로 다시 이관하는 작업은 현재 단계에서 중복 가능성이 높다.

### 3. 실제 병목은 라우팅이다

기존 저장소 규칙은 `catalog/`에서 검색을 시작하고 근거가 필요하면 REF와 원문으로 내려가도록 했지만, 실제 집필 직전에 다음을 강제하지 않았다.

- 사건·스토리 문제와 장면 표현 문제의 분리
- 같은 REF의 PROSE 우선 조회
- 대표·대비·실패/과잉 세트 재독
- 같은 REF 우선, 타 REF 후순위
- 참고작 종료 후 대상 작품 문체로 재번역
- 초고 후 의미 선점·중복 해설·주제 설명 대사 감사

이번 변경은 이 라우팅 공백만 보강한다.

## 변경 내용

### `indexes/expression_retrieval.md` 신규

- 집필 전 이중 진단
- 검색 순서
- 표현 문제 facet 9종
- 대표·대비·실패 세트
- 대상 작품으로 번역하는 단계
- 초고 후 표현 감사
- 스키마 확장 중단 조건
- 완료 판정

facet은 새 ID나 영구 태그가 아니라 검색 질문 좌표로 정의했다.

### `AGENTS.md` 수정

실제 집필 직전에는 `indexes/expression_retrieval.md`를 따르도록 진입 규칙을 추가했다.

### `README.md` 수정

사건·스토리 검색과 장면 표현 검색을 분리하고, 같은 REF 우선 및 대표·대비·실패 재독 원칙을 사용자 진입점에 노출했다.

## 스키마 판정

- 새 디렉터리: 없음
- 새 작품 모델 파일 유형: 없음
- 새 기법 ID 체계: 없음
- 새 영구 태그 DB: 없음
- 매니페스트 스키마 변경: 없음

현재 문제는 기존 필드 손실이 아니라 검색 연결 부족이므로 스키마 개정 조건을 충족하지 않는다.

## 익명성 감사

- 신규 인덱스와 규칙 파일에 실제 작품명·저자명·인물명·조직명·기술명 없음
- 레거시 고유명을 신규 연구층으로 복사하지 않음
- REF/SRC 코드와 역할 수준의 표현만 사용
- 원문 문장을 신규 규칙에 인용하지 않음

## 품질 감사

- 태그가 분석을 대신하지 않도록 facet을 검색 질문으로 제한함
- 표현 참고가 성공 사례 하나의 모방으로 끝나지 않도록 대표·대비·실패를 묶음
- 설명을 무조건 줄이는 규칙이 아니라 인물 판단·상대 수용·다음 행동 참여 여부를 감사 기준으로 삼음
- 같은 REF 우선 원칙으로 작품 간 표면 혼합 위험을 낮춤
- 기존 PROSE·Macro·Micro·TH의 원문 재독 역할을 유지함

## 다음 검증

실제 집필 샘플에서 다음을 측정한다.

1. 표현 문제를 한 문장으로 진단할 수 있는가.
2. 같은 REF 안에서 적합한 대표·대비·실패 근거를 찾을 수 있는가.
3. 초고의 서술자 의미 선점·중복 해설·주제 설명 대사가 줄어드는가.
4. 검색 실패가 반복될 경우에만 추가 facet 또는 스키마 변경을 검토한다.

## 변경 파일

- `indexes/expression_retrieval.md`
- `AGENTS.md`
- `README.md`
- `audits/AUD-20260807-EXPRESSION-RETRIEVAL.md`

## 판정

`PASS_FOR_MERGE`

새 표현 연구층을 만들지 않고도 기존 PROSE·Macro·Micro·반례·레거시 표현 장면을 집필 직전 검색 흐름으로 연결할 수 있다. 다음 단계는 스키마 확장이 아니라 실제 동일 회차 재작성 A/B 테스트다.
