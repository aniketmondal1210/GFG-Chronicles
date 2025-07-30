# Find the Highest Element in a Bitonic Array

## Problem Statement

You are given an integer array `a[]` of size `n`. The array is either:

- Strictly increasing, or  
- Strictly increasing followed by strictly decreasing (bitonic).  

Your task is to find the **highest (peak) element** of the array.

**Note:**  
- All elements are distinct (`a[i] != a[i+1]`).

---

## Examples

### Example 1:
**Input:**  
`n = 11`  
`a = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]`  
**Output:**  
`6`  
**Explanation:**  
The array increases and then decreases. The highest element is `6`.

---

### Example 2:
**Input:**  
`n = 5`  
`a = [1, 2, 3, 4, 5]`  
**Output:**  
`5`  
**Explanation:**  
The array is strictly increasing. The highest element is the last element, `5`.

---

## Constraints

- `2 ≤ n ≤ 10⁶`  
- `1 ≤ a[i] ≤ 10⁶`  

---
