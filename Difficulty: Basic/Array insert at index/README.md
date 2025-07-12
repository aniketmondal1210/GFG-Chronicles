# Insert an Element at a Given Index in an Array

## Problem Statement

You are given an array `arr` (0-based index) and two positive integers `index` and `val`.  
You need to insert `val` at the given `index`.

---

## Examples

### Example 1

**Input:**  
`arr = [1, 2, 3, 4, 5]`, `index = 5`, `val = 90`  
**Output:**  
`[1, 2, 3, 4, 5, 90]`  
**Explanation:**  
90 is inserted at index 5. After insertion, array becomes `[1, 2, 3, 4, 5, 90]`.

---

### Example 2

**Input:**  
`arr = [1, 2, 3, 4, 5]`, `index = 2`, `val = 90`  
**Output:**  
`[1, 2, 90, 3, 4, 5]`  
**Explanation:**  
90 is inserted at index 2. After insertion, array becomes `[1, 2, 90, 3, 4, 5]`.

---

## Constraints

- `1 ≤ arr.size() ≤ 10^5`
- `0 ≤ element, arr[i] ≤ 10^6`
- `0 ≤ index ≤ arr.size()`
