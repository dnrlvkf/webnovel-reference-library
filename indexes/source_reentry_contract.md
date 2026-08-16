# 참고작 원문 재진입 계약

> 목적: 파생 연구층에서 찾은 REF·회차·행 좌표가 실제 원문 바이트로 다시 이어지게 하되, 공개 연구 저장소에 원문을 복제하지 않고 `VERIFIED_MATCH`의 의미를 약화시키지 않는다.

## 1. 핵심 원칙

**원천 신원과 원천 접근은 서로 다른 계약이다.**

- `source_id + SHA-256 + byte size + encoding + boundary`는 원천의 **신원(identity)** 을 증명한다.
- repository/path/file ID/project attachment 같은 locator는 이번 실행에서 그 바이트를 실제로 읽을 수 있게 하는 **transport(access)** 다.
- 신원이 맞아도 transport가 없으면 `SOURCE_READY`나 `VERIFIED_MATCH`가 아니다.
- transport가 있어도 실제 읽은 바이트를 canonical identity와 대조하기 전에는 `VERIFIED_MATCH`가 아니다.
- Source Scene·PSE·PVAR·PROSE·Macro·Micro·TH는 원문 대신이 아니라 원문으로 내려가는 검색 좌표다.

## 2. 상태

원천 재진입 상태는 다음 의미로만 사용한다.

- `UNBOUND`: canonical source identity는 있으나 cross-project transport locator가 없다.
- `BOUND_UNVERIFIED`: transport locator는 있으나 현재 실행에서 실제 바이트 대조가 끝나지 않았다.
- `VERIFIED_MATCH`: 현재 실행에서 locator로 읽은 원천의 SHA-256·byte size·encoding이 canonical source identity와 일치한다.
- `SOURCE_LIMITED`: 필요한 원문 전체 재독을 수행할 transport/identity/episode boundary가 없어 이번 reference refresh를 더 진행할 수 없다.
- `REVOKED`: 과거 locator가 더 이상 canonical source identity를 가리키지 않거나 접근 권한이 폐기되었다.

`접근 가능`, `검색 성공`, `파일명이 비슷함`, `회차 수가 같음`은 `VERIFIED_MATCH`가 아니다.

## 3. canonical locator 최소 필드

cross-project transport를 결박할 때는 source inventory 또는 작품 source bridge에 다음 의미를 보존한다.

```yaml
source_access:
  transport_status: "BOUND_UNVERIFIED"
  transport_kind: "github_private | google_drive_private"
  stable_locator: "<repository/path or provider file id>"
  access_control: "<private/owner-only/shared-with-authorized-account>"
  locator_identity_exposure: "sealed"
  expected_source_id: "SRC-..."
  expected_sha256: "..."
  expected_byte_size: 0
  encoding: "utf-8"
  episode_coordinate_basis: "<line/offset/index contract>"
```

- 실제 필드명은 기존 레지스트리 구조에 맞춰도 된다. 핵심은 같은 정보를 잃지 않는 것이다.
- 공개 저장소의 locator에는 실제 작품명·작가명·원문 파일명을 넣지 않는다. source ID와 stable provider ID 같은 opaque 식별자를 사용한다.
- 현재 consumer가 읽을 수 없는 transport 종류를 등록해 놓고 `SOURCE_READY`라고 표시하지 않는다.
- provider locator 자체가 공개되어도 원문 접근 권한은 provider access control로 차단되어야 한다.

## 4. project source와 cross-project transport 구분

ChatGPT 프로젝트에 업로드된 ZIP/TXT 같은 `project_source`는 그 프로젝트 안에서는 직접 원문이 될 수 있다. 그러나 다른 프로젝트가 같은 바이트를 읽을 수 있다는 보장은 없다.

따라서:

- `project_source_zip`, `project_source_file`만 존재하고 공용 접근 locator가 없으면 cross-project 상태는 `UNBOUND`다.
- 연구 프로젝트 안에서 원문을 읽었다는 사실만으로 다른 집필 프로젝트의 `VERIFIED_MATCH`를 대신하지 않는다.
- 다른 프로젝트가 동일 파일을 별도로 업로드했다면 그 실행에서 canonical SHA/size와 다시 대조할 수 있다. 일치하면 그 실행에 한해 `VERIFIED_MATCH`가 가능하다.

## 5. 권장 transport

현재 구조에서는 **접근 제어된 account-scoped transport**를 사용한다.

우선순위:

1. 현재 consumer가 읽을 수 있는 private GitHub source vault
2. 현재 consumer가 읽을 수 있는 private Google Drive raw file
3. 그 밖의 access-controlled provider는 동일한 stable locator + raw-byte verification 계약을 충족할 때만 허용

