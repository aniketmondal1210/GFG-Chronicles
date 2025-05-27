# Median of Two Sorted Arrays

## Problem Statement

Given two **sorted arrays** `a[]` and `b[]`, merge them into a single sorted array and return the **median** of the merged array.

The median is:
- The middle element if the total number of elements is odd.
- The average of the two middle elements if the total number of elements is even.

## Examples

### Example 1:
**Input:**  
`a = [-5, 3, 6, 12, 15]`,  
`b = [-12, -10, -6, -3, 4, 10]`  
**Output:**  
`3`  
**Explanation:**  
Merged array = `[-12, -10, -6, -5, -3, 3, 4, 6, 10, 12, 15]`  
Median = `3`

---

### Example 2:
**Input:**  
`a = [2, 3, 5, 8]`,  
`b = [10, 12, 14, 16, 18, 20]`  
**Output:**  
`11`  
**Explanation:**  
Merged array = `[2, 3, 5, 8, 10, 12, 14, 16, 18, 20]`  
Median = `(10 + 12) / 2 = 11`

---

### Example 3:
**Input:**  
`a = []`,  
`b = [2, 4, 5, 6]`  
**Output:**  
`4.5`  
**Explanation:**  
Merged array = `[2, 4, 5, 6]`  
Median = `(4 + 5) / 2 = 4.5`

## Constraints

- `0 ≤ a.length, b.length ≤ 10^6`
- `1 ≤ a[i], b[i] ≤ 10^9`
- `a.length + b.length > 0`
