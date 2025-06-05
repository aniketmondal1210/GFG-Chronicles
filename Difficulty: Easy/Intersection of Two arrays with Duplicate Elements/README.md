# Intersection of Two Arrays

## Problem Statement

Given two integer arrays `a[]` and `b[]`, find the **intersection** of the two arrays.  
Intersection of two arrays is defined as the **elements that are common** in both arrays.  
The intersection should **not have duplicate elements**, and the result can contain items in **any order**.

> Note: The driver code will sort the resulting array in increasing order before printing.

---

## Examples

**Example 1:**

Input:  
`a = [1, 2, 1, 3, 1]`  
`b = [3, 1, 3, 4, 1]`  
Output:  
`[1, 3]`  
Explanation: 1 and 3 are the only common elements, and only one occurrence of each is returned.

---

**Example 2:**

Input:  
`a = [1, 1, 1]`  
`b = [1, 1, 1, 1, 1]`  
Output:  
`[1]`  
Explanation: 1 is the only common element in both arrays.

---

**Example 3:**

Input:  
`a = [1, 2, 3]`  
`b = [4, 5, 6]`  
Output:  
`[]`  
Explanation: No common elements between the two arrays.

---

## Constraints

- `1 ≤ a.length, b.length ≤ 10^5`
- `1 ≤ a[i], b[i] ≤ 10^5`
