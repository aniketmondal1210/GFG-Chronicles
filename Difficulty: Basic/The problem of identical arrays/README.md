# Check if Two Arrays Are Identical

## Problem Statement

Given two arrays `a[]` and `b[]`, determine whether they are **identical** or not.

Two arrays are considered identical if they contain the **same elements** with the **same frequencies**, regardless of the order of elements.

---

## Examples

### Example 1  
**Input:**  
`a = [1, 2, 3, 4, 5]`  
`b = [3, 4, 1, 2, 5]`  
**Output:**  
`true`  
**Explanation:**  
Array `b` is a permutation of array `a`, so both arrays are identical.

---

### Example 2  
**Input:**  
`a = [1, 2, 4]`  
`b = [3, 2, 1]`  
**Output:**  
`false`  
**Explanation:**  
Array `b` does not contain `4` and has an extra `3`, so they are not identical.

---

## Constraints

- `1 ≤ a.length, b.length ≤ 10^5`
- `a.length == b.length`
- `1 ≤ a[i], b[i] ≤ 10^5`

---
