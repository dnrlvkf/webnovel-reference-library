# REF-47 1-166화 회차 경계 검증 레지스트리

- source_id: `SRC-DIRECT-001`
- source_sha256: `95d22f155d582ec702142b906161f4b36241627a76cdf858ff9b39cd6d686a4e`
- raw_byte_size: `5927798`
- raw_encoding: `UTF-16`
- line_basis: UTF-16 decode 후 `splitlines()` 기준 1-based
- scope: `ep1-166`
- verification_status: `VERIFIED_BOUNDARIES`
- verified_next_anchor: `line 92262 / 악당은 살고 싶다 167화`
- boundary_entry_count: `166`
- canonical_boundary_core_sha256: `58d92a04b52dc661e4bbc8d7f4567280cf770976c58a47e8b916d9feb874ff52`
- canonical_boundary_fullmap_sha256: `4b707c2c1ee217c280529a258eee15ba8668a0510839c9459da2e24b1a7303d2`

## 검증 방법

1. 원문 전체를 UTF-16으로 직접 디코드했다.
2. 1-166화의 일반 제목 경계와 비표준 제목 경계를 직접 대조했다.
3. 각 회차의 시작은 직전 회차 종료+1과 맞물리게 하고, ep166 종료 다음 줄이 명시적 `167화` 헤더인지 확인했다.
4. 각 회차 구간은 `\n`으로 결합하고 마지막 개행을 붙인 UTF-8 바이트로 SHA-256을 계산했다.
5. 경계 핵심 직렬화는 `episode,start,end,title,kind`, fullmap 직렬화는 여기에 각 회차 normalized SHA-256을 포함한 JSON compact serialization이다.
6. ep1의 기존 source bridge CRLF legacy hash는 호환을 위해 유지하며, 본 레지스트리의 ep1 값은 LF normalized hash다.

## 비표준·주의 경계

| episode | header line | observed header | 판정 |
|---:|---:|---|---|
| 25 | 11285 | `흔적. (5)` 뒤 유료 시작 장식이 같은 줄에 붙음 | 일반 제목 regex만으로 누락될 수 있어 직접 경계로 포함 |
| 62 | 32173 | 단독 제목 `예행연습.` | `(n)` 표기가 없어 직접 경계로 포함 |
| 68 | 36259 | `< 정리. (2) >` | 꺾쇠 장식 때문에 일반 제목 regex만으로 누락될 수 있어 직접 경계로 포함 |
| 90 | 49827 | `펜던트? (2)` 뒤 중복 업로드 안내만 존재 | source artifact 그대로 한 경계로 보존; 다음 명시 번호와 분리 |
| 91 | 49839 | `91. 펜던트? (2)` | 중복 업로드 교정 뒤 명시된 91화 경계와 일치 |
| 157 | 87382 | 단독 제목 `숲` | `(n)` 표기 없이 직접 경계로 포함 |
| 158 | 87870 | 단독 제목 `숲` | 연속 단독 제목이며 다음 `숲. (3)` 전 별도 경계로 포함 |

## 선택 검증 앵커

| episode | lines | normalized full-episode sha256 | note |
|---:|---:|---|---|
| 1 | 471-862 | `133528e6f6ae7e85964cda2cb08f4f671f90304488edcd47fd0cec5855009570` | LF normalized; legacy CRLF hash는 source bridge에서 별도 보존 |
| 2 | 863-1100 | `0e5a07fbc1c8de84871c3424e8885865c714052d4d34706b95d846137998b64e` | ep1 직후 연속 경계 |
| 25 | 11285-11790 | `b537239cbf699b7b167dc69e9a83145c7142fc70fb7927d6a09e0b3a97f19265` | 유료 시작 장식 경계 |
| 62 | 32173-32964 | `d680b8312d5137d058b5e30a2e8afa845981cb11da80dc38582a9e1e4bdf32cb` | 단독 제목 경계 |
| 68 | 36259-36820 | `2df9bf5f6864e68a37aa1fb8926fd3b8270f66c224f842e59b76a76eb84a5ad1` | 꺾쇠 장식 경계 |
| 78 | 42081-42670 | `b03cdc24a766d86cb138ea538641a9b2edc370c66747def523497372e7188a22` | 이번 신뢰 경계 연구 전체 회차 |
| 90 | 49827-49838 | `dd49777132181ad26c9a5a9630a848cce834f574d09626522362cee2821225aa` | 중복 업로드 안내 artifact |
| 91 | 49839-50482 | `46487d73b6a5b2ceb7fe997e358fb88f25b65bce93e6630a14151f2ee0712cec` | 명시적 91화 교정 경계 |
| 124 | 70003-70422 | `4cba2e2667b123b524761769f757ddb7848d2da03ebbd638a46ec6be96845356` | 제자 역할 복구 연구 전체 회차 |
| 132 | 74015-74668 | `2e156e270f3e1bbbaf9bafff8847d7626d5e827611932abd88277622a68632bb` | 제자 역할 지속 후속 확인 |
| 157 | 87382-87869 | `453e06650bde1fd0c6802e9dd5cb049934e8202ff22348046fde5015658432e4` | 단독 `숲` 경계 |
| 158 | 87870-88307 | `e45f869ccc950095be8198d2d978d4ecdca3a5be3cf5feb5eaa4e83794ebc2f4` | 연속 단독 `숲` 경계 |
| 163 | 90276-90733 | `931fe49d7c5638ebcac466ba161aba7828cf2fc40b90814fddb0843cacef8240` | 관계 상태 오독 연구 전체 회차 |
| 166 | 91672-92261 | `96e4e7874641dbfe814b0539eb2e80c5ec1b45e0d0db3b2189da05faea7c88e7` | 다음 줄 167화 명시 헤더로 종료 검증 |

## 결론

- `DIRECT`: ep1-166은 166개의 연속 회차 경계로 복원된다.
- `DIRECT`: ep166 종료 다음 줄 `92262`는 `악당은 살고 싶다 167화`다.
- `CONTRADICTED`: `(n)`이 붙은 일반 제목만 세면 1-166 경계를 정확히 복원할 수 있다는 가정.
- 본 레지스트리 생성으로 REF-47의 기존 `ep1 direct boundary verified; 167-350 previously verified` 상태는 `ep1-350 episode-header boundaries verified`로 승격 가능하다.
- 이 경계 검증은 서사 연구 판정을 대신하지 않으며, 향후 원문 재진입 좌표의 신뢰도를 높이는 source-registry 작업이다.
