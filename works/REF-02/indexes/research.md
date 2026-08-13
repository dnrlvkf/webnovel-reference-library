# REF-02 연구 인덱스

- identity: `sealed`
- source: `SRC-COL2-027`
- boundary: `1~284화 / exact`
- canonical_completed_precision_scope: `1~284화`
- first_pass_direct_read_scope: `1~284화 / complete`
- overall_research_status: `whole_work_mining_required`
- latest_batch: `BATCH-REF02-0010`
- latest_receipt: `RCPT-20260813-1237-REF02`
- latest_status: `complete_first_pass_batch`
- research_content_sha: `ab80452f5e4ef08e8acd7bc7d4a7039f47d2a1e2`

## 표준 상태

- standard_source: `project_source`
- SOP: `REFERENCE_RESEARCH_ANALYSIS_SOP_v6.1.md`
- lock: `REFERENCE_RESEARCH_STANDARD_SOURCE_LOCK_v1.yaml`
- contract_addendum: `REFERENCE_RESEARCH_REPOSITORY_CONTRACT_v1.2_PROJECT_SOURCE_ADDENDUM.md`
- verification: filename·SHA-256·byte size matched

## 현재 연구 모드

- 1차 직접 순회: `complete / 1~284화`
- 다음 공식 모드: `작품 전체 왕복 채굴`
- completion marker: `not_created`
- 이유: whole-work HOLD·반례·포화·품질 감사가 남아 있음.

## 운영 전략

- 구간 정밀 분석은 `1~284화` 전체를 직접 읽는 단계까지 완료.
- 저변화 반복은 압축하되 Source Scene 좌표로 재진입 가능하게 유지.
- 작품 전체 왕복 채굴에서는 초·중·후반의 떨어진 장면을 같은 질문으로 다시 읽어 기존 TH의 범위·반례·비용·실패를 확정한다.
- 동일 질문을 새 TH로 증식하지 않고 기존 모델·TH를 우선 갱신한다.
- 완료는 source boundary 도달이 아니라 unresolved HOLD·포화·품질 감사까지 끝났을 때만 판정한다.

## 배치

- `BATCH-REF02-0001` — 1~10화 / complete
- `BATCH-REF02-0002` — 11~20화 / complete
- `BATCH-REF02-0003` — 21~30화 / complete
- `BATCH-REF02-0004` — 31~40화 / complete
- `BATCH-REF02-0005` — 41~50화 / complete
- `BATCH-REF02-0006` — 51~60화 / complete
- `BATCH-REF02-0007` — 61~120화 / adaptive / complete
- `BATCH-REF02-0008` — 121~180화 / adaptive / complete
- `BATCH-REF02-0009` — 181~240화 / adaptive / complete
- `BATCH-REF02-0010` — 241~284화 / adaptive / complete

## 원천 장면

- `SC-REF02-0001~0052` — 1~60화
- `SC-REF02-0053~0062` — 61~120화 / adaptive clusters
- `SC-REF02-0063~0071` — 121~180화 / adaptive clusters
- `SC-REF02-0072~0081` — 181~240화 / adaptive clusters
- `SC-REF02-0082~0088` — 241~284화 / adaptive clusters

## 작품 모델

### CHARACTER

- `CHR-REF02-0001` — 주인공 A 누적 판단 지도 / whole-work 최종 통합 대상.
- `CHR-REF02-0002` — 상위 동맹 A / 과거 본능 실패→후대 기준→현혹 붕괴→비가역 비용 복귀→유산 인계.
- `CHR-REF02-0003` — 자유 탐구자 A / 통제 역이용→탐구·자유→독점 정보·관계 욕망→현재 선택 책임 경쟁→세계 파괴성.

### RELATIONSHIP

- `REL-REF02-0001` — 장기 동업자 A / 비밀권·이동권·신체 성장 책임·상계 공동 목표 + 기존 조직 의무/기억 강제 침해.
- `REL-REF02-0002~0004` — 기존 조직·검증 동료 관계.
- `REL-REF02-0005` — 상위 후계자 A / 자율성 선택→독립 재등장→상위 체계 강제 분리.
- `REL-REF02-0006` — 위험 상위자와 복수 계약→공동 공로·원조·잠입·영혼 종결.
- `REL-REF02-0007` — 상위 동맹 A / 현재 기술↔미래 후대 연구 의무→현혹 붕괴→비가역 비용 복귀→유산.
- `REL-REF02-0008` — 포획 강적 A / 강제 노예·수련 보조→성장 자원 약속 이행·해방→자기 동기의 최종 전쟁 동맹.

### ORGANIZATION

- `ORG-REF02-0001~0004` — 기존 모델 유지.
- 최종부의 숙명 명령·하위 지휘권 역이용·적대 진영 수장 위장/전쟁 운영은 CHARACTER/RELATIONSHIP/EVENT/STORY에 우선 흡수; whole-work에서 중복 여부 재감사.

### EVENT

- `EVT-REF02-0001~0007` — 1~240화.
- `EVT-REF02-0008` — 강제 상위 임무→진영 규칙 역이용→세계 위협 재분류/자기소모→관계망 해산→대승경→조직 지휘권 탈취→6계위→숨은 동료 성장 회수→최종 상위자/최종 적→세계 파괴수→비상 능력 종결 시도.

### STORY / PAYOFF

- `STY-REF02-0001~0007` — 1~240화.
- `STY-REF02-0008` — 보상 직후 더 깊은 비용/종료 조건을 재개방하고 숨은 동료 투자·실존 앵커를 순차 공개하는 최종부 배열.
- `PAY-REF02-0001~0004` — 기존 장기 회수.
- `PAY-REF02-0005` — 운명 회피 봉인→자발적 위험 선택→사명 종료→봉인 해제→최종전 시간 정지 역할.

