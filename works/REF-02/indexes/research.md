# REF-02 연구 인덱스

- identity: `sealed`
- source: `SRC-COL2-027`
- boundary: `1~284화 / exact`
- canonical_completed_precision_scope: `1~40화`
- prepared_scope: `41~50화`
- latest_batch: `BATCH-REF02-0005`
- latest_receipt: `RCPT-20260813-0906-REF02`
- latest_status: `pending_merge`
- research_content_sha: `PENDING_MERGE`

## 표준 상태

- standard_source: `project_source`
- SOP: `REFERENCE_RESEARCH_ANALYSIS_SOP_v6.1.md`
- lock: `REFERENCE_RESEARCH_STANDARD_SOURCE_LOCK_v1.yaml`
- contract_addendum: `REFERENCE_RESEARCH_REPOSITORY_CONTRACT_v1.2_PROJECT_SOURCE_ADDENDUM.md`
- verification: filename·SHA-256·byte size matched

## 배치

- `BATCH-REF02-0001` — 1~10화 / complete
- `BATCH-REF02-0002` — 11~20화 / complete
- `BATCH-REF02-0003` — 21~30화 / complete
- `BATCH-REF02-0004` — 31~40화 / complete
- `BATCH-REF02-0005` — 41~50화 / pending merge

## 원천 장면

- `SC-REF02-0001~0004` — 1~10화
- `SC-REF02-0005~0012` — 11~20화
- `SC-REF02-0013~0022` — 21~30화
- `SC-REF02-0023~0032` — 31~40화
- `SC-REF02-0033~0042` — 41~50화 / branch

## 작품 모델

### 누적 모델

- `CHR-REF02-0001` — 주인공 A 조건별 판단 지도, 1~50화 준비
- `REL-REF02-0001` — 제한 계약에서 감사·사과·비공식 의무까지, 11~50화 준비
- `EVT-REF02-0001` — 사건 결과의 성장 인프라·새 위험 전환, 1~30화
- `STY-REF02-0001` — 보상 정산·생활 관계·다음 위험 배열, 1~30화
- `PRO-REF02-0001` — 설명·시점·재분류 운용, 1~30화

### 31~40화

- `REL-REF02-0002` — 경쟁 상위 조직과의 비용·권리 협력
- `ORG-REF02-0001`, `ORG-REF02-0002` — 경쟁 조직 모델
- `EVT-REF02-0002` — 비경 수확·자율 법기·법역 토벌
- `STY-REF02-0002` — 수확·제작·실전 검증·법역 반전
- `PRO-REF02-0002` — 합리적 오해·역할 설명·구조 비유

### 41~50화 준비

- `REL-REF02-0003` — 소개자의 신뢰가 절차적 보호로 바뀌는 초기 관계
- `EVT-REF02-0003` — 결전 후 포식·분리 신원·축기·중층부 진입
- `STY-REF02-0003` — 승리·은폐·성장 보상을 즉시 다음 비용으로 뒤집는 배열
- `PRO-REF02-0003` — POV 전환·비전환과 사후 의도 공개

## 활성 TH

- `TH-REF02-CHR-02` — `VERIFIED_THREAD` / 연속 위협 기준 비상 능력 배분 보강
- `TH-REF02-CHR-06` — `VERIFIED_THREAD` / 상대 포식 선택·반격·책임 귀속 신규
- `TH-REF02-REL-04` — `VERIFIED_THREAD`
- `TH-REF02-REL-05` — `VERIFIED_THREAD`
- `TH-REF02-TEC-02` — `VERIFIED_THREAD` / 별도 활동 신원으로 확장
- `TH-REF02-TEC-05` — `VERIFIED_SCENE`
- `TH-REF02-EVT-03` — `VERIFIED_THREAD`

## Macro·Micro

- `MAC-REF02-0001` — 거래 관계의 걱정을 손익 언어로 감추고 반사 발화가 사과를 끌어내는 장면
- `MIC-REF02-0001` — 상대의 성격 판정을 되돌려 사과를 발생시키는 반사 발화

## 감사

- `AUDIT-REF02-0001` — historical HOLD
- `AUDIT-REF02-0002` — standard source restore / resolved
- `AUDIT-REF02-0003` — 31~40 pre-merge / passed
- `AUDIT-REF02-0004` — 31~40 post-merge / complete
- `AUDIT-REF02-0005` — 41~50 v6.1 pre-merge / passed

## 41~50화 핵심 미확인

- 인간다움이 큰 생존 비용과 충돌할 때의 우선순위
- 자기합리화가 죄책감·타인 비판으로 수정되는지
- 원영경 후기 이상에게 비상 능력이 실제로 통하지 않는지
- 중개자 A의 걱정의 객관적 감정 성격
- 활동 신원 A와 실제 신원의 재연결 여부

## 다음 절차

1. branch diff와 최신 main HEAD를 비교한다.
2. 중복 ID·링크·익명성·스키마를 재감사한다.
3. 통과하면 PR 병합 후 `canonical_completed_precision_scope`를 `1~50화`로 올린다.
4. 영수증·전역 최근 영수증·post-merge audit·FINAL SHA를 봉인한다.
5. 다음 구간은 `51~60화`다.
