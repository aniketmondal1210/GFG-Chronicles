# Product of Max of First Array and Min of Second Array

## Problem Statement

Given two arrays `arr1` and `arr2`, the task is to calculate the **product** of the **maximum element** of the first array `arr1`, and the **minimum element** of the second array `arr2`.

---

## Examples

### Example 1
**Input:**  
`arr1 = [5, 7, 9, 3, 6, 2]`  
`arr2 = [1, 2, 6, 1, 9]`  
**Output:**  
`9`  
**Explanation:**  
- Max of `arr1` is `9`  
- Min of `arr2` is `1`  
- Product = `9 * 1 = 9`

---

### Example 2
**Input:**  
`arr1 = [0, 0, 0, 0]`  
`arr2 = [1, 1, 2]`  
**Output:**  
`0`  
**Explanation:**  
- Max of `arr1` is `0`  
- Min of `arr2` is `1`  
- Product = `0 * 1 = 0`

---

## Constraints

- `1 ≤ arr1.size(), arr2.size() ≤ 10^6`
- `0 ≤ arr1[i], arr2[i] ≤ 10^8`

---

## Expected Complexity

- **Time Complexity:** `O(n + m)`  
- **Auxiliary Space:** `O(1)`
