# AUDIT-REF46-0020

- work_id: `REF-46`
- mode: `작품 전체 왕복 채굴`
- focus: `753화 이후 베테랑 안내자 A 외적 유산 STORY/RELATIONSHIP`
- standard: `REFERENCE_RESEARCH_ANALYSIS_SOP_v7.1.md`
- schema: `REFERENCE_WORK_MODEL_SCHEMA_v2.md`
- base_sha: `0e2b99fb96c76c0b573ddc8bec34dac1e8b37630`
- source_sha256: `9cf9d175c228c02e960a04f3d721f29bb4362b380065f2fd200b828291ba1191`
- receipt: `RCPT-20260817-1202-REF46`
- status: `passed_pre_merge`

## 표준·정본 복원

- `REPOSITORY_MANIFEST.yaml` 현행 schema version `1.7` 확인.
- canonical branch `main` 확인.
- project-source 승인 표준 `REFERENCE_RESEARCH_ANALYSIS_SOP_v7.1.md`, `REFERENCE_RESEARCH_REPOSITORY_CONTRACT_v1.md`, `REFERENCE_WORK_MODEL_SCHEMA_v2.md`의 파일명·SHA-256·byte size가 표준 잠금과 일치함.
- 현행 addendum `REFERENCE_RESEARCH_REPOSITORY_CONTRACT_v1.4_PROJECT_SOURCE_ADDENDUM.md` 확인.
- REF-46 source bridge `VERIFIED_MATCH`, exact boundary `1~917화`, source SHA 일치 확인.
- 이전 REF-46 연구 뒤 main에 132개 커밋이 추가되었으나 REF-46 연구 내용과 직접 충돌한 변경은 없고 source bridge transport 및 전역 표준/검색 계약 갱신이 중심임을 확인.

## 원문 좌표 감사

- `SC-REF46-0025`: 739화 / `347,703~347,767행` / SHA `b643dadc1b357a67bc110ebc5e0033dcf2f617ee20796b80db80ee19aaa7d0d0`
- `SC-REF46-0026`: 754화 / `354,291~354,418행` / SHA `a11fcffbd05b59c75939b836bf4e186e4f5585180e1536607fa14fb2cf8d67cd`
- `SC-REF46-0027`: 773~774화 / `361,827~362,006행` / SHA `17f615376a75db0f7aaea48ae4787d28b97b3a91b3a7e09d9b7e4a4a4431238c`
- `SC-REF46-0028`: 789화 / `367,787~367,818행` / SHA `32960f3582b32f4ab2c88e51744ceab72bd5fc81c9de4ece8e233317ca425840`

지원 좌표 775·776·794·829화도 원문 raw SHA를 재확인함.

## CHARACTER 경계 감사

- 753화 이후 고인 본인의 자기판단을 새로 만들지 않음.
- 타인의 회고·평가를 `CHR-REF46-0002`의 자기평가 근거로 역귀속하지 않음.
- 기존 CHARACTER 포화 판정 유지.

## RELATIONSHIP 감사

신규 `REL-REF46-0001`은 감정 호감도가 아니라 권리·정보 변화로 구성됨.

- 행정 담당자 A의 호감: `DIRECT`.
- 베테랑 안내자 A의 반복 돌봄과 마지막 특정: `DIRECT / SUPPORTED`.
- 상호 연애 감정 확정: `HOLD`.
- 739화 참전 중단권: 없음.
- 774화 마지막 메시지 뒤 새로 얻는 것: 사망자의 사적 우선순위 정보 + 자기 애도 정당성.
- 새로 얻지 못하는 것: 생전 통제권·공식 연애 관계·상호 미래 약속.

사후 정보를 생전 권리 소급으로 과해석하지 않음.

## STORY 감사

신규 `STY-REF46-0002`는 죽음 후 회상 목록이 아니라 서로 다른 상태 변화로 분리됨.

- 754: 독자의 장기 가치 재평가
- 758~759: 현재 위기로 감정 정산 유예
- 768~769: 후속 적대 판단의 비용
- 773~774: 관계 정보권·애도권 변화
- 775~776: 사회적 교육 기억·기술 귀속
- 789·794: 실제 탐사 행동 재사용
- 829: 새 전문가 평가의 직업 기준

같은 칭찬의 반복이 아니라 증거 종류가 달라짐을 확인.

## PROSE / v7.1 감사

- 754화 제한적 타인 시점은 기존 정보 접근권 모델의 변형으로 확인.
- 새 기능: 사망자의 숨은 현재 감정이 아니라 `주인공 A가 알지 못하는 잃어버린 미래 가치 평가`를 독자에게만 공개.
- 외부 관찰자의 대체 미래 판정을 객관적 실현 미래로 승격하지 않음.
- 754·774·789·829화는 독자가 기존 아크를 이미 학습한 callback/payoff이므로 압축 표면을 첫 소개/온보딩 문체로 일반화하지 않음.
- 단문 수·문단 길이 같은 표면 수치로 일반화하지 않음.

## PSE/PVAR 억제 감사

- 신규 PSE: 0.
- 신규 PVAR: 0.

이번 질문에서 손실되는 핵심은 `정보 공개 시점 → 관계권/행동 변화 → 후속 회수`이며, 조사·부사·연결 어미·시제·문장/문단 경계의 독립 비교 문제가 아님.

v7.1/v2가 PSE/PVAR를 승인했다는 이유만으로 기계 생성하지 않음.

## Source Scene / Macro / Micro / TH 감사

- 신규 Source Scene: 4. 각 장면은 별도 상태 변화와 재독 이유를 가짐.
- 신규 Macro: 1 (`MAC-REF46-0001`). 739화 생전 권리 한계와 773~774화 사후 정보 공개를 함께 읽어야 하는 독립 집필 판단 존재.
- 신규 Micro: 0. 마지막 메시지 문구 자체보다 정보 배치와 관계권 변화가 핵심임.
- 신규 TH: 0. 같은 작품의 다른 사망 인물에서 반복·변형·반례를 확인하지 않았으므로 장기 메커니즘 승격 금지.

## 반례·HOLD 감사

- `낮은 전투 등급 = 낮은 장기 기여`: 754화 관찰자 판정으로 반례가 제시되지만 대체 미래 자체는 미실현.
- `마지막 부탁 = 상호 연애 고백`: 성립하지 않음.
- `사후 정보 = 생전 관계 권리`: 성립하지 않음.
- `가르친 방식 = 영원한 최고 성능`: 789화 새 길잡이형 동료가 반례.
- `829화 이후 이름 재호출 없음 = 잊힘`: 근거 없음.

## 중복·편중 감사

- 기존 `STY-REF46-0001`은 POV 정보권 전반, 신규 `STY-REF46-0002`는 특정 인물 사후 유산의 장기 배열로 질문이 다름.
- `REL-REF46-0001`은 기존 REF-46에 단독 RELATIONSHIP 파일이 없던 실제 공백을 메움.
- `MAC-REF46-0001`은 Source Scene 요약이 아니라 생전 권리 한계와 사후 정보 교정의 결합 재독 단위임.
- CHARACTER 유사 사례 추가를 중단해 기존 편중을 악화시키지 않음.

## 익명성 감사

- 파생 연구층에 실제 작품명·인물명·조직명 노출 없음.
- 역할명·REF 코드·회차·행·SHA만 사용.
- 원문 식별자는 source bridge를 통해서만 재진입.

## 결과

`passed_pre_merge`.

현재 외적 유산 질문은 서로 다른 증거 채널이 충분히 확보되어 포화에 가까움. 동일 회상 사례 신규 수집보다 REF-46 RELATIONSHIP/ORGANIZATION 편중 감사를 다음 단계로 제안한다.
