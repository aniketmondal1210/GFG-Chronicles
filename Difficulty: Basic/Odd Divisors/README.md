# Count Numbers with Odd Number of Divisors

## Problem Description

Given a natural number $n$, count all numbers from $1$ to $n$ that have an **odd number of divisors**.

---

## Key Mathematical Insight

A positive integer $k$ has an **odd number of divisors** if and only if $k$ is a **perfect square**.

### Explanation:
Divisors of any number $k$ usually come in pairs $(d, k/d)$. 
- For example, divisors of $12$ are $(1, 12), (2, 6), (3, 4)$ $
-> 6$ divisors (even).
- However, if $k$ is a perfect square, there exists a divisor $d$ where $d = k/d$ (i.e., $d = \sqrt{k}$). This divisor pairs with itself and is counted only once.
- For example, divisors of $36$ are $(1, 36), (2, 18), (3, 12), (4, 9), (6, 6) 
-> 9 divisors (odd).

Therefore, counting numbers between $1$ and $n$ with an odd number of divisors is equivalent to finding the number of perfect squares $\le n$, which is given by:

$$	{Count} = floor(\sqrt{n})

---

## Examples

### Example 1
- **Input:** $n = 1$
- **Output:** `1`
- **Explanation:** $1$ has 1 divisor $\{1\}$ (odd). $\lfloor \sqrt{1} 
floor = 1$.

### Example 2
- **Input:** $n = 4$
- **Output:** `2`
- **Explanation:** Numbers with an odd number of divisors are $1$ and $4$. $\lfloor \sqrt{4} 
floor = 2$.

---

## Constraints

- $1 \le n \le 10^6$

---
