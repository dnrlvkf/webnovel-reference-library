# SOP v6.1 표준 승격 감사

- date_time: `2026-08-08T23:52:00+09:00`
- operation: `project-source analysis SOP promotion`
- base_sha: `19b0f393e1b500bcb2f69ada6f39974b23b94e57`
- branch: `ops/promote-sop-v6.1-20260808`
- status: `reviewed_before_merge`

## 프로젝트 소스 직접 확인

승격 대상 프로젝트 소스를 직접 읽고 파일명·내용 선두·해시·바이트 크기를 확인했다.

- filename: `REFERENCE_RESEARCH_ANALYSIS_SOP_v6.1.md`
- sha256: `fc60b40c9e2dda72271284d295bf6daabd121b5494e16b3b5452e810f2cdb431`
- size_bytes: `94818`
- document heading: `REFERENCE_RESEARCH_ANALYSIS_SOP_v6.1`
- v6.1 scope: 캐릭터 경쟁 기준·오판·비합리적 이탈·복귀, POV 정보 접근권, 시점 비전환, 캐릭터 판단에서 실제 대사·지문 표현으로의 미시 연결을 보강

같은 프로젝트 소스의 나머지 필수 표준도 기존 잠금값과 일치함을 재확인했다.

- repository contract v1 SHA-256: `8a6479621af6d1196433ca5760ae727eb5ccc1b876dea468df3faafc964e304e`
- work model schema v1 SHA-256: `825324e6b2e4d3cdafce6decf1919c80aac1d9d59863c237960d49be64f79121`

## GitHub 변경

- `REFERENCE_RESEARCH_STANDARD_SOURCE_LOCK_v1.yaml`
  - analysis SOP filename: v6 → v6.1
  - approved SHA-256 갱신
  - approved byte size 갱신
- `REPOSITORY_MANIFEST.yaml`
  - `sop_filename`: v6 → v6.1

연구 기록·작품 모델·TH·원천 장면·인덱스의 의미 내용은 이 승격에서 수정하지 않았다.

## 계약 확인

프로젝트 소스 부속서의 표준 갱신 규칙에 따라 새 승인 프로젝트 소스, lock 갱신, manifest 갱신을 한 변경 묶음으로 처리했다. 매니페스트와 잠금은 동일한 v6.1 파일을 가리킨다.

## diff 감사

BASE 대비 표준 선택 변경은 lock과 manifest 두 파일에 한정된다. 별도 스키마 변경은 없으므로 manifest schema와 work-model schema 버전은 유지한다.

## 병합 전 조건

1. 원격 `main` HEAD가 BASE SHA와 같은지 다시 확인한다.
2. 다르면 manifest·lock의 동시 변경 여부를 다시 읽고 충돌을 검증한다.
3. 동일하면 force 없이 fast-forward 한다.
4. 원격 반영 뒤 검증 완료 SHA를 봉인한다.
