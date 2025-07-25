# Check if Number is Sum or Difference of 5s

## Problem Statement

You are given an integer input `N`. You need to determine whether it can be formed using only the sum or difference of the integer `5`.

Allowed operations include:

- 5 + 5  
- 5 + 5 + 5  
- 5 - 5  
- 5 - 5 - 5 + 5 + 5  
- and so on...

In other words, determine if `N` is a multiple of 5.

---

## Examples

### Example 1:
**Input:**  
`N = 10`  
**Output:**  
`YES`  

**Explanation:**  
10 can be expressed as 5 + 5.

---

### Example 2:
**Input:**  
`N = 9`  
**Output:**  
`NO`  

**Explanation:**  
9 cannot be expressed using only sums or differences of 5.

---

## Constraints

- `-10^9 <= N <= 10^9`

---

## Expected Time Complexity

- `O(1)`

## Expected Auxiliary Space

- `O(1)`

---
