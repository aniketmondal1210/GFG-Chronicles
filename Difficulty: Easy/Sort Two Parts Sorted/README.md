# Merge Two Sorted Parts of an Array

## Problem Description

Given an integer array `arr[]` where the two parts around an unknown break point are individually sorted, merge them into a single sorted array. The break point can be anywhere in the array, including at the beginning or end.

---

## Examples

### Example 1
- **Input:** `arr[] = [2, 3, 8, -1, 7, 10]`
- **Output:** `[-1, 2, 3, 7, 8, 10]`
- **Explanation:** `[2, 3, 8]` and `[-1, 7, 10]` are sorted in the original array. Merging them produces `[-1, 2, 3, 7, 8, 10]`.

### Example 2
- **Input:** `arr[] = [-4, 6, 9, -1, 3]`
- **Output:** `[-4, -1, 3, 6, 9]`
- **Explanation:** `[-4, 6, 9]` and `[-1, 3]` are sorted in the original array. Merging them produces `[-4, -1, 3, 6, 9]`.

### Example 3
- **Input:** `arr[] = [10, 20, 30]`
- **Output:** `[10, 20, 30]`
- **Explanation:** One part is empty and the other is the whole array, which is already sorted.

---

## Constraints

- $1 \le 	{arr.size()} \le 10^6$
- $-10^5 \le 	{arr}[i] \le 10^5$

---
