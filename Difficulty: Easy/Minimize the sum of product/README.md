# Minimum Sum of Product of Two Arrays

## Problem Statement
You are given two arrays `arr1` and `arr2` of equal size `N`.  
Your task is to find the **minimum possible value** of:

arr1[0] * arr2[0] + arr1[1] * arr2[1] + ... + arr1[N-1] * arr2[N-1]


You are allowed to **shuffle (reorder)** the elements of both arrays.

---

## Example 1
**Input:**

arr1 = [3, 1, 1]
arr2 = [6, 5, 4]


**Output:**

23


**Explanation:**

16 + 15 + 3*4 = 6 + 5 + 12 = 23

This is the minimum possible sum after rearranging the arrays.

---

## Example 2
**Input:**

arr1 = [6, 1, 9, 5, 4]
arr2 = [3, 4, 8, 2, 4]


**Output:**

80


**Explanation:**

29 + 36 + 45 + 44 + 8*1
= 18 + 18 + 20 + 16 + 8
= 80

This is the minimum possible sum.

---

## Expected Time Complexity

O(n log n)


## Expected Auxiliary Space

O(1)


---

## Constraints

- 1 ≤ arr1.size() == arr2.size() ≤ 10⁵
- 1 ≤ arr1[i], arr2[i] ≤ 10⁶


---