공통 조건:

- 다른 작품 프로젝트에서도 같은 연결 계정으로 읽을 수 있어야 한다.
- stable locator가 있어야 한다.
- raw source를 공개 라이브러리에 복제하지 않는다.
- provider가 텍스트를 변환하는 방식이 아니라 원본 파일 바이트를 내려받아 SHA-256·byte size를 검증할 수 있어야 한다.
- Google Drive는 native Docs 변환본이 아니라 stored raw file을 사용한다. 파일이 공유되지 않았는지 또는 승인된 계정에만 공유되었는지 metadata로 확인한다.

실제 locator가 존재하고 현재 실행에서 접근 가능한 경우에만 결박한다. placeholder repository/path/file ID를 만들지 않는다.

## 6. `VERIFIED_MATCH` 절차

reference refresh에서 후보 REF를 골랐다면:

1. 같은 `H_REF`의 `REPOSITORY_MANIFEST.yaml`을 읽는다.
2. `registry/works.yaml`에서 작품 source binding과 `source_reentry_status`를 확인한다.
3. source inventory 또는 작품 source bridge에서 canonical `source_id / SHA-256 / byte size / encoding / boundary`를 읽는다.
4. `source_access` locator가 없다면 즉시 `SOURCE_LIMITED`로 닫는다. 파생 연구층만으로 표현 판단을 계속하지 않는다.
5. locator가 있으면 현재 실행에서 실제 raw source bytes를 읽는다.
6. 전체 source identity를 canonical SHA-256·byte size·encoding과 대조한다.
7. 모두 일치할 때만 **현재 실행의** `VERIFIED_MATCH`로 올린다. 레지스트리의 과거 VERIFIED_MATCH는 locator 결박 영수증이지 새 실행의 검증을 생략하는 면허가 아니다.
8. 후보의 정확한 episode boundary를 source bridge/index로 확인한다.
9. **해당 원문 회차 전체를 직접 재독**한다. 선행 제시·후속 회수와 결합하면 필요한 인접 회차까지 확장한다.
10. 원문 재독 뒤에만 `take_judgment / do_not_take_surface / pov_conversion` 등 집필 참고 판정을 남긴다.

## 7. 파생층에서 source까지 내려가는 최소 사슬

모든 집필 검색 후보는 가능한 한 다음 사슬을 복원할 수 있어야 한다.

```text
Macro / Micro / TH / PROSE / PVAR / PSE
→ Source Scene 또는 source_locations
→ REF
→ source_id
→ canonical source identity
→ source_access locator
→ current-run VERIFIED_MATCH
→ full episode reread
```

중간 링크가 하나라도 없으면 누락 위치를 보고하고, 원문 재독을 완료한 것처럼 표현하지 않는다.

## 8. 공개 저장소에 저장하지 않는 것

- 저작권 있는 원문 전체
- 원문 회차 전문
- 실제 작품명이 드러나는 private source path/file name
- 파생 연구만으로 복원 가능한 대량의 연속 원문

PSE·Source Scene은 현행 익명화·인용 최소화 계약을 유지한다. 정확한 표면은 private/project source에서 재독한다.

## 9. transport 변경과 무효화

- source bytes가 바뀌면 새 source identity로 취급하고 SHA/size/boundary를 다시 검증한다.
- locator repository/path/file ID가 바뀌면 `BOUND_UNVERIFIED`로 내려 다시 대조한다.
- 접근 권한이 사라지면 `REVOKED` 또는 `SOURCE_LIMITED`다.
- canonical source identity와 다른 바이트를 자동으로 새 정본으로 승격하지 않는다.
- provider가 파일을 native document로 변환하거나 newline/encoding을 바꾼 사본은 기존 raw identity의 `VERIFIED_MATCH`로 사용하지 않는다.

## 10. 완료 판정

원문 재진입 기반이 완성되었다고 말하려면 다음이 모두 가능해야 한다.

- 연구 후보에서 `source_id`까지 역추적된다.
- `source_id`에서 현재 실행이 읽을 수 있는 locator가 나온다.
- 읽은 실제 바이트와 canonical identity를 대조해 `VERIFIED_MATCH`를 만들 수 있다.
- 후보의 full episode boundary를 찾을 수 있다.
- 다른 작품 프로젝트에서도 같은 절차가 재현된다.

일부 source만 locator가 있으면 **그 source만 transport-ready**다. collection 전체나 다른 REF를 자동 승격하지 않는다.
