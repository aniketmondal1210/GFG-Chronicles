# Push Array Elements to Stack and Print While Popping

## Problem Statement
You are given an integer array `arr[]`.  
Your task is to:

1. **Push all elements** of the array into a stack (in the given order).
2. **Pop all elements** from the stack and print them.

Since a stack follows **LIFO (Last In, First Out)**, the output will be the reverse of the input array.

**Note:** Do not print an extra line after printing the result.

---

## Examples

### Example 1
**Input:**  

arr = [1, 2, 3, 4, 5]


**Output:**  

5 4 3 2 1


**Explanation:**  
Elements are popped from the top in the order: 5 → 4 → 3 → 2 → 1.

---

### Example 2
**Input:**  

arr = [1, 6, 43, 1, 2, 0, 5]


**Output:**  

5 0 2 1 43 6 1


---

## Constraints

1 ≤ arr[i] ≤ 10⁷

---
