# Swap Kth Elements

## Problem Statement
Given an array `arr[]`, swap the **kth element from the beginning** with the **kth element from the end**.

> Note: The array uses **1-based indexing**.

---

## Examples

### Example 1
**Input:**

arr = [1, 2, 3, 4, 5, 6, 7, 8]
k = 3

**Output:**

[1, 2, 6, 4, 5, 3, 7, 8]

**Explanation:**  
The 3rd element from the beginning is `3` and from the end is `6`.  
After swapping, array becomes `[1, 2, 6, 4, 5, 3, 7, 8]`.

---

### Example 2
**Input:**

arr = [5, 3, 6, 1, 2]
k = 2

**Output:**

[5, 1, 6, 3, 2]

**Explanation:**  
2nd element from beginning → `3`, 2nd element from end → `1`.  
After swapping, array becomes `[5, 1, 6, 3, 2]`.

---

## Constraints

1 ≤ arr.size(), k ≤ 10^6
-10^9 ≤ arr[i] ≤ 10^9

---
