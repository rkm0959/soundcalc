# 📊 DummyWHIR

How to read this report:
- Table rows correspond to security regimes
- Table columns correspond to proof system components
- Cells show bits of security per component
- Proof size estimate is only indicative

**Parameters:**
- Polynomial commitment scheme: WHIR
- Hash size (bits): 256
- Field: Goldilocks²
- Iterations (M): 5
- Folding factor (k): 4
- Constraint degree: 1
- Batch size: 100
- Batching: Powers
- Queries per iteration: [119, 47, 29, 22, 18]
- OOD samples per iteration: [2, 2, 2, 2]
- Total grinding overhead log2: 16.88

**Proof Size Estimate:** 257 KiB, where 1 KiB = 1024 bytes

| regime | total | OOD(i=1) | OOD(i=2) | OOD(i=3) | OOD(i=4) | Shift(i=1) | Shift(i=2) | Shift(i=3) | Shift(i=4) | batching | fin | fold(i=0,s=1) | fold(i=0,s=2) | fold(i=0,s=3) | fold(i=0,s=4) | fold(i=1,s=1) | fold(i=1,s=2) | fold(i=1,s=3) | fold(i=1,s=4) | fold(i=2,s=1) | fold(i=2,s=2) | fold(i=2,s=3) | fold(i=2,s=4) | fold(i=3,s=1) | fold(i=3,s=2) | fold(i=3,s=3) | fold(i=3,s=4) | fold(i=4,s=1) | fold(i=4,s=2) | fold(i=4,s=3) | fold(i=4,s=4) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| UDR | 25 | 219 | 227 | 235 | 243 | 95 | 59 | 43 | 29 | 106 | 25 | 113 | 114 | 115 | 116 | 114 | 115 | 116 | 117 | 115 | 116 | 117 | 118 | 116 | 117 | 118 | 119 | 117 | 118 | 119 | 120 |
| JBR | -17 | 216 | 221 | 226 | 231 | 133 | 132 | 130 | 125 | -17 | 133 | -4 | 2 | 8 | 14 | 5 | 11 | 17 | 23 | 14 | 20 | 26 | 32 | 23 | 29 | 35 | 41 | 32 | 38 | 44 | 50 |
