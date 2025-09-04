# Find Area of Triangle from Three Sides

## Problem Statement
You are given three integers `A`, `B`, and `C` representing the sides of a triangle.  
Your task is to find the **area of the triangle**.

- If the triangle is not valid (triangle inequality fails), return `0.000`.

We use **Heron's Formula** for a valid triangle:

s = (A + B + C)/2
Area = sqrt(s(s - A)(s - B)(s - C))

---

## Examples

### Example 1
**Input:**

A = 2, B = 2, C = 3


**Output:**

1.984


**Explanation:**  
The triangle with sides `2, 2, 3` has semi-perimeter `s = 3.5`.  
Area = √(3.5 × 1.5 × 1.5 × 0.5) = `1.984`.

---

### Example 2
**Input:**

A = 1, B = 3, C = 1


**Output:**

0.000


**Explanation:**  
Triangle inequality fails (`1 + 1 <= 3`), so the triangle cannot exist.  
Area = `0.000`.

---

## Constraints
- `1 ≤ A, B, C ≤ 10^4`

---

## Expected Complexity
- **Time Complexity:** `O(1)`
- **Space Complexity:** `O(1)`

---
