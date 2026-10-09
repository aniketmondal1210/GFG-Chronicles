# Minimum Steps to Reach N

## Problem Description

Given a number $n$, find the minimum number of operations required to reach $n$ starting from $0$.

You have two operations available:
- **Double the number:** $x = x \times 2$
- **Add one to the number:** $x = x + 1$

---

## Strategy & Approach

To minimize the total number of operations, work **backwards** from $n$ to $1$:

1. If $n$ is **even**, the most efficient preceding step is division by 2 ($n = n / 2$).
2. If $n$ is **odd**, subtract 1 ($n = n - 1$).
3. Repeat until $n = 0$.

Count each step until $n$ reaches 0.

---

## Examples

### Example 1
- **Input:** $n = 8$
- **Output:** `4`
- **Explanation:** 
  - $0 \to 1$ ($+1$)
  - $1 \to 2$ ($+1$)
  - $2 \to 4$ ($\times 2$)
  - $4 \to 8$ ($\times 2$)
  - Total operations: 4.

### Example 2
- **Input:** $n = 7$
- **Output:** `5`
- **Explanation:** 
  - $0 \to 1$ ($+1$)
  - $1 \to 2$ ($+1$)
  - $2 \to 3$ ($+1$)
  - $3 \to 6$ ($\times 2$)
  - $6 \to 7$ ($+1$)
  - Total operations: 5.

---

## Constraints

- $1 \le n \le 10^6$

---
