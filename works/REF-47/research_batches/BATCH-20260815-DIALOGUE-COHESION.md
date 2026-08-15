# REF-47 dialogue cohesion batch

- mode: 작품 전체 왕복 채굴 / dialogue cohesion
- question: 대사가 이어질 때 지문이 단문 행동비트로 과분절되지 않고, 질문·답변이 정보 조회 인터페이스로 기계화되지 않게 하는 원문 선택은 무엇인가
- base_sha_after_cleanup: `579148754098b1563591bc7044222a16b826be43`
- original_pre_cleanup_head: `f9758c9104683b2564edf05e7480199daf553cb4`
- source: `SRC-DIRECT-001`
- reread: ep230,256(existing),298,329,331

## 생성/보강
- source scenes: `SC-REF47-0014~0017`
- PSE: `PSE-REF47-0014~0017`
- PVAR: `PVAR-REF47-0004`
- PROSE: `PRO-REF47-0004`
- existing contrast: `PSE-REF47-0007`

## 핵심 비교
- 질문형 문장이 정보 요청이 아니라 반론·공격·권리 행사가 되는 경우
- 중간·긴 지문 블록이 숨은 동기·권력·정체성 판단을 묶어 다음 발화를 준비하는 경우
- 짧은 반복 대사에 개별 행동비트를 넣지 않고 연쇄 자체를 유지한 뒤 한 번에 압축하는 경우
- 사실 확인 대화가 책임·체면·관계 충돌로 프레임을 이동하는 경우

## 억제
- `대사 뒤 지문을 길게 쓴다`는 길이 공식 금지
- `질문에 직접 답하지 않는다`는 회피 공식 금지
- 행동비트 대신 설명형 심리 문단을 자동 삽입하지 않음
- Macro/Micro/TH 신규 생성 없음
