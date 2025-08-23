# Count Intersection of Two Arrays

## Problem
You are given two **unsorted integer arrays** `a[]` and `b[]`, each consisting of **distinct elements**.  
Your task is to return the **count of elements in the intersection** (common elements) of the two arrays.

**Note:** Intersection of two arrays is defined as the set containing distinct common elements between them.

---

## Constraints
- `1 ≤ a.size(), b.size() ≤ 10^5`
- `1 ≤ a[i], b[i] ≤ 10^5`

---

## Examples

### Example 1
**Input**

a = [89, 24, 75, 11, 23]
b = [89, 2, 4]

**Output**

1

**Explanation:**  
Only `89` is common in both arrays.

---

### Example 2
**Input**

a = [1, 2, 4, 3, 5, 6]
b = [3, 4, 5, 6, 7]

**Output**

4

**Explanation:**  
Common elements are `{3, 4, 5, 6}` → Count = 4.

---

### Example 3
**Input**

a = [20, 10, 30, 50, 40]
b = [15, 25, 30, 20, 35]

**Output**

2

**Explanation:**  
Common elements are `{20, 30}` → Count = 2.

---
