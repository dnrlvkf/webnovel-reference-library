# 통합 Source Scene 검색 비강제 계약 감사

- date: `2026-08-15`
- mode: `작품 전체 왕복 채굴 / retrieval-contract audit`
- base_sha: `255343d8a51cfccad1d6179b40adf297b4233c3d`
- basis: `REF-47 integrated scene-chain pilot / ep238,256,298,331 reverified`

## 문제
통합 Source Scene이 CHARACTER·RELATIONSHIP·EVENT·PROSE의 실제 연결을 잘 보존할수록, 집필 검색에서 다음 두 실패가 생길 위험이 있다.

1. 현재 장면이 전체 observed chain과 다르다는 이유로 유용한 부분 근거까지 버림.
2. 성공 사례의 beat 순서·대사/지문 조합·권리 이동을 현재 장면에 억지로 맞춤.

## 직접 확인한 기존 방화벽
- 전역 expression retrieval은 native anchor 우선, 구조/표현 분리, 대표·대비·실패 세트, 외부 표면 복제 금지를 이미 요구한다.
- prose realization retrieval은 PVAR를 정답 문형이 아니라 선택 공간 복원용으로 규정한다.
- REF-47 통합 Source Scene은 실제 원문 결합을 보존하지만 기존 파일럿 검색 순서는 `가까운 Source Scene`을 찾게 되어 있어 전체 결합 유사성을 과도하게 우대할 여지가 있었다.

## 보정
- 신규 `indexes/scene_retrieval_contract.md` 생성.
- Source Scene 사슬을 `observed_chain`, 집필용 재현안을 `recommended_chain`으로 구분하고 후자를 금지.
- 장면 전체가 아니라 CHARACTER/RELATIONSHIP/EVENT/STORY/PROSE/reader picture 부분 문제로 검색.
- 모든 후보에 `matched_problem / mismatch_boundary / usable_judgment / do_not_import`를 남김.
- 불일치를 탈락 사유가 아니라 참고 경계로 사용.
- 함께 관찰된 요소를 인과 필수로 승격하지 않음.
- 완전 일치 장면 자동 우대 금지.
- 표현 실현까지 참고할 때 PVAR/PSE를 변형·반례 안전장치로 사용.
- 초고 뒤 `결합 강제 감사` 추가.

## 판정
- `SUPPORTED`: Source Scene의 통합 결합을 연구 증거로 보존하는 것과 집필에서 부분 문제만 가져오는 것은 양립 가능하다.
- `CONTRADICTED`: 현재 장면과 Source Scene의 전체 결합이 맞아야 참고 가치가 있다는 전제.
- `CONTRADICTED`: 성공한 Source Scene의 beat 순서가 집필 장면의 권장 뼈대라는 전제.
- `HOLD`: 새 스키마/새 레코드 타입. 검색 계약과 drafting test로 해결 가능한지 먼저 검증한다.

## 감사 체크
- [x] 기존 Source Scene 원문 근거와 beat 사슬을 삭제하지 않음.
- [x] 외부 장면의 결합을 실행 규칙으로 컴파일하지 않음.
- [x] 부분 일치와 불일치 경계를 모두 검색 정보로 인정.
- [x] PVAR의 변형 기능을 안전장치로 연결.
- [x] 새 기법 ID·새 스키마·새 트랙 생성 없음.
- [x] 다음 테스트에서 `인물 교체 불가능성 / 관계 권리 개별성 / 사건 운동 / 독자 그림 / 결합 복제 여부`를 함께 비교할 수 있음.

## 다음 검증
새 테스트 원고를 작성할 때 서로 다른 Source Scene에서 필요한 부분 문제만 뽑고, 외부 beat 순서를 임시 아웃라인에 복사하지 않은 상태에서 이전 테스트보다 결과가 좋아지는지 확인한다.
