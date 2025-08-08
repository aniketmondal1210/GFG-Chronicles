# Union of Two Arrays (Sorted Order)

## Problem Statement
Given two **unsorted arrays** `a[]` and `b[]` containing **distinct elements**, return the **union** of the two arrays in **sorted order**.

**Note:**  
- The union should contain all **distinct** elements present in either array.
- The result must be **sorted**.

---

## Examples

### Example 1:
**Input:**  
`a = [89, 24, 75, 11, 23]`  
`b = [89, 2, 4]`  

**Output:**  
`[2, 4, 11, 23, 24, 75, 89]`  

**Explanation:**  
Distinct elements from both arrays are `{2, 4, 11, 23, 24, 75, 89}`.

---

### Example 2:
**Input:**  
`a = [1, 2, 3, 4, 5, 6]`  
`b = [3, 4, 5, 6, 7]`  

**Output:**  
`[1, 2, 3, 4, 5, 6, 7]`

---

## Constraints
- `1 ≤ len(a), len(b) ≤ 10^5`
- `1 ≤ a[i], b[i] ≤ 10^5`
- Elements in each array are **distinct**.

---
