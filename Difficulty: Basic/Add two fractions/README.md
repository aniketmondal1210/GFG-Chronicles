# Add Two Fractions and Express in Simplified Form

## Problem Description

Given four integers `num1`, `den1`, `num2`, and `den2`, representing two fractions $\frac{\text{num1}}{\text{den1}}$ and $\frac{\text{num2}}{\text{den2}}$, write a program to find their sum and return the resulting fraction in its **simplest (reduced) form**.

### Output Format
Return the answer as an array/list of two integers:
1. **Numerator** of the resulting fraction.
2. **Denominator** of the resulting fraction.

---

## Examples

### Example 1
- **Input:** `num1 = 1`, `den1 = 500`, `num2 = 2`, `den2 = 500`
- **Output:** `[3, 500]`
- **Explanation:** 
  $$\frac{1}{500} + \frac{2}{500} = \frac{1 + 2}{500} = \frac{3}{500}$$

### Example 2
- **Input:** `num1 = 1`, `den1 = 6`, `num2 = 1`, `den2 = 3`
- **Output:** `[1, 2]`
- **Explanation:** 
  $$\frac{1}{6} + \frac{1}{3} = \frac{1}{6} + \frac{2}{6} = \frac{3}{6} = \frac{1}{2}$$

---

## Constraints

- $1 \le \text{num1}, \text{den1}, \text{num2}, \text{den2} \le 10^4$

---
