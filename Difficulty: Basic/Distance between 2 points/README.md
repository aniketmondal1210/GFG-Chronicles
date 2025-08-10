# Distance Between Two Points (Rounded Up)

## Problem Statement
Given coordinates of two points `(x1, y1)` and `(x2, y2)` on a Cartesian plane,  
find the **distance** between them, **rounded up** to the nearest integer.

---

## Examples

### Example 1
**Input:**  
`0 0 2 -2`  
**Output:**  
`3`  

**Explanation:**  
The Euclidean distance is:  

{(2 - 0)^2 + (-2 - 0)^2} = {4 + 4} = sqrt{8} approx 2.828

Rounding up gives `3`.

---

### Example 2
**Input:**  
`-20 23 -15 68`  
**Output:**  
`45`  

**Explanation:**  

{(-15 - (-20))^2 + (68 - 23)^2} = {25 + 2025} = {2050} 45.276

Rounding up gives `45`.

---

## Constraints
- `-1000 ≤ x1, y1, x2, y2 ≤ 1000`

---
