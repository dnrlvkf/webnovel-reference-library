# REF-47 PSE/PVAR 첫 적용 감사

- base_sha: `26773d3d9115473db6d538d4be7dd59f0b9a6816`
- branch: `research/ref47-prose-variation-pilot`
- mode: 작품 전체 왕복 채굴 / prose pilot

## 감사
- [x] 프로젝트 소스 SOP v7 / schema v2 / repository contract v1 해시 일치
- [x] REF-47 신원은 private map에만 저장
- [x] 일반 연구층에 실제 작품명·인물명·원문 문장 미복사
- [x] PSE는 4개 선택 장면만 생성, 전체 문단 기계 등록 없음
- [x] PVAR는 4 PSE의 실제 변형을 비교하며 추천 문형 목록으로 만들지 않음
- [x] `그렇다고` 반복을 메커니즘으로 승격하지 않고 표면 붕괴 사례 포함
- [x] 문단 길이 절대값보다 문장 결속과 화면 블록 경계를 비교
- [x] CHARACTER/RELATIONSHIP/EVENT/STORY/TECHNIQUE를 근거 없이 채우지 않음

## 한계
- 원천 파일의 1~166화 개별 episode header는 이번 검증에서 확인되지 않아 boundary status를 `partial_header_verification`으로 유지.
- PVAR 선택 조건은 `HYPOTHESIS`.
- 다음 배치에서 무표지 보정/행동 재판정 반례 필요.
