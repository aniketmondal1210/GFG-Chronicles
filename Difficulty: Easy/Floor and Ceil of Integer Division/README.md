# Floor and Ceil Division

## Problem Statement
You are given two integers `a` and `b` (where `b ≠ 0`).  
The task is to compute both the **floor division** and **ceiling division** of the expression `a / b`.

- **Floor division**:  
  ⌊ a / b ⌋ → the greatest integer less than or equal to `a / b`.

- **Ceil division**:  
  ⌈ a / b ⌉ → the smallest integer greater than or equal to `a / b`.

---

## Example 1
**Input:**  

a = 5, b = 3


**Output:**  

[1, 2]


**Explanation:**  
- `5 / 3 = 1.666...`  
- Floor = `1`, Ceil = `2`.

---

## Example 2
**Input:**  

a = -7, b = 2


**Output:**  

[-4, -3]


**Explanation:**  
- `-7 / 2 = -3.5`  
- Floor = `-4`, Ceil = `-3`.

---

## Constraints
- `-10^9 ≤ a ≤ 10^9`  
- `-10^9 ≤ b ≤ 10^9`, `b ≠ 0`  

---
