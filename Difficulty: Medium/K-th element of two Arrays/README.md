# K-th Element of Two Sorted Arrays

## Problem
You are given two sorted arrays `a[]` and `b[]`, and an integer `k`.  
The task is to find the element that would be at the **k-th** position in the combined sorted array formed by merging both arrays.

---

## Examples

### Example 1
**Input:**

a = [2, 3, 6, 7, 9]
b = [1, 4, 8, 10]
k = 5

**Output:**

6

**Explanation:**
The merged sorted array is:  
`[1, 2, 3, 4, 6, 7, 8, 9, 10]`  
The 5th element is `6`.

---

### Example 2
**Input:**

a = [1, 4, 8, 10, 12]
b = [5, 7, 11, 15, 17]
k = 6

**Output:**

10

**Explanation:**
The merged sorted array is:  
`[1, 4, 5, 7, 8, 10, 11, 12, 15, 17]`  
The 6th element is `10`.

---

## Constraints
- 1 ≤ `a.size()`, `b.size()` ≤ 10^6  
- 1 ≤ `k` ≤ `a.size()` + `b.size()`  
- 0 ≤ `a[i]`, `b[i]` ≤ 10^8  

---
