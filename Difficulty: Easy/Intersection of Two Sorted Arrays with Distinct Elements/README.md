# Intersection of Two Sorted Arrays

You are given two **sorted arrays** `a[]` and `b[]`, each containing distinct elements.  
The task is to return the elements in the **intersection** of the two arrays in **sorted order**.  

Intersection = Distinct common elements present in both arrays.  

---

## Examples

### Example 1
**Input:**

a[] = [1, 2, 3, 4, 5]
b[] = [1, 2, 3, 6, 7]


**Output:**

1 2 3


**Explanation:** Distinct common elements in both arrays are `{1, 2, 3}`.  

---

### Example 2
**Input:**

a[] = [2, 3, 4, 5]
b[] = [1, 2, 3, 4]


**Output:**

2 3 4


**Explanation:** Distinct common elements are `{2, 3, 4}`.  

---

### Example 3
**Input:**

a[] = [1]
b[] = [2]


**Output:**

[]


**Explanation:** No common elements.  

---

## Constraints
- 1 ≤ a.size(), b.size() ≤ 10⁵  
- -10⁹ ≤ a[i], b[i] ≤ 10⁹  
- Arrays are sorted, and contain distinct elements.  

---
