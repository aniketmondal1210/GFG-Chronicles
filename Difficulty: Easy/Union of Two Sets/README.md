# Count Elements in Union of Two Sets

## Problem Statement

Given two arrays `a` and `b`, find the **number of distinct elements** in the **union** of these two arrays.  
Union means a set containing **all unique elements** from both arrays.

---

## Examples

### Example 1  
**Input:**  
`a = [1, 2, 3, 4, 5]`  
`b = [1, 2, 3]`  
**Output:**  
`5`  
**Explanation:**  
Union: `{1, 2, 3, 4, 5}` → Count is 5

### Example 2  
**Input:**  
`a = [85, 25, 1, 32, 54, 6]`  
`b = [85, 2]`  
**Output:**  
`7`  
**Explanation:**  
Union: `{1, 2, 6, 25, 32, 54, 85}` → Count is 7

### Example 3  
**Input:**  
`a = [1, 2, 1, 1, 2]`  
`b = [2, 2, 1, 2, 1]`  
**Output:**  
`2`  
**Explanation:**  
Union: `{1, 2}` → Count is 2

---

## Constraints

- `1 ≤ a.size(), b.size() ≤ 10⁶`  
- `0 ≤ a[i], b[i] < 10⁵`
