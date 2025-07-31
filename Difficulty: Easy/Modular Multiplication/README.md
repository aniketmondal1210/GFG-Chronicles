# Modular Multiplication

## Problem Statement

Given three integers `a`, `b`, and `M`, compute the result of the modular multiplication operation:

(a × b) % M

This operation returns the **remainder** when the product of `a` and `b` is divided by `M`. The result will always be an integer in the range `[0, M - 1]`.

---

## Examples

### Example 1:
**Input:**  
`a = 5, b = 3, M = 11`  
**Output:**  
`4`  
**Explanation:**  
`5 × 3 = 15`  
`15 % 11 = 4`

---

### Example 2:
**Input:**  
`a = 12, b = 15, M = 7`  
**Output:**  
`5`  
**Explanation:**  
`12 × 15 = 180`  
`180 % 7 = 5`

---

## Constraints

- `1 ≤ a, b ≤ 10⁴`  
- `2 ≤ M ≤ 10⁹`

---
