# Merge Two Sorted Halves of an Array

You are given an integer array `arr[]` of size `N`, where **both the first half and the second half are individually sorted**.  
The task is to merge these two sorted halves into a single **fully sorted array**.

---

## Problem Statement

- The array is divided into two sorted parts:  
  - First half of size `k`  
  - Second half of size `N-k`  
- Merge them into one sorted array.  

---

## Examples

### Example 1
**Input:**

N = 6
arr[] = {2, 3, 8, -1, 7, 10}


**Output:**

-1 2 3 7 8 10


**Explanation:**  
- First half `{2, 3, 8}` is sorted  
- Second half `{-1, 7, 10}` is sorted  
- Merged result: `{-1, 2, 3, 7, 8, 10}`  

---

### Example 2
**Input:**

N = 5
arr[] = {-4, 6, 9, -1, 3}


**Output:**

-4 -1 3 6 9


**Explanation:**  
- First half `{-4, 6, 9}` is sorted  
- Second half `{-1, 3}` is sorted  
- Merged result: `{-4, -1, 3, 6, 9}`  

---

## Constraints
- 1 ≤ N ≤ 10⁶  

---

## Expected Complexity
- **Time Complexity:** O(N)  
- **Auxiliary Space:** O(N)  

---
