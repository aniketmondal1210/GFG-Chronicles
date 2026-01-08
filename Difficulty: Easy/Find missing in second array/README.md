# Elements Present in First Array but Not in Second

## Problem Statement
You are given two integer arrays `a` and `b`.

Your task is to **find all numbers that are present in array `a` but not present in array `b`**.

### Important Notes
- The **relative order** of elements must be the **same as in array `a`**.
- If no such elements exist, return an **empty array**.

---

## Examples

### Example 1
**Input:**

a = [1, 2, 3, 4, 5, 10]
b = [2, 3, 1, 0, 5]


**Output:**

[4, 10]


**Explanation:**  
Elements `4` and `10` appear in `a` but not in `b`.

---

### Example 2
**Input:**

a = [4, 3, 5, 9, 11]
b = [4, 9, 3, 11, 10]


**Output:**

[5]


**Explanation:**  
Only `5` from array `a` is missing in array `b`.

---

### Example 3
**Input:**

a = [9]
b = [7, 9, 4, 9, 9, 9]


**Output:**

[]


**Explanation:**  
All elements of `a` are present in `b`.

---

## Constraints

- 1 <= a.size(), b.size() <= 10^5
- 1 <= a[i], b[i] <= 10^5


---
