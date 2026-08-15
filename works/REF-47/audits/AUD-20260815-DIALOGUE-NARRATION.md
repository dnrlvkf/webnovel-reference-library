# REF-47 dialogue–narration allocation 감사

- base_sha: `8ae0a7d18038c387df9c74be94cd6124a4f1807f`
- branch: `research/ref47-dialogue-narration-pilot`
- mode: 작품 전체 왕복 채굴

## 품질 감사
- [x] SOP v7 / schema v2 / repository contract v1 잠금 일치
- [x] 원문 ep238,251,256,300 직접 재독
- [x] 대사 비율이나 짧은 대사 빈도를 성공 규칙으로 만들지 않음
- [x] 지문을 대사로 옮기는 것을 자동 개선으로 판정하지 않음
- [x] 각 PSE에서 발화가 상대의 다음 반응을 어떻게 바꾸는지 기록
- [x] 행동·침묵·환경·사건이 답변/증명 역할을 하는 반례 포함
- [x] 기술 인과를 지문으로 처리한 대비 사례 포함
- [x] `질문→답변` 고정 문형으로 압축하지 않음
- [x] CHARACTER/RELATIONSHIP의 장기 변화는 이번 표본만으로 새 ID를 만들지 않음

## 판정
- `PVAR-REF47-0002`: 공통 기능과 채널 분산은 SUPPORTED.
- 세부 선택 조건은 일부 HYPOTHESIS 유지.
- 기존 `PVAR-REF47-0001`의 후속 반례 요구 중 `행동·환경·사건이 먼저 재판정하게 하는 사례`는 이번 배치에서 확인.

## 다음 감사 질문
- 정서 고백/친밀 대화에서는 설명과 침묵이 어떤 권리 변화로 작동하는가.
- 장문 대사가 실제로 상대의 프레임을 바꾸지 못하고 독자 설명에 그치는 실패 사례는 있는가.
