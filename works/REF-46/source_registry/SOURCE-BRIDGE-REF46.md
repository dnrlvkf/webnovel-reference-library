# REF-46 원천 브리지

- work_id: `REF-46`
- identity_exposure: `sealed`
- source_binding_status: `legacy_registry_verified`
- boundary_status: `exact`
- confirmed_scope: `1~917화`
- source_sha256: `9cf9d175c228c02e960a04f3d721f29bb4362b380065f2fd200b828291ba1191`
- encoding: `utf-8`
- legacy_registry: `catalog/tables/reference-registry.csv`

## 경계 주의

레거시 원천 레지스트리에 기록된 표제 보정을 적용하면 1~917화가 연속한다. 신규 작품 모델은 레거시 실제 식별자를 복사하지 않고 REF 코드와 원문 위치로 재진입한다.

## 이번 연구 재검증 범위

- `118화 / 57,035~57,075행`
- `134화 / 64,520~64,785행`
- `142~143화 / 68,745~69,575행`
- `150화 / 72,545~72,635행`
- `208화 / 101,610~101,660행`
- `360화 / 176,209~176,420행`
- `362화 / 177,157~177,311행`
- `604~606화 / 293,185~293,245행`
- `742~743화 / 349,170~349,330행`
- `817화 / 378,520~378,565행`

selected_segments_sha256: `305f634dc2cc415413d7a1fbaf8652958c0545de95a60a30fbd1c9a323a0618b`

## 연결

- `source_scenes/SOURCE-SCENES-REF46-0001-0010.md`
- `indexes/research.md`

## 이관 경계

이번 배치는 원천 자체를 새 source inventory ID로 재이관하지 않는다. 레거시 레지스트리의 exact boundary와 SHA를 정본 재진입 좌표로 보존하고, 새 `works/` 연구층만 추가한다. source inventory 전면 이관은 별도 migration audit 없이 수행하지 않는다.
