# Binary Search for Element Position

## Problem Statement

Given a **sorted array** `arr` and an integer `k`, find the **position** (0-based index) at which `k` is present in the array using **binary search**.

### Note:
- If there are **multiple occurrences** of `k`, return the **smallest index**.
- If `k` is **not found**, return `-1`.

---

## Examples

### Example 1:

**Input:**  
`arr = [1, 2, 3, 4, 5], k = 4`  
**Output:**  
`3`  
**Explanation:**  
4 appears at index 3.

---

### Example 2:

**Input:**  
`arr = [11, 22, 33, 44, 55], k = 445`  
**Output:**  
`-1`  
**Explanation:**  
445 is not present in the array.

---

### Example 3:

**Input:**  
`arr = [1, 1, 1, 1, 2], k = 1`  
**Output:**  
`0`  
**Explanation:**  
The first occurrence of 1 is at index 0.

---

## Constraints

- `1 ≤ arr.length ≤ 10^5`
- `1 ≤ arr[i] ≤ 10^6`
- `1 ≤ k ≤ 10^6`
