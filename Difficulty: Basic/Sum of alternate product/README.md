# Sum of Products of Paired Elements

## Problem Statement

Given an array `arr[]` of **even size** consisting of **positive integers**, your task is to:

1. Sort the array in non-decreasing order.
2. Find the sum of the product of the i-th element from the start and the i-th element from the end.

That is, calculate:  
`arr[0]*arr[n-1] + arr[1]*arr[n-2] + ... + arr[n/2 - 1]*arr[n/2]`

---

## Examples

### Example 1  
**Input:**  
`arr = [9, 2, 8, 4, 5, 7, 6, 0]`  
**Output:**  
`74`  
**Explanation:**  
After sorting: `[0, 2, 4, 5, 6, 7, 8, 9]`  
Sum = `0*9 + 2*8 + 4*7 + 5*6 = 0 + 16 + 28 + 30 = 74`

---

### Example 2  
**Input:**  
`arr = [1, 2, 3, 4]`  
**Output:**  
`10`  
**Explanation:**  
Already sorted: `[1, 2, 3, 4]`  
Sum = `1*4 + 2*3 = 4 + 6 = 10`

---

## Constraints

- `2 ≤ arr.length ≤ 10^5` (array size is even)
- `1 ≤ arr[i] ≤ 10^3`

---
