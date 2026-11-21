# Nth Pell Number

## Problem Description

Given an integer `n`, find the `n`-th Pell number. The Pell sequence is defined by the recurrence:

- $P_0 = 0$
- $P_1 = 1$
- $P_n = 2 \times P_{n-1} + P_{n-2}$ for all $n \ge 2$

Since the result can grow very large, return $P_n \bmod (10^9 + 7)$.

---

## Examples

### Example 1
- **Input:** `n = 3`
- **Output:** `5`
- **Explanation:** $P_0 = 0$, $P_1 = 1$, $P_2 = 2 \times 1 + 0 = 2$, and $P_3 = 2 \times 2 + 1 = 5$.

### Example 2
- **Input:** `n = 4`
- **Output:** `12`
- **Explanation:** $P_0 = 0$, $P_1 = 1$, $P_2 = 2 \times 1 + 0 = 2$, $P_3 = 2 \times 2 + 1 = 5$, and $P_4 = 2 \times 5 + 2 = 12$.

---

## Constraints

- $1 \le n \le 10^5$

---
