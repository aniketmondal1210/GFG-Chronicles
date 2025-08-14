# Union of Two Sorted Arrays (with Duplicates)

## Problem
Given two **sorted** arrays `a[]` and `b[]`, where each array may contain duplicate elements,  
return the union of the two arrays in **sorted order**, with **distinct elements**.

The **union** of two arrays is defined as the set of distinct elements that appear in either array.

---

## Examples

### Example 1
**Input:**

a = [1, 2, 3, 4, 5]
b = [1, 2, 3, 6, 7]

**Output:**

[1, 2, 3, 4, 5, 6, 7]

**Explanation:**  
Distinct elements from both arrays: `1, 2, 3, 4, 5, 6, 7`.

---

### Example 2
**Input:**

a = [2, 2, 3, 4, 5]
b = [1, 1, 2, 3, 4]

**Output:**

[1, 2, 3, 4, 5]

**Explanation:**  
Distinct elements from both arrays: `1, 2, 3, 4, 5`.

---

### Example 3
**Input:**

a = [1, 1, 1, 1, 1]
b = [2, 2, 2, 2, 2]

**Output:**

[1, 2]

**Explanation:**  
Distinct elements from both arrays: `1, 2`.

---

## Constraints
- 1 ≤ `a.size()`, `b.size()` ≤ 10^5  
- -10^9 ≤ `a[i]`, `b[i]` ≤ 10^9  

---
