# Check Elements in Range

## Problem Statement

You are given an array `arr[]` containing positive elements. Two numbers `A` and `B` define a range.  
Your task is to **check if the array contains all elements in the given range (inclusive)**.

Return `true` if all elements in the range `[A, B]` are present in the array, otherwise return `false`.

---

## Examples

### Example 1  
**Input:**  
`n = 7`, `A = 2`, `B = 5`  
`arr = [1, 4, 5, 2, 7, 8, 3]`  
**Output:**  
`True`  
**Explanation:**  
The array contains all elements from 2 to 5 (i.e. 2, 3, 4, 5).

---

### Example 2  
**Input:**  
`n = 7`, `A = 2`, `B = 6`  
`arr = [1, 4, 5, 2, 7, 8, 3]`  
**Output:**  
`False`  
**Explanation:**  
The array does not contain 6. So it does not have all elements in the range 2 to 6.

---

## Your Task

This is a function problem. You don't need to take any input, as it is already handled by the driver code.  
You just need to complete the function `check_elements()` that takes:
- `arr` (array of integers)
- `n` (number of elements in array)
- `A` (start of range)
- `B` (end of range)  

and returns `True` if all elements in the range `[A, B]` are present in the array, else `False`.

---

## Constraints

- `1 ≤ n ≤ 10^7`

---

## Expected Time and Space Complexity

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(1)` (excluding input and output storage)
