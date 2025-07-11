# Check if an Array is Palindrome

## Problem Statement

Given an array `arr`, the task is to determine whether the array is a **palindrome** or not.  
An array is said to be a **palindrome** if reversing it results in the same array.

---

## Examples

### Example 1:

**Input:**  
`arr = [1, 2, 3, 2, 1]`

**Output:**  
`true`

**Explanation:**  
The reverse of `[1, 2, 3, 2, 1]` is `[1, 2, 3, 2, 1]`, which is the same as the original. Hence, it is a palindrome.

---

### Example 2:

**Input:**  
`arr = [1, 2, 3, 4, 5]`

**Output:**  
`false`

**Explanation:**  
The reverse of `[1, 2, 3, 4, 5]` is `[5, 4, 3, 2, 1]`, which is not the same as the original. Hence, it is not a palindrome.

---

## Expected Time Complexity

- `O(n)`

## Expected Auxiliary Space

- `O(1)`

---

## Constraints

- `1 ≤ arr.size ≤ 10^6`  
- `1 ≤ arr[i] ≤ 10^9`
