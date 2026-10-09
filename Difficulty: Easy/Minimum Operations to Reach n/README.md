# Minimum Steps to Reach N

## Problem Description

Given a number $n$, find the minimum number of operations required to reach $n$ starting from $0$.

You have two operations available:
- **Double the number:** $x = x \times 2$
- **Add one to the number:** $x = x + 1$

---

## Examples

### Example 1
- **Input:** $n = 8$
- **Output:** `4`
- **Explanation:** 
  - $0 	o 1$ ($+1$)
  - $1 	o 2$ ($+1$)
  - $2 	o 4$ ($	imes 2$)
  - $4 	o 8$ ($	imes 2$)
  - Total operations: 4.

### Example 2
- **Input:** $n = 7$
- **Output:** `5`
- **Explanation:** 
  - $0 	o 1$ ($+1$)
  - $1 	o 2$ ($+1$)
  - $2 	o 3$ ($+1$)
  - $3 	o 6$ ($	imes 2$)
  - $6 	o 7$ ($+1$)
  - Total operations: 5.

---

## Constraints

- $1 \le n \le 10^6$

---
