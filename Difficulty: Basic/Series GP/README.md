# N-th Term of a Geometric Progression (GP)

## Problem Statement
You are given three integers `a`, `r`, and `n`:
- `a` → the first term of a geometric progression (GP),
- `r` → the common ratio,
- `n` → the position of the term to find.

Your task is to calculate the **n-th term** of the GP.  
Since the result can be very large, return the answer modulo **1000000007**.

---

## Examples

### Example 1
**Input:**

a = 2, r = 2, n = 4

**Output:**

16

**Explanation:**  
The GP is `2, 4, 8, 16, 32, ...`.  
The 4th term is `16`.

---

### Example 2
**Input:**

a = 4, r = 3, n = 3

**Output:**

36

**Explanation:**  
The GP is `4, 12, 36, 108, ...`.  
The 3rd term is `36`.

---

## Constraints
- 1 ≤ a, r, n ≤ 10^6

---
