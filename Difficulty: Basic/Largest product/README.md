# Maximum Product of K Contiguous Elements

## Problem Statement
Given an array `arr[]` and an integer `k`,  
find the **maximum product** of any **k contiguous elements** in the array.

---

## Example 1

**Input:**

arr = [1, 2, 3, 4]
k = 2


**Output:**

12


**Explanation:**
Subarrays of size 2:
- 1 × 2 = 2  
- 2 × 3 = 6  
- 3 × 4 = 12  

Maximum product = 12

---

## Example 2

**Input:**

arr = [1, 6, 7, 8]
k = 3


**Output:**

336


**Explanation:**
Subarrays of size 3:
- 1 × 6 × 7 = 42  
- 6 × 7 × 8 = 336  

Maximum product = 336

---

## Expected Time Complexity

O(n)


## Expected Auxiliary Space

O(1)


---

## Constraints

- 1 ≤ arr.size() ≤ 10⁶
- 1 ≤ k ≤ 8
- 1 ≤ arr[i] ≤ 10²


---

## Time and Space Complexity
- **Time Complexity:** `O(n)`
- **Auxiliary Space:** `O(1)`

---
