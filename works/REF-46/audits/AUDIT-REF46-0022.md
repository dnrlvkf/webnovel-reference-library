# AUDIT-REF46-0022 · RELATIONSHIP / ORGANIZATION 작품 모델 편중 감사

- work_id: `REF-46`
- identity_exposure: `sealed`
- audit_type: `track_coverage / pre_merge`
- mode: `작품 전체 왕복 채굴`
- question: `이미 검증된 장면의 관계·조직 권리 변화가 작품 모델층에서 누락되어 있는가.`
- base_sha: `2400f30d0a77e94301ed18e58b6147d43f7d6db7`
- source_id: `SRC-LEGACY-REF46`
- source_boundary: `1~917화 / exact`
- source_sha256: `9cf9d175c228c02e960a04f3d721f29bb4362b380065f2fd200b828291ba1191`
- status: `passed_pre_merge`

## 표준 잠금

- manifest: schema `1.7`, canonical branch `main`.
- approved SOP: `REFERENCE_RESEARCH_ANALYSIS_SOP_v7.1.md` / SHA·size lock match.
- approved repository contract: `REFERENCE_RESEARCH_REPOSITORY_CONTRACT_v1.md` / lock match.
- approved work model schema: `REFERENCE_WORK_MODEL_SCHEMA_v2.md` / lock match.
- current addendum: `REFERENCE_RESEARCH_REPOSITORY_CONTRACT_v1.4_PROJECT_SOURCE_ADDENDUM.md`.
- source bridge: `VERIFIED_MATCH`.

## 감사 전 works-layer 분포

- CHARACTER: `3` standalone files.
- RELATIONSHIP: `1` standalone file (`REL-REF46-0001`).
- ORGANIZATION: `0` standalone files / directory absent.
- STORY: `2` standalone files.
- PROSE: `1` standalone file.
- TH: `2` verified threads.

파일 수 자체를 결함으로 판정하지 않았다. 아래 조건을 모두 충족하는지로 누락 여부를 판단했다.

1. 기존 CHARACTER·TH·Source Scene에 권리·의무·정보 접근·명령·위임 변화가 반복적으로 이미 존재함.
2. 단일 장면 감정 변화가 아니라 떨어진 구간의 후속 행동으로 증명됨.
3. 기존 파일에만 두면 관계·조직의 독립 질문이 캐릭터 요약에 흡수됨.
4. 새 파일이 기존 장면을 복사하지 않고 권리·조직 구조의 재독 좌표를 제공함.

## CREATE 판정

### `REL-REF46-0002` · 주인공 A ↔ 베테랑 안내자 A

`CREATE / SUPPORTED`.

근거 범위:
- 150화 사적 정체 질문권과 완전 정보 접근의 분리.
- 174화 친분과 유료 전문 노동의 분리.
- 473화 높은 사회적 권력과 상대의 거절권 공존.
- 742~746화 구조·배치 위험 소유.
- 751~753화 보호 방향 역전과 길찾기·호송 국소 판단권 이동.

독립 질문: `오래된 동료 관계에서 정체 질문권·전문 노동권·배치 책임·호송 책임이 어떻게 이동하는가.`

### `REL-REF46-0003` · 주인공 A ↔ 마법사 장교 A

`CREATE / SUPPORTED`.

근거 범위:
- 208화 전문 밖 불가역 판단의 최종 결정권 이전.
- 360~362화 정체 의심·직접 검증·공적 보고 의무 충돌.
- 373화 보고 존재와 정보 충실도 분리.
- 590·616·717~718화 문제 영역별 제안권·안전 수정권·최종 결정권 분리.

독립 질문: `전문 판단권·정체 정보권·국가 보고 의무가 한 관계 안에서 어떻게 충돌하고 병존하는가.`

### `ORG-REF46-0001` · 종족 공동체 A

`CREATE / SUPPORTED`.

근거 범위:
- 452~454화 대표·장로·행정 전문 인력의 기능 분리, 외부 접근 허가, 기록·예산·토지 권한 위임.
- 634화 교육·측량 지원의 실제 조직 기능.
- 650~651화 보상·훈련·기술 전수·고용·문자 교육의 후속 운영.

독립 질문: `전사 중심 권위가 행정·재정·교육·고용 기능과 분리될 때 누가 어떤 권리와 비용을 갖는가.`

### `ORG-REF46-0002` · 군 조직 A

`CREATE / SUPPORTED`.

