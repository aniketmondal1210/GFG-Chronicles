# Perfect Number Check

## Problem Description

Given a positive integer $n$, check whether $n$ is a **Perfect Number** or not. 

A number is said to be a **Perfect Number** if the sum of all its proper divisors (all factors excluding the number itself) is equal to $n$.

---

## Examples

### Example 1
- **Input:** $n = 6$
- **Output:** `true`
- **Explanation:** Proper divisors of 6 are 1, 2, and 3. Their sum is $1 + 2 + 3 = 6$, which equals $n$.

### Example 2
- **Input:** $n = 10$
- **Output:** `false`
- **Explanation:** Proper divisors of 10 are 1, 2, and 5. Their sum is $1 + 2 + 5 = 8 
eq 10$.

### Example 3
- **Input:** $n = 15$
- **Output:** `false`
- **Explanation:** Proper divisors of 15 are 1, 3, and 5. Their sum is $1 + 3 + 5 = 9 
eq 15$.

---

## Constraints

- $1 \le n \le 10^9$

---
