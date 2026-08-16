# REF-47 source bridge

- source_id: `SRC-DIRECT-001`
- source_hash_sha256: `95d22f155d582ec702142b906161f4b36241627a76cdf858ff9b39cd6d686a4e`
- raw_byte_size: `5927798`
- raw_encoding: `UTF-16`
- line_basis: UTF-16 decode 후 `splitlines` 기준 1-based
- claimed_scope: `1-350`
- verified episode header scope: `ep1 direct boundary verified; 167-350 previously verified`
- boundary_status: `partial_header_verification`

## 전체 회차 재독 위치

| full episode | episode | lines | normalized full-episode sha256 |
|---|---:|---:|---|
| `FULL-EP-REF47-0001` | 1 | 471-862 | `a4085b570676be7cd9fc2e59942651d7ad151d7c62286336445d7654460c1368` |
| `FULL-EP-REF47-0235` | 235 | 126555-126972 | `5dd3a8e2f60155d8d0681f1f24f0b52647bec32c17216614a34464fd9c84b2b9` |
| `FULL-EP-REF47-0269` | 269 | 143231-143724 | `02cc2a442c3c1d1fe9e3c4001ae8ad2ef415add4c08a89d1b3a09005323e34c5` |
| `FULL-EP-REF47-0275` | 275 | 146201-146834 | `546da03584812072642e1ed5759d120f0fd7cd66c389d6f07cd9e3a9fe668946` |
| `FULL-EP-REF47-0297` | 297 | 157503-158510 | `1ce770b1fb5004fabdb9d0f372d82b47644c8787abda90a5b40660449f471cdc` |
| `FULL-EP-REF47-0298` | 298 | 158511-159140 | `c59a5231ce99e2b479875eeefcf2fa583ab21074bc39c81936bf193d9b1b75cd` |
| `FULL-EP-REF47-0318` | 318 | 169913-170380 | `c96ab603a4e912101fc962a630002dc1790c97197f8856f972417bceed5c53b6` |
| `FULL-EP-REF47-0320` | 320 | 170949-171566 | `b67e4ca659893bf70f0dcdb592b048a6b7903993eaa99a043a91deb21c6f1530` |
| `FULL-EP-REF47-0327` | 327 | 174645-175042 | `a1b8891106c3d303506d4abcd786a948c0aa865b0bad242e2392545b31cb4fe6` |
| `FULL-EP-REF47-0328` | 328 | 175043-175492 | `8b505a15a618ecdde9058884a6c247cf193b1ecbaef6de52acd54a2ad2f5276d` |
| `FULL-EP-REF47-0330` | 330 | 175987-176464 | `c7c2eb33901c9989a40ee712c2b7a450b6c7e94e061db19eac67d46a1da268ba` |
| `FULL-EP-REF47-0331` | 331 | 176465-176880 | `4605c6eca8b2dfeb86ca6b95b6edd4bfc07ec12025cffbfb44bc613bd8b91bca` |
| `FULL-EP-REF47-0350` | 350 | 185225-185651 | `40a14817adc65dee5143a9acbd7706b7419b2656bc4ce42e098122a039d32701` |

- ep235/269/275/297/298/318/320/327/328/330/331/350은 이미 검증된 `167-350` episode-header 범위 안에서 각 배치가 회차 시작과 다음 회차 header 또는 source EOF를 다시 확인해 전체 경계를 고정했다.
- 정규화 whole-episode hash는 각 표의 행 범위를 `\n`으로 결합하고 마지막 개행을 붙인 UTF-8 바이트 기준이다. ep1은 기존 직접 검증값을 유지한다.

## 기존 재독 위치

| scene | episode | lines | normalized segment sha256 |
|---|---:|---:|---|
| `SC-REF47-0001` | 245 | 131481-131519 | `ae61fe5c4d8446e3d15735c9d390e3dab5f3f52d2c4877df7e177c8978ea6e14` |
| `SC-REF47-0002` | 253 | 135351-135385 | `23e6d5f71dc69f13d1b0df544f90e49c9a31e05e079bc30b7d3cae55c8647f71` |
| `SC-REF47-0003` | 255 | 136273-136311 | `f37431d6a5aa5fe83339f588e810137d192375fec9cf7cff44ac0c63c28e697d` |
| `SC-REF47-0004` | 319 | 170617-170641 | `95fbb05e830a5cc1f54db3471c569262325f8d043f6be8b9f670cc680b7f1e86` |
| `SC-REF47-0005` | 238 | 128177-128271 | `5279f94828a21fdc4dd7f7b92c6fd2274e0db739fbae710eb4b3057e31dad18d` |
| `SC-REF47-0006` | 251 | 134591-134635 | `570ca0f2b9dd46667e5c3858ac20fcee8a31fda442183fd315a89540e12e77fc` |
| `SC-REF47-0007` | 256 | 137225-137297 | `6439dea638e206cbe02318b38ee7e90d3239e179733225e4da4750534b117a8d` |
| `SC-REF47-0008` | 300 | 159991-160085 | `8d2ef727cb331d1c8846fb6719533de9c5070b2e8416c9411b6d1e3decdea3a0` |
| `SC-REF47-0009` | 228 | 123365-123415 | `d56b42c3faafa8e6a9ec59dc55321d71b3f5baaa235de820cfebe5144ba81468` |
| `SC-REF47-0010` | 269 | 143565-143609 | `ae0957e27377684661db4c8e0c7455f4d1c12b886d97179501151a1d6eb5a740` |
| `SC-REF47-0011` | 307 | 164109-164149 | `22e5624f02bb7e97e0fb4e48ea4262d7afd17dfca903bd6377a9e68ef17f8e7d` |
| `SC-REF47-0012` | 318 | 170359-170377 | `481e7084e2441f5825f4fa3e890f09f42f076403bc315cd54196248f5c961565` |
| `SC-REF47-0013` | 319 | 170397-170425 | `6f55ae60bcf328c97badfdd72a8ef208cf14a6b23ff8ff89a75351a2af78130e` |
| `SC-REF47-0014` | 230 | 124333-124429 | `64b2f3437d61b14216c0bb972d48bd16fe84442e0522fe9865b49134a176df39` |
| `SC-REF47-0015` | 298 | 158903-159005 | `f6ca299d9a6ad557cbeaad6e691dcc230e28b8ff275d41b2f85f2f21b08e64b2` |
| `SC-REF47-0016` | 329 | 175511-175609 | `746325423092914edcd1d7c38c503f14a2133ee02e17fb899e45f0a13467446d` |
| `SC-REF47-0017` | 331 | 176495-176571 | `c659e68a4d5cd9a0ad306ff13332b65433abddce22c80a694bbb3a000fce840d` |

## 저수준 재분류 구간

| PSE | episode | lines | normalized segment sha256 |
|---|---:|---:|---|
| `PSE-REF47-0018` | 328 | 175413-175457 | `1d7013f1320c636aeaf4ed581b2d090415a4e6185b0e459aafacf5b1e18efa1e` |
| `PSE-REF47-0019` | 350 | 185409-185499 | `b9e2274b3bae36847dd8480ab751e5feac1949288727482b03fd3243e7469227` |

`ep1`은 line 471의 episode header와 line 863의 다음 episode header를 직접 확인해 471-862 경계를 검증했다. 이는 기존 `1-166화 개별 episode header 미확정` 상태 전체를 해제하는 것이 아니라 ep1 한 건의 직접 경계 검증만 추가한다.
