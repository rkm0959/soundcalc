# 📊 SP1

How to read this report:
- Table rows correspond to security regimes
- Table columns correspond to proof system components
- Cells show bits of security per component
- Proof size estimates are indicative (1 KiB = 1024 bytes)

## zkVM Overview

| Metric | Value | Relevant circuit | Notes |
| --- | --- | --- | --- |
| Final proof size (worst case) | **1267 KiB** | [compress](#compress) | |
| Final bits of security | **100 bits** | [core](#core) | Regime: UDR |

## Circuits

- [core](#core)
- [compress](#compress)

## core

**Parameters:**
- Polynomial commitment scheme: Unknown
- Lookup (logup): lookup

**Proof Size:** 918 KiB (expected) / 1479 KiB (worst case)

| regime | total | lookup | batching | commit round 1 | commit round 10 | commit round 11 | commit round 12 | commit round 13 | commit round 14 | commit round 15 | commit round 16 | commit round 17 | commit round 18 | commit round 19 | commit round 2 | commit round 20 | commit round 21 | commit round 3 | commit round 4 | commit round 5 | commit round 6 | commit round 7 | commit round 8 | commit round 9 | query phase | reduce to dense PCS | zerocheck |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| UDR | 100 | 100 | 100 | 103 | 112 | 113 | 114 | 115 | 116 | 117 | 118 | 119 | 120 | 121 | 104 | 121 | 122 | 105 | 106 | 107 | 108 | 109 | 110 | 111 | 100 | 116 | 112 |


## compress

**Parameters:**
- Polynomial commitment scheme: Unknown
- Lookup (logup): lookup

**Proof Size:** 735 KiB (expected) / 1267 KiB (worst case)

| regime | total | lookup | batching | commit round 1 | commit round 10 | commit round 11 | commit round 12 | commit round 13 | commit round 14 | commit round 15 | commit round 16 | commit round 17 | commit round 18 | commit round 19 | commit round 2 | commit round 20 | commit round 3 | commit round 4 | commit round 5 | commit round 6 | commit round 7 | commit round 8 | commit round 9 | query phase | reduce to dense PCS | zerocheck |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| UDR | 100 | 107 | 100 | 104 | 113 | 114 | 115 | 116 | 117 | 118 | 119 | 120 | 121 | 121 | 105 | 122 | 106 | 107 | 108 | 109 | 110 | 111 | 112 | 100 | 116 | 115 |

