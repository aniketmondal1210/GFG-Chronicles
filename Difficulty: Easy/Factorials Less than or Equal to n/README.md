# Factorial Numbers Less Than or Equal to N

## Problem Description

A number $n$ is called a **factorial number** if it is equal to $k!$ for some positive integer $k \ge 1$. The first few factorial numbers are $1, 2, 6, 24, 120, \dots$.

Given a number $n$, return the list of all factorial numbers that are **less than or equal to** $n$.

---

## Examples

### Example 1
- **Input:** `n = 3`
- **Output:** `[1, 2]`
- **Explanation:** 
  - $1! = 1 \le 3$
  - $2! = 2 \le 3$
  - $3! = 6 > 3$ (stop)

### Example 2
- **Input:** `n = 6`
- **Output:** `[1, 2, 6]`
- **Explanation:** 
  - $1! = 1 \le 6$
  - $2! = 2 \le 6$
  - $3! = 6 \le 6$
  - $4! = 24 > 6$ (stop)

---

## Constraints

- $1 \le n \le 10^{18}$

---
