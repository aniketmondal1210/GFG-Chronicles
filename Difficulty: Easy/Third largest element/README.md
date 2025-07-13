# Find the Third Largest Element in an Array

## Problem Statement

You are given an array `arr` of positive integers. Your task is to **find the third largest element** in the array.

- If the array has fewer than 3 elements, return `-1`.
- If the array has fewer than 3 **distinct** elements, return that repeating value as the third largest.
- The solution must run in `O(n)` time and use `O(1)` extra space.

---

## Examples

### Example 1
**Input:**  
`arr = [2, 4, 1, 3, 5]`  
**Output:**  
`3`  
**Explanation:**  
The third largest element is 3.

---

### Example 2
**Input:**  
`arr = [10, 2]`  
**Output:**  
`-1`  
**Explanation:**  
Less than 3 elements in the array.

---

### Example 3
**Input:**  
`arr = [5, 5, 5]`  
**Output:**  
`5`  
**Explanation:**  
All values are the same, so the third largest is 5.

---

## Constraints

- `1 ≤ arr.length ≤ 10^5`
- `1 ≤ arr[i] ≤ 10^5`

---

## Expected Time and Space Complexity

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(1)`
