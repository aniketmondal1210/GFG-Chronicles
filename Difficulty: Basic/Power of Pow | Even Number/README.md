# Sum of Square of First N Even Natural Numbers

## Problem Description

Given a single integer $n$, calculate the sum of the squares of the first $n$ even natural numbers:

$$\text{Sum} = (2)^2 + (4)^2 + (6)^2 + \dots + (2n)^2$$

---

## Mathematical Derivation

We can factor out $2^2 = 4$ from each term in the series:

$$\sum_{i=1}^{n} (2i)^2 = 4 \sum_{i=1}^{n} i^2$$

Using the standard formula for the sum of the first $n$ square numbers, $\sum_{i=1}^{n} i^2 = \frac{n(n + 1)(2n + 1)}{6}$:

$$\text{Sum} = 4 \times \frac{n(n + 1)(2n + 1)}{6} = \frac{2n(n + 1)(2n + 1)}{3}$$

---

## Examples

### Example 1
- **Input:** $n = 2$
- **Output:** `20`
- **Explanation:** $2^2 + 4^2 = 4 + 16 = 20$.

### Example 2
- **Input:** $n = 3$
- **Output:** `56`
- **Explanation:** $2^2 + 4^2 + 6^2 = 4 + 16 + 36 = 56$.

---

## Constraints

- $1 \le n \le 100$

---