### PROSE

- `PRO-REF02-0001~0007` — 1~240화.
- `PRO-REF02-0008` — 강제 상황의 권리 계산, 심마의 기억 불일치 판별, 6계위 법칙·지속·관측 지문, 최종 관계 욕망 조건 조립.

## 활성 TH · whole-work 재검증 대기

- `TH-REF02-CHR-02` — `VERIFIED_THREAD`; 진체/변형 존재 대상 지정·시선/행동권 조건을 1~284 범위에서 재통합 예정.
- `TH-REF02-CHR-06` — `VERIFIED_THREAD`; 자율성·강제·영향/현재 선택 책임의 전체 분포 재검증 예정.
- `TH-REF02-REL-04` — `VERIFIED_THREAD`; 권리 협상과 직접 행동권 박탈의 경계 재검증 예정.
- `TH-REF02-REL-05`, `TH-REF02-REL-06` — `VERIFIED_THREAD`.
- `TH-REF02-TEC-02` — `VERIFIED_THREAD`; 개인 위장→조직 지휘권 위장의 장기 확장 재검증 예정.
- `TH-REF02-TEC-05` — `VERIFIED_THREAD`.
- `TH-REF02-TEC-06` — `VERIFIED_THREAD`.
- `TH-REF02-TEC-07` — `VERIFIED_THREAD`; 실패가 구조 오판보다 실행 용량·도구·신체·인지·관측 한계에 집중되는지 왕복 검증 예정.
- `TH-REF02-TEC-08` — `VERIFIED_THREAD`; 원영경식 육신/영혼을 넘어 `표면 격파와 경지별 실존 앵커 종결`로 재구성할지 왕복 검증 예정.
- `TH-REF02-EVT-03` — `VERIFIED_THREAD`.

## Macro·Micro

- `MAC-REF02-0001~0006` — 기존.
- `MAC-REF02-0007` — 같은 적·같은 반운명 명분이 있어도 `도피 vs 원인과 대결`의 방법 차이로 동맹 거절.
- `MAC-REF02-0008` — 인간형을 잃은 최종 적의 독점 정보 욕망을 호출해 시선·대상 지정 조건 조립.
- `MIC-REF02-0001` — 기존.
- 241~284화 신규 Micro: 없음.

## 241~284화 핵심 판정

1. 강제 상위 임무 실행은 충성/동의와 다르다.
2. 상위 조직의 절대 명령은 하위 희생 명령을 무효화하는 제한으로도 역이용 가능하다.
3. 자율성은 보편적 불간섭 원칙이 아니다. 위험한 적·실존 위기에는 강제가 발생한다.
4. 의무가 끝난 동료의 평범한 삶·현재 정체성 선택은 존중된다.
5. 같은 적/명분보다 해결 방법이 동맹 판정의 더 높은 기준이다.
6. 6계위는 일반 기술 자동 상향이 아니라 상위 법칙 직접 접속이며 지속·영혼·관측 비용이 크다.
7. 새 상위 기술도 전투 경험이 높은 적의 기만에 운용 실패할 수 있다.
8. 표면 육신이 실제 최종 앵커가 아닌 사례가 대승경·세계수 단계에서 반복된다.
9. 위장은 개인 신분에서 조직 수장 외형·예상 기술·지휘권 탈취까지 확대된다.
10. 최종전은 숨겨 둔 동료 투자/봉인을 역할 분업으로 회수한다.
11. 최종 적 인간형 격파 뒤 뿌리/세계 구조가 남아 종료 조건이 다시 열린다.
12. source boundary는 비상 능력 사용 순간에 닫혀 이후 세계 상태는 HOLD다.

## HOLD · whole-work 우선 질문

- 자율성의 자기/타인 비대칭과 강제 예외의 정확한 조건.
- 상위 동맹 A 후대 연구 의무 직접 회수.
- 장기 동업자 A 기존 조직 의무와 상계 공동 목표 최종 충돌.
- 상위 후계자 A 강제 상층 이동 뒤 재교차.
- TEC-07 순수 잘못된 구조 판독 실패 여부.
- 비상 능력 분신/가짜 본체 오지정 실패 여부.
- 초월 힘 모사 감지의 일반 법칙 여부.
- 세계 위기 시계와 주인공 성장의 실제 인과.
- 강제 상위 임무의 source boundary 이후 장기 종속/거절권 구조.
- 284화 비상 능력 사용 이후 세계 파괴수 최종 상태.

## 감사

- `AUDIT-REF02-0001~0014` — historical / 31~240 pre/post.
- `AUDIT-REF02-0015` — 241~284 adaptive pre-merge / passed.
- `AUDIT-REF02-0016` — 241~284 post-merge + 1~284 first-pass audit / complete.

## 원격 상태

- PR: `#14` / merged.
- research content SHA: `ab80452f5e4ef08e8acd7bc7d4a7039f47d2a1e2`.
- final SHA: `RCPT-20260813-1237-REF02-SEAL` 참조 예정.
- remote status: `verified_on_main`.

## 다음 단계 · 작품 전체 왕복 채굴

1. 자율성 기준의 자기/타인 비대칭과 강제 예외.
2. TEC-07 실패 유형의 실제 분포와 `순수 구조 오판` 부재 여부.
3. TEC-08의 `경지별 실존 앵커` 상위 메커니즘.
4. 세계 위기 시계와 성장의 인과/제시 동기화 구분.
5. 관계·유산 HOLD의 source-boundary 판정.
6. 전체 TH/Macro/Payoff 포화·중복·품질 감사.
