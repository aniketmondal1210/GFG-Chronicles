# Disarium Number

## Problem Statement

A number **N** is called a **Disarium Number** if:


(sum of its digits powered to their respective positions) = N


Positions start from **1 (left to right)**.

Return:
- `1` → If N is Disarium  
- `0` → Otherwise  

---

## Example 1

**Input**

N = 89


**Output**

1


**Explanation**

8¹ + 9² = 8 + 81 = 89


---

## Example 2

**Input**

N = 81


**Output**

0


**Explanation**

8¹ + 1² = 8 + 1 = 9 ≠ 81


---

## ⏱️ Complexity

- **Time Complexity:** `O(log N)`  
  (Number of digits in N)
- **Space Complexity:** `O(1)`

---

## Constraints

- 0 <= N <= 10^8

---
