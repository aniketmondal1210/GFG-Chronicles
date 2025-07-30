# Find Mean and Median of an Array

## Problem Statement

You are given an array `arr[]` of positive integers. Your task is to:

- Compute the **mean** (average) of the array.
- Compute the **median** (middle element after sorting).

**Note:**  
- Return the **floor value** of both mean and median.

---

## Examples

### Example 1:
**Input:**  
`arr = [1, 2, 19, 28, 5]`  
**Output:**  
`11 5`  
**Explanation:**  
- Mean = floor((1 + 2 + 19 + 28 + 5) / 5) = floor(55 / 5) = 11  
- Median = 5 (middle element after sorting → [1, 2, 5, 19, 28])

---

### Example 2:
**Input:**  
`arr = [2, 8, 3, 4]`  
**Output:**  
`4 3`  
**Explanation:**  
- Mean = floor((2 + 8 + 3 + 4) / 4) = floor(17 / 4) = 4  
- Median = floor((3 + 4) / 2) = floor(7 / 2) = 3  
  (sorted array → [2, 3, 4, 8])

---

## Constraints

- `1 ≤ arr.length ≤ 10⁵`  
- `1 ≤ arr[i] ≤ 10⁴`

---
