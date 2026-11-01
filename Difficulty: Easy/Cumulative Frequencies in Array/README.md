# Cumulative Frequency of Elements

## Problem Description

Given an array `arr[]` of elements, calculate the cumulative frequency of each distinct element of the array.

*Note:* Cumulative frequency should be taken according to the sorted order of array elements.

---

## Examples

### Example 1
- **Input:** `arr[] = [1, 2, 2, 1, 3, 4]`
- **Output:** `[2, 4, 5, 6]`
- **Explanation:** 
  - Frequencies: `{1: 2, 2: 2, 3: 1, 4: 1}`
  - Sorted distinct elements: `[1, 2, 3, 4]`
  - Cumulative frequencies: `[2, 2+2=4, 4+1=5, 5+1=6]` $\rightarrow$ `[2, 4, 5, 6]`

### Example 2
- **Input:** `arr[] = [1, 2, 1, 2, 1, 2]`
- **Output:** `[3, 6]`
- **Explanation:** 
  - Frequencies: `{1: 3, 2: 3}`
  - Sorted distinct elements: `[1, 2]`
  - Cumulative frequencies: `[3, 3+3=6]` $\rightarrow$ `[3, 6]`

---

## Constraints

- $1 \le \text{arr.size()}, \text{arr}[i] \le 10^5$

---
