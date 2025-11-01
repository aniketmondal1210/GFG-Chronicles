# Modular Exponentiation

## Problem Statement

Given two positive integers **a** and **b**, find:

a^b mod (10^9 + 7)

That is, compute the power of `a` raised to `b`, **modulo 1,000,000,007**.

---

## Examples

### **Example 1**
**Input:**

a = 1

b = 1

Output:

1

Explanation:
1^1 mod (109+7)=1

Example 2

Input:

a = 2

b = 5

Output:

32

Explanation:

25 mod (109+7)=32

25mod(109+7)=32

## Time & Space Complexity

Time Complexity: O(log b)

(Each iteration halves the exponent b)

Space Complexity: O(1)

(Constant extra space)

## Constraints
Variable	Range

a	1 ≤ a ≤ 10⁵

b	1 ≤ b ≤ 10¹⁶
