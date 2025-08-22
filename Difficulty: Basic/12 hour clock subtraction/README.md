# Subtraction on a 12-Hour Clock

## Problem
Given two positive integers `num1` and `num2`, subtract `num2` from `num1` **on a 12-hour clock** (0 to 11) instead of a number line.

---

## Constraints
- `1 ≤ num1, num2 ≤ 10^3`  
- Expected Time Complexity: `O(1)`  
- Expected Auxiliary Space: `O(1)`  

---

## Examples

### Example 1
**Input**  

num1 = 7, num2 = 5

**Output**  

2


**Explanation**  
`7 - 5 = 2` → On a 12-hour clock, result is `2`.

---

### Example 2
**Input**  

num1 = 5, num2 = 7

**Output**  

10


**Explanation**  
`5 - 7 = -2` → On a 12-hour clock, `-2 ≡ 10 (mod 12)`.

---
