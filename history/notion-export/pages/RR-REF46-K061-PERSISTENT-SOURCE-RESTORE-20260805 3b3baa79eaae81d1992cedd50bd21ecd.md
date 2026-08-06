# RR-REF46-K061-PERSISTENT-SOURCE-RESTORE-20260805

K회차: K061
결과: APPLIED
관찰 델타: K061 참고작 독서 차단 원인 해소. SCENE-174~177 페이지에 PERSISTENT_SOURCE_ATTACHED 상태와 실제 원문 첨부가 추가됐다. 기존 무효 후보는 복구하지 않았고 CURRENT-STATE·정본·커밋 체인은 전진시키지 않았다.
구현 위치: 03-A SCENE-174~177 원천 페이지 및 차단 기록 REF-READ-BLOCK-JSNG-K061-v001
반례 확인: Yes
비정사: Yes
사용 스레드: TH-REF46-12 · 진실 판정 장치는 발화자의 확신만 인증해 질문권·묵비권·문장 설계가 협상권을 결정한다 (https://app.notion.com/p/TH-REF46-12-3b2baa79eaae8151975ad0c5e1f503a2?pvs=21)
원문 근거: SCENE-174~177의 TH-12 발췌 파일을 원본 ZIP SHA-256 f714793fcea00dc84e11d420bb4a69713e7264df8b2b9260d1a6b473f8f483a4에서 추출했다. 개별 SHA-256은 7e1b33e7…, a68afd67…, ec3c3922…, f9f2c053…로 차단 기록과 일치한다.
이유: 기존 03-A 페이지에는 임시 /mnt/data 경로와 해시만 있어 새 채팅에서 실제 원문을 읽을 수 없었다. 네 실제 발췌 본문을 Notion 파일 첨부로 영속 저장하고 각 원천 페이지에 직접 연결했다.
장면 질문: K061의 ORIGINAL_SCENE_READING에 필요한 REF-46 네 장면이 새 런타임에서도 실제 본문으로 다시 열리는가.
프로젝트 코드: 기법 연구