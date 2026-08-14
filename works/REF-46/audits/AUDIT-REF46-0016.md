# AUDIT-REF46-0016

- work_id: `REF-46`
- mode: `작품 전체 왕복 채굴`
- base_sha: `ce6fbdf1929064e714d390e7892ba4f146bc174c`
- branch: `research/ref46-post-neardeath-guide-duty`
- question: `742~743화 죽음 직전 구조 경험 이후 교육·후방 역할과 생존 판단의 재결합`
- status: `passed_pre_merge`

## 표준·원천 감사

- manifest canonical branch `main` 재확인.
- project-source SOP v6.1 / repository contract v1 / work-model schema v1의 파일명·SHA-256·바이트 크기 lock 일치.
- REF-46 전체 원천 SHA-256 `9cf9d175c228c02e960a04f3d721f29bb4362b380065f2fd200b828291ba1191` 재확인.
- 직접 재독 범위 `742~753화 / 348,691~354,290행` raw SHA-256 `a7ab597842fa7bf15daceb9a78552928117d55fc5dbc0b990cc18820b08b740c`.

## 근거 감사

- 742화의 죽음 공포·생존 욕망을 `공포 극복`으로 뒤집지 않음.
- 746~748화의 현장 참여는 보호 범위·후열·길잡이 전문 기능으로 제한되므로 149화 현장 부족 판정 철회로 처리하지 않음.
- 751~753화의 호송 책임은 정보 수집·현실적 이동안·도주 계산·현장 오판/수정·전문 오더·최종 선택 순서로 보존.
- 753화 개인 도주 선택지가 직접 제시된 뒤 742화 죽음 경험이 명시적으로 재호출되는 인과를 확인.
- 마지막 선택을 상시 자기희생 성격으로 일반화하지 않고 `역할 대체 불가능성 + 호송 대상 생존 경로` 조건의 비가역 예외로 제한.
- 강한 동료 A의 오더 수용은 전투 서열 역전이 아니라 길찾기·호송 문제의 국소 지휘권으로 제한.

## 산출물 감사

- 신규 Source Scene: 2 (`SC-REF46-0023`, `SC-REF46-0024`).
- 수정 CHARACTER: `CHR-REF46-0002` 1건.
- 신규 RELATIONSHIP/EVENT/STORY/PROSE 단독 파일: 0.
- 신규 TH: 0.
- 신규 Macro: 0.
- 신규 Micro: 0.
- 기존 교육 실패·사망 음성 판정, 449화 HOLD 경계, 역할별 자기평가 분리는 삭제하지 않음.

## 원천 재진입 감사

- `SC-REF46-0023`
  - `746화 / 350,783~350,843행` SHA `1adc08bc402ae8967f21f71dbc65c37d80af66f2b40443015fe9718d3fd5b204`
  - `748화 / 351,447~351,483행` SHA `5e2c25108eaa36525fd7e44715c3979461d40e3095cc56f5b9b435d40727676f`
- `SC-REF46-0024`
  - `751화 / 353,279~353,453행` SHA `f82eb0d899fb5954a1347d1ff6d6946ebf053c5a5ef097336d2509baf856919d`
  - `752화 / 353,493~353,639행` SHA `6ca91b843fe2d8f3d31fb59971b1ef99bab2c153cf1b367d04db37d17cee5583`
  - `752~753화 / 353,769~354,149행` SHA `56b13a4f90bb579800cb1bdc56fdbf2acad17c700685ae64d999e84a3c048bcb`

## 익명성 감사

- 일반 연구층에 실제 작품명·저자명·원천 파일명 없음.
- 실제 인물·조직·기술 고유명은 역할명으로 치환.
- 원문 장문 인용 없음.

## 결과

pre-merge audit passed. 병합 전 remote `main`이 BASE에서 움직였는지 재확인한다.
