# XOR Gate Operation on N Bits

## Problem Statement

Given **N bits** as input to an XOR gate, find the output that will be produced.

### XOR Gate Table

| A | B | A ^ B |
|:-:|:-:|:------:|
| 1 | 1 | 0 |
| 1 | 0 | 1 |
| 0 | 1 | 1 |
| 0 | 0 | 0 |

---

## Example 1

**Input:**

N = 4
arr = [1, 1, 1, 0]


**Output:**

1


**Explanation:**

1 ^ 1 = 0
0 ^ 1 = 1
1 ^ 0 = 1
Hence, output = 1


---

## Example 2

**Input:**

N = 4
arr = [0, 0, 1, 0]


**Output:**

1


**Explanation:**

0 ^ 0 = 0
0 ^ 1 = 1
1 ^ 0 = 1
Hence, output = 1


---

## Constraints

1 <= N <= 1000
Each bit is either 0 or 1


**Expected Time Complexity:** O(N)  
**Expected Space Complexity:** O(1)

---
