# Sum of All Distinct Elements in an Array

## Problem Statement
You are given an array `arr[]` of size `n` such that **each element lies in the range `1` to `n`**.

Your task is to **find the sum of all distinct elements** present in the array.

---

## Examples

### Example 1
**Input:**


arr = [5, 1, 2, 4, 6, 7, 3, 6, 7]


**Output:**


28


**Explanation:**
Distinct elements are:


1, 2, 3, 4, 5, 6, 7

Sum = `1 + 2 + 3 + 4 + 5 + 6 + 7 = 28`

---

### Example 2
**Input:**


arr = [1, 1, 1]


**Output:**


1


**Explanation:**
Only one distinct element exists → `1`

---

## Complexity Analysis
- **Time Complexity:** `O(n)`
- **Auxiliary Space:** `O(1)`

---

## Constraints


- 1 ≤ arr.size() ≤ 10^6
- 1 ≤ arr[i] ≤ arr.size()


---
