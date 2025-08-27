# Swap ith Element with (i+2)th Element

## Problem Statement
Given an array `arr` of positive integers, the task is to **swap every ith element** of the array with the **(i+2)th element**.

---

## Examples

### Example 1:
**Input:**  

arr = [1, 2, 3]

**Output:**  

[3, 2, 1]

**Explanation:**  
- Swap 1 and 3 → `[3, 2, 1]`  
Only one swap is possible.

---

### Example 2:
**Input:**  

arr = [1, 2, 3, 4, 5]

**Output:**  

[3, 4, 5, 2, 1]

**Explanation:**  
1. Swap 1 and 3 → `[3, 2, 1, 4, 5]`  
2. Swap 2 and 4 → `[3, 4, 1, 2, 5]`  
3. Swap 1 and 5 → `[3, 4, 5, 2, 1]`  

---

## Constraints
- `1 <= arr.size() <= 10^6`  
- `0 <= arr[i] <= 10^9`  

---

## Expected Complexity
- **Time Complexity:** `O(n)`  
- **Auxiliary Space:** `O(1)`  

---
