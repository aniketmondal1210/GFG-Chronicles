# Search Element in a Sorted Array

## Problem Statement

You are given a sorted array `arr[]` in **ascending order** and an integer `k`.  
Your task is to determine whether `k` is present in the array or not.

Return `true` if present, otherwise `false`.

---

## Examples

### Example 1:
**Input:**  
`arr = [1, 2, 3, 4, 6]`, `k = 6`  
**Output:**  
`true`  
**Explanation:**  
6 is present in the array at index 4.

---

### Example 2:
**Input:**  
`arr = [1, 2, 4, 5, 6]`, `k = 3`  
**Output:**  
`false`  
**Explanation:**  
3 is not present in the array.

---

### Example 3:
**Input:**  
`arr = [2, 3, 5, 6]`, `k = 1`  
**Output:**  
`false`  
**Explanation:**  
1 is not present in the array.

---

## Constraints

- `1 ≤ arr.size() ≤ 10^6`
- `1 ≤ k ≤ 10^6`
- `1 ≤ arr[i] ≤ 10^6`
- The array is **sorted in ascending order**

---
