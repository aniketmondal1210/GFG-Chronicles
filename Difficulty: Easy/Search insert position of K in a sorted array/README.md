# Search Insert Position

## Problem
Given a **sorted array** `arr[]` (0-index based) of distinct integers and an integer `k`,  
find the **index of k** if it is present in the array.  
If not, return the index where `k` should be inserted to maintain sorted order.

---

## Constraints
- `1 ≤ arr.size() ≤ 10^4`  
- `-10^3 ≤ arr[i] ≤ 10^3`  
- `-10^3 ≤ k ≤ 10^3`  
- **Expected Time Complexity:** `O(log N)`  
- **Expected Auxiliary Space:** `O(1)`  

---

## Examples

### Example 1
**Input**

arr[] = [1, 3, 5, 6], k = 5

**Output**

2

**Explanation**  
Since `5` is present at index `2`, the answer is `2`.

---

### Example 2
**Input**

arr[] = [1, 3, 5, 6], k = 2

**Output**

1

**Explanation**  
`2` is not present, but inserting it at index `1` keeps the array sorted.

---

### Example 3
**Input**

arr[] = [2, 6, 7, 10, 14], k = 15

**Output**

5

**Explanation**  
`15` is not present, inserting it after index `4` keeps the array sorted.

---
