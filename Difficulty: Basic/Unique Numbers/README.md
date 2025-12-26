# Numbers with Unique Digits in a Given Range

## Problem Statement
You are given a range of integers **[L, R]**.  
Your task is to find and return **all numbers whose digits are unique** (no digit repeats within the number).

A number is considered **unique** if each digit appears exactly once.

---

## Examples

### Example 1
**Input:**  

L = 10
R = 20


**Output:**  

10 12 13 14 15 16 17 18 19 20


**Explanation:**  
- `11` is excluded because digit `1` appears twice.
- All other numbers have unique digits.

---

### Example 2
**Input:**  

L = 1
R = 9


**Output:**  

1 2 3 4 5 6 7 8 9


**Explanation:**  
All single-digit numbers have unique digits.

---

## Time and Space Complexity
- **Time Complexity:** `O(N)` where `N = R - L + 1`
- **Auxiliary Space:** `O(1)` (constant space for digit tracking)

---

## Constraints

- 1 ≤ L ≤ R ≤ 10⁴

---
