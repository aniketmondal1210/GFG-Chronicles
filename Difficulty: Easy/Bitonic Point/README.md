# Find the Bitonic Point in an Array

## Problem
Given an array of integers `arr[]` that is first strictly increasing and then maybe strictly decreasing,  
find the **bitonic point**, i.e., the maximum element in the array.

A **Bitonic Point** is the peak element such that:
- All elements before it are strictly increasing.
- All elements after it are strictly decreasing.

It is guaranteed that the array contains **exactly one bitonic point**.

---

## Constraints
- `3 ≤ arr.size() ≤ 10^5`
- `1 ≤ arr[i] ≤ 10^6`

---

## Examples

### Example 1
**Input**

arr = [1, 2, 4, 5, 7, 8, 3]

**Output**

8

**Explanation**  
Before `8`: `[1, 2, 4, 5, 7]` (strictly increasing)  
After `8`: `[3]` (strictly decreasing).  
So the bitonic point = **8**.

---

### Example 2
**Input**

arr = [10, 20, 30, 40, 50]

**Output**

50

**Explanation**  
Only strictly increasing → peak = **last element**.

---

### Example 3
**Input**

arr = [120, 100, 80, 20, 0]

**Output**

120

**Explanation**  
Only strictly decreasing → peak = **first element**.

---
