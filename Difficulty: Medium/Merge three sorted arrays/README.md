# Merge Three Sorted Arrays

## Problem
Given three sorted arrays `a[]`, `b[]` and `c[]` of positive integers, the task is to merge them into a single sorted array.

---

## Constraints
- `1 ≤ a.size(), b.size(), c.size() ≤ 10^4`
- `1 ≤ a[i], b[i], c[i] ≤ 10^5`
- **Expected Time Complexity:** `O(n1 + n2 + n3)`  
- **Expected Auxiliary Space:** `O(n1 + n2 + n3)`

---

## Examples

### Example 1
**Input**

a[] = [1, 2, 3, 4]
b[] = [1, 2, 3, 5]
c[] = [1, 2, 3, 4, 5, 6]


**Output**

[1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 5, 5, 6]


**Explanation**
- Merging these arrays → `[1,1,1,2,2,2,3,3,3,4,4,5,5,6]`.

---

### Example 2
**Input**

a[] = [1, 2]
b[] = [2, 3, 4]
c[] = [4, 5, 6, 7]


**Output**

[1, 2, 2, 3, 4, 4, 5, 6, 7]


**Explanation**
- Merging these arrays → `[1,2,2,3,4,4,5,6,7]`.

---

✅ Time Complexity = `O(n1 + n2 + n3)`  
✅ Space Complexity = `O(n1 + n2 + n3)` (for result array)

---
