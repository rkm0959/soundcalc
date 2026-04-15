# 📊 SP1

How to read this report:
- Table rows correspond to security regimes
- Table columns correspond to proof system components
- Cells show bits of security per component
- Proof size estimates are indicative (1 KiB = 1024 bytes)

## zkVM Overview

| Metric | Value | Relevant circuit | Notes |
| --- | --- | --- | --- |
| Final proof size (worst case) | **1001 KiB** | [wrap](#wrap) | |
| Final bits of security | **98 bits** | [wrap](#wrap) | Regime: UDR |

## Circuits

- [core](#core)
- [compress](#compress)
- [shrink](#shrink)
- [wrap](#wrap)

## core

**Parameters:**
- Polynomial commitment scheme: Jagged + FRI
- Trace length: $2^{22}$
- Trace width: 3728
- Dense length (inner FRI): $2^{21}$
- Hash size (bits): 248
- Number of queries: 124
- Grinding query phase (bits): 16
- Field: KoalaBear⁴
- Rate (ρ): 0.25
- FRI rounds: 21
- FRI folding factors: [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
- FRI early stop degree: 4
- Number of constraints: 3412
- Dense batch size: 193
- Batching: Affine
- Lookup (logup): lookup

**Proof Size:** 918 KiB (expected) / 1479 KiB (worst case)

| regime | total | lookup | batching | commit round 1 | commit round 10 | commit round 11 | commit round 12 | commit round 13 | commit round 14 | commit round 15 | commit round 16 | commit round 17 | commit round 18 | commit round 19 | commit round 2 | commit round 20 | commit round 21 | commit round 3 | commit round 4 | commit round 5 | commit round 6 | commit round 7 | commit round 8 | commit round 9 | query phase | reduce to dense PCS | zerocheck |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| UDR | 99 | 100 | 99 | 103 | 112 | 113 | 114 | 115 | 116 | 117 | 118 | 119 | 120 | 121 | 104 | 121 | 122 | 105 | 106 | 107 | 108 | 109 | 110 | 111 | 100 | 116 | 112 |


## compress

**Parameters:**
- Polynomial commitment scheme: Jagged + FRI
- Trace length: $2^{21}$
- Trace width: 326
- Dense length (inner FRI): $2^{20}$
- Hash size (bits): 248
- Number of queries: 124
- Grinding query phase (bits): 16
- Field: KoalaBear⁴
- Rate (ρ): 0.25
- FRI rounds: 20
- FRI folding factors: [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
- FRI early stop degree: 4
- Number of constraints: 204
- Dense batch size: 128
- Batching: Affine
- Lookup (logup): lookup

**Proof Size:** 735 KiB (expected) / 1267 KiB (worst case)

| regime | total | lookup | batching | commit round 1 | commit round 10 | commit round 11 | commit round 12 | commit round 13 | commit round 14 | commit round 15 | commit round 16 | commit round 17 | commit round 18 | commit round 19 | commit round 2 | commit round 20 | commit round 3 | commit round 4 | commit round 5 | commit round 6 | commit round 7 | commit round 8 | commit round 9 | query phase | reduce to dense PCS | zerocheck |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| UDR | 100 | 107 | 100 | 104 | 113 | 114 | 115 | 116 | 117 | 118 | 119 | 120 | 121 | 121 | 105 | 122 | 106 | 107 | 108 | 109 | 110 | 111 | 112 | 100 | 116 | 115 |


## shrink

**Parameters:**
- Polynomial commitment scheme: Jagged + FRI
- Trace length: $2^{19}$
- Trace width: 326
- Dense length (inner FRI): $2^{18}$
- Hash size (bits): 248
- Number of queries: 94
- Grinding query phase (bits): 22
- Field: KoalaBear⁴
- Rate (ρ): 0.125
- FRI rounds: 18
- FRI folding factors: [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
- FRI early stop degree: 8
- Number of constraints: 204
- Dense batch size: 128
- Batching: Affine
- Lookup (logup): lookup

**Proof Size:** 529 KiB (expected) / 887 KiB (worst case)

| regime | total | lookup | batching | commit round 1 | commit round 10 | commit round 11 | commit round 12 | commit round 13 | commit round 14 | commit round 15 | commit round 16 | commit round 17 | commit round 18 | commit round 2 | commit round 3 | commit round 4 | commit round 5 | commit round 6 | commit round 7 | commit round 8 | commit round 9 | query phase | reduce to dense PCS | zerocheck |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| UDR | 100 | 109 | 101 | 105 | 114 | 115 | 116 | 117 | 118 | 119 | 120 | 120 | 121 | 106 | 107 | 108 | 109 | 110 | 111 | 112 | 113 | 100 | 116 | 115 |


## wrap

**Parameters:**
- Polynomial commitment scheme: Jagged + FRI
- Trace length: $2^{21}$
- Trace width: 120
- Dense length (inner FRI): $2^{21}$
- Hash size (bits): 248
- Number of queries: 94
- Grinding query phase (bits): 22
- Field: KoalaBear⁴
- Rate (ρ): 0.125
- FRI rounds: 21
- FRI folding factors: [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
- FRI early stop degree: 8
- Number of constraints: 43
- Dense batch size: 64
- Batching: Affine
- Lookup (logup): lookup

**Proof Size:** 580 KiB (expected) / 1001 KiB (worst case)

| regime | total | lookup | batching | commit round 1 | commit round 10 | commit round 11 | commit round 12 | commit round 13 | commit round 14 | commit round 15 | commit round 16 | commit round 17 | commit round 18 | commit round 19 | commit round 2 | commit round 20 | commit round 21 | commit round 3 | commit round 4 | commit round 5 | commit round 6 | commit round 7 | commit round 8 | commit round 9 | query phase | reduce to dense PCS | zerocheck |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| UDR | 98 | 108 | 98 | 102 | 111 | 112 | 113 | 114 | 115 | 116 | 117 | 118 | 119 | 120 | 103 | 120 | 121 | 104 | 105 | 106 | 107 | 108 | 109 | 110 | 100 | 116 | 116 |

