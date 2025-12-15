# Reverse a Subarray

You are given an array `arr[]` and two indices `l` and `r` (1-based indexing).  
Your task is to reverse the elements of the subarray from index `l` to `r` (inclusive).

---

## Examples

### Example 1

Input:
arr = [1, 2, 3, 4, 5, 6, 7]
l = 2, r = 4

Output:
[1, 4, 3, 2, 5, 6, 7]


**Explanation:**  
The subarray `[2, 3, 4]` is reversed to `[4, 3, 2]`.

---

### Example 2

Input:
arr = [1, 6, 7, 4]
l = 1, r = 4

Output:
[4, 7, 6, 1]


**Explanation:**  
The entire array is reversed.

---

### Constraints

- 1 ≤ arr.size() ≤ 10^6
- 1 ≤ arr[i] ≤ 10^6
- 1 ≤ l ≤ r ≤ arr.size()

---
