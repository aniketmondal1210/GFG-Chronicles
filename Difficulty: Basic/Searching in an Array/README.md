# First Occurrence of Element (1-Based Indexing)

## Problem Statement

Given an integer `k` and an array `arr`, return the **1-based position** of the **first occurrence** of `k` in the array.  
If the element `k` is not present, return `-1`.

---

## Examples

### Example 1
**Input:**  
`k = 16`  
`arr = [9, 7, 16, 16, 4]`  
**Output:**  
`3`  
**Explanation:**  
16 appears at indices 3 and 4 (1-based). First occurrence is at position 3.

---

### Example 2  
**Input:**  
`k = 98`  
`arr = [1, 22, 57, 47, 34, 18, 66]`  
**Output:**  
`-1`  
**Explanation:**  
98 is not found in the array.

---

## Constraints

- `1 ≤ arr.size ≤ 10^6`
- `1 ≤ arr[i] ≤ 10^9`
- `1 ≤ k ≤ 10^6`

---