근거 범위:
- 338화 평시 보고 검증·부하 교정.
- 354~355화 위기 명령·위임·후방 차단.
- 360·373화 공식 보고와 선택적 누락·가공.
- 391화 관리 공백 책임.
- 553화 상부 명령에 따른 외부 임무 참여.
- 777화 명령 구조와 개인 목표의 충돌·이탈 선택.

독립 질문: `공식 직급이 어떤 판단·명령·위임·정보 권리를 주며, 같은 제도가 개인 행동권을 어떻게 제한하는가.`

## NO-CREATE 판정

### 신참 마법사 A ↔ 사랑하는 상대

`NO_CREATE_CURRENTLY`.

- 신참 마법사 A의 일방적 욕망·고백 억제·상대 미래 비용 계산은 CHARACTER/STORY에서 강하게 확인됨.
- 그러나 이번 감사에서 상호 질문권·접근권·통제권·비용 의무가 떨어진 구간에서 독립적으로 변하는 장기 관계 사슬은 충분히 확인되지 않았다.
- `감정이 중요함 = standalone RELATIONSHIP 필요`로 과대평가하지 않음.

### 신참 마법사 A ↔ 주인공 A

`NO_CREATE_CURRENTLY`.

- 전문적 인정과 동료 역할은 강하지만 현재 works-layer의 `CHR-REF46-0001`과 `SC-REF46-0002~0003`이 질문을 보존한다.
- 독립 장기 권리 질문이 새로 확인되기 전 파일을 늘리지 않음.

### 정체 네트워크·플레이어 공동체·기타 조직

`NO_CREATE_CURRENTLY`.

- `TH-REF46-05`에 정보 채널·정체 권리 근거가 존재하지만, 이번 감사의 현재 질문에서 특정 조직의 장기 자원·권한·비용 구조를 독립적으로 다시 읽어야 할 구체 공백이 확인되지 않았다.
- 조직 파일 수를 맞추기 위한 생성 금지.

## 연결 감사

- 새 RELATIONSHIP은 호감도가 아니라 질문·거절·전문 판단·정보 접근·보호·보고 의무 변화로 작성됨: `PASS`.
- 새 ORGANIZATION은 설정 소개가 아니라 접근·자산·보고·명령·위임·관리·고용 권한으로 작성됨: `PASS`.
- 캐릭터 판단을 조직 파일에 복사하지 않고 제도 조건이 캐릭터의 선택 가능성을 어떻게 바꾸는지 분리함: `PASS`.
- 기존 Source Scene을 재사용하고, 조직 구조에서 손실되는 장면만 `SC-REF46-0029~0030`으로 새 원천 좌표화: `PASS`.
- 신규 Event/Story/PROSE/Macro/Micro/TH/PSE/PVAR를 파일 수 목적으로 만들지 않음: `PASS`.
- v7.1 onboarding/prose-realization 질문이 아닌 배치이므로 PSE/PVAR 미생성: `PASS`.

## 근거 경계

- 공동체 A의 대표 정체 공개 뒤 최종 대표 정당성: `HOLD`.
- 공동체 A의 공식 반대 의견·처벌·감사 절차: `HOLD`.
- 군 조직 A의 정확한 승급 절차: `HOLD`.
- 군 조직 A의 정보 누락·가공에 대한 공식 징계: `HOLD`.
- 마법사 장교 A의 조직 이탈 뒤 보고망·부하 접근권 잔존: `HOLD`.
- 주인공 A가 베테랑 안내자 A의 마지막 내부 판단을 사후에 정확히 아는지: `HOLD`.

## 익명화 감사

- works-layer 신규 파일에 실제 작품명·인물명·조직명·원천 파일명 없음: `PASS`.
- 원문 고유 문장 장기 인용 없음: `PASS`.
- 회차·행·SHA는 재진입 좌표로만 사용: `PASS`.

## 결론

편중은 실제였지만 `RELATIONSHIP 1 / ORGANIZATION 0`이라는 숫자 때문에 보정한 것이 아니다. 기존 고해상도 CHARACTER·TH가 이미 보존하던 **네 개의 독립 권리·조직 질문**만 작품 모델층으로 승격한다.

다음 원문 연구 질문은 새 파일 수가 아니라 `ORG-REF46-0001`과 `TH-REF46-01/05`가 공유하는 미확인 범위, 즉 **후반 공개 정체 뒤 종족 공동체 A의 대표권 인정 기준**으로 넘길 수 있다.
