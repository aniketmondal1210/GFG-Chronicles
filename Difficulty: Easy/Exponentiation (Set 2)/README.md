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
1^1 mod (10^9+7)=1

Example 2

Input:

a = 2

b = 5

Output:

32

Explanation:

2^5 mod (10^9+7)=32

## Time & Space Complexity

Time Complexity: O(log b)

(Each iteration halves the exponent b)

Space Complexity: O(1)

(Constant extra space)

## Constraints
Variable	Range

1 ≤ a ≤ 10⁵

1 ≤ b ≤ 10¹⁶
