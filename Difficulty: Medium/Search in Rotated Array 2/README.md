# Search in Sorted and Rotated Array (with Duplicates)

## Problem Statement
You are given a sorted and rotated array `arr[]` and a target `key`.  
The task is to check whether the key is present in the array or not.  

⚠️ Note: The array may contain **duplicate elements**.

---

## Example 1
**Input:**

arr = [3, 3, 3, 1, 2, 3], key = 3


**Output:**

true


**Explanation:**  
`3` is present in the array.

---

## Example 2
**Input:**

arr = [4, 5, 8, 1, 1, 1, 2], key = 6


**Output:**

false


**Explanation:**  
`6` is not present in the array.

---

## Constraints
- `1 ≤ arr.size() ≤ 10^6`  
- `0 ≤ arr[i], key ≤ 10^8`

---

## Expected Complexity
- **Time Complexity:** `O(log n)` (average), but may degrade to `O(n)` due to duplicates  
- **Space Complexity:** `O(1)`

---
