# AUDIT-REF46-0027 · 대표직 존속·실행 제약 post-merge 감사

- work_id: `REF-46`
- audit_type: `rights_durability / post_merge`
- base_sha: `889a6c60f06afb0e0030a955e168d42c9dce11c7`
- pr: `#36`
- research_final_sha: `0103a5043f5b4e36f26f9bf060ffe86132f61799`
- status: `PASS`

## 병합 검증

- PR #36이 `main`에 정상 병합됨.
- 연구 변경의 병합 SHA: `0103a5043f5b4e36f26f9bf060ffe86132f61799`.
- 변경 범위는 REF-46 조직 모델, TH-REF46-01, Source Scene 0033~0034, 배치·감사·영수증, 작품 레지스트리와 최근 영수증 인덱스에 한정됨.
- diff 감사 중 `works/REF-46/indexes/research.md`를 과도하게 축약한 중간 변경을 발견했고, 병합 전에 정본 blob으로 완전 복원하여 최종 PR diff에서 제외함.
- 기존 최근 영수증 이력의 삭제는 병합 전에 복원함.

## 연구 판정 재확인

- 낮은 지지: 정책 성공률·지시 수행률·집단 정서에 영향을 주지만 대표직 자동 해임은 관찰되지 않음.
- 정책 실패·내부 이견: 조정·위임·수행 비용은 만들지만 대표직 자동 해임은 관찰되지 않음.
- 장기 부재·실무 공백: 실무 과부하·집단 불안을 만들지만 자동 해임은 관찰되지 않음.
- 외부 정치·법적 압력: 외부 사안의 관할·협상 제약으로 작동하지만 공동체 내부 대표권 회수는 관찰되지 않음.
- 직접 관찰된 대표직 변경 통로는 공식 도전·패배 쪽에 집중됨.

## 산출물 감사

- 신규 Source Scene: `SC-REF46-0033`, `SC-REF46-0034`.
- 보강: `ORG-REF46-0001`, `TH-REF46-01`.
- 미수정: `TH-REF46-05`.
- 신규 CHARACTER / RELATIONSHIP / EVENT / STORY / PROSE / TH / Macro / Micro / PSE / PVAR: 0.
- 신규 파일 수를 성과로 삼지 않고 기존 모델 경계 보강을 우선함.

## 다음 질문

도전권의 경계: 누가 언제 대표에게 도전할 수 있고, 대표의 장기 부재·무능·지지 하락이 실제 도전을 촉발하거나 도전 수락을 강제하는가.

## 결론

`PASS / verified_on_main`. 연구 병합 SHA `0103a5043f5b4e36f26f9bf060ffe86132f61799`를 이번 배치의 `FINAL SHA`로 사용한다.