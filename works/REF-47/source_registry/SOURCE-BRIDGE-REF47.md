# REF-47 source bridge

- source_id: `SRC-DIRECT-001`
- source_hash_sha256: `95d22f155d582ec702142b906161f4b36241627a76cdf858ff9b39cd6d686a4e`
- raw_byte_size: `5927798`
- raw_encoding: `UTF-16`
- line_basis: UTF-16 decode 후 `splitlines` 기준 1-based
- claimed_scope: `1-350`
- verified episode header scope: `167-350`
- boundary_status: `partial_header_verification`

## 이번 재독 위치

| scene | episode | lines | normalized segment sha256 |
|---|---:|---:|---|
| `SC-REF47-0001` | 245 | 131481-131519 | `ae61fe5c4d8446e3d15735c9d390e3dab5f3f52d2c4877df7e177c8978ea6e14` |
| `SC-REF47-0002` | 253 | 135351-135385 | `23e6d5f71dc69f13d1b0df544f90e49c9a31e05e079bc30b7d3cae55c8647f71` |
| `SC-REF47-0003` | 255 | 136273-136311 | `f37431d6a5aa5fe83339f588e810137d192375fec9cf7cff44ac0c63c28e697d` |
| `SC-REF47-0004` | 319 | 170617-170641 | `95fbb05e830a5cc1f54db3471c569262325f8d043f6be8b9f670cc680b7f1e86` |

정규화 구간 해시는 해당 행 범위를 `\n`으로 결합하고 마지막 개행을 붙인 UTF-8 바이트 기준이다.
