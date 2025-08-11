# 12 Hour Clock Sum

## Problem Statement

Given two positive integers `num1` and `num2`, find their sum **in 12-hour clock format** instead of a number line.  
In a 12-hour clock:
- Numbers wrap around after 12.
- If the sum is exactly 12, it should be represented as `0`.
- If the sum exceeds 12, it wraps around using modulo 12.

---

## Examples

### Example 1:
**Input:**  
`num1 = 5, num2 = 7`  
**Output:**  
`0`  
**Explanation:**  
`5 + 7 = 12`, which in 12-hour clock format is `0`.

---

### Example 2:
**Input:**  
`num1 = 3, num2 = 5`  
**Output:**  
`8`  
**Explanation:**  
`3 + 5 = 8`, which is still within 12, so it remains `8`.

---

## Constraints
- `1 ≤ num1, num2 ≤ 50`
- Both inputs are integers.

---

## Expected Time Complexity
- **O(1)**

## Expected Auxiliary Space
- **O(1)**

---
