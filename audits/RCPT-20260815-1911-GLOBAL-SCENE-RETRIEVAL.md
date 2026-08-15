# GLOBAL 연구 영수증 — Source Scene retrieval non-forcing contract

- receipt_id: `RCPT-20260815-1911-GLOBAL-SCENE-RETRIEVAL`
- date_time: `2026-08-15T19:11:00+09:00`
- work_id: `GLOBAL / REF-47 pilot basis`
- mode: `작품 전체 왕복 채굴 / retrieval-contract audit`
- question: `통합 Source Scene의 실제 결합은 보존하되 집필 검색에서 그 결합을 정답·탈락 조건·강제 뼈대로 만들지 않으려면 어떤 검색 계약이 필요한가`
- source_scope: `REF-47 / SRC-DIRECT-001 / ep238,256,298,331 selected ranges reverified; no new source claim`
- base_sha: `255343d8a51cfccad1d6179b40adf297b4233c3d`
- branch: `research/retrieval-nonforcing-contract`
- research_content_sha: `PENDING_BRANCH_COMMIT`
- final_sha: `PENDING_FINAL_CHECKPOINT`
- final_sha_mode: `self_excluding_receipt_finalization`
- remote_status: `pending_merge`
- status: `prepared_for_commit`

## 조회
- project-source SOP v7 / repository contract v1 / work model schema v2 + lock 재검증
- GitHub manifest / current main HEAD
- global `indexes/expression_retrieval.md`
- global `indexes/prose_realization_retrieval.md`
- REF-47 `indexes/source_scenes.md`, README, integrated-scene receipt
- REF-47 ep238,256,298,331 원문 구간 재확인

## 변경
- `indexes/scene_retrieval_contract.md` 신규
- REF-47 `indexes/source_scenes.md`에 observed-chain 비강제·부분 검색·사용 경계·결합 강제 감사 추가
- REF-47 README에 global retrieval contract 연결
- global audit / receipt 추가

## 여섯 트랙 영향
- CHARACTER: 전체 장면 유사성보다 `무엇을 먼저 보는가/무슨 비용을 우선하는가`를 부분 검색 가능하게 함.
- RELATIONSHIP: 원천 장면의 질문·명령·차단권을 현재 관계에 자동 이식하지 않도록 mismatch boundary를 필수화.
- EVENT: 외부 장면의 사건 단계 전체를 복사하지 않고 현재 상태 변경에 필요한 선택만 참고.
- STORY: 원문의 제시 순서는 observed chain으로 보존하지만 대상 장면의 제시 순서로 강제하지 않음.
- PROSE: Source Scene 결합 뒤 PVAR/PSE를 읽어 다른 실현 가능성을 확인하도록 연결.
- TECHNIQUE: 신규 Macro/Micro/TH 없음. 기존 연구 단위를 검색 계약으로 안전하게 연결.

## 판정
- SUPPORTED: 통합 장면 연구와 비강제 집필 검색은 양립 가능.
- CONTRADICTED: 전체 결합 일치가 참고 적격성이라는 전제.
- CONTRADICTED: 성공 장면 beat 순서가 권장 템플릿이라는 전제.
- HOLD: schema v3 또는 새 retrieval record type.

## 다음 질문
부분 검색 계약을 적용한 새 테스트 원고가 이전 테스트보다 캐릭터 고유성·관계 권리·사건 운동·독자 그림을 강화하면서도 외부 Source Scene 결합 복제를 줄이는가.
