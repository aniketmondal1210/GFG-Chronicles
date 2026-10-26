# Count Elements Between Min and Max

## Problem Description

Given an integer array `arr[]`, the task is to find how many elements should be added such that all elements between the maximum element and minimum element are present in the array.

---

## Examples

### Example 1
- **Input:** `arr[] = [205, 173, 102, 324, 957]`
- **Output:** `851`
- **Explanation:** The maximum element is `957` and the minimum element is `102`. Total elements from `102` to `957` = $854$, out of which $3$ are already present. So the answer is $851$.

### Example 2
- **Input:** `arr[] = [3, 4, 4, 8]`
- **Output:** `3`
- **Explanation:** The maximum element is `8` and the minimum element is `3`. Total elements from `3` to `8` = $6$, out of which $3$ are already present. So the answer is $3$.

### Example 3
- **Input:** `arr[] = [545]`
- **Output:** `0`
- **Explanation:** We don't need to add any elements to the array.

---

## Constraints

- $1 \le \text{arr.size()} \le 10^5$
- $1 \le \text{arr}[i] \le 10^9$

---
