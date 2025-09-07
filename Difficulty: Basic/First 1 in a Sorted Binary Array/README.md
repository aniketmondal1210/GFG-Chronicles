# Find First Index of 1 in a Sorted Binary Array

## Problem Statement
You are given a **sorted array** `arr` consisting only of `0`s and `1`s.  
The task is to find the **index (0-based)** of the **first occurrence of `1`** in the array.  

- If `1` is not present in the array, return **-1**.

---

## Examples

### Example 1:
**Input:**  

arr = [0, 0, 0, 0, 0, 0, 1, 1, 1, 1]

**Output:**  

6

**Explanation:**  
The first `1` occurs at index `6`.

---

### Example 2:
**Input:**  

arr = [0, 0, 0, 0]

**Output:**  

-1

**Explanation:**  
There are no `1`s in the array.

---

## Constraints
- 1 ≤ arr.size() ≤ 10^6
- 0 ≤ arr[i] ≤ 1  

---

## Expected Complexity
- **Time Complexity:** O(log (n)) (Binary Search)  
- **Space Complexity:** O(1)

---
