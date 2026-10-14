# Fit Array

## Problem Description

Given two arrays `a[]` and `b[]` of the same size. The array `a[]` will be said to fit in array `b[]` if by arranging the elements of both arrays, there exists a solution such that the $i$-th element of `a[]` is less than or equal to the $i$-th element of `b[]`, for each $i$ ($0 \le i < n$). 

Find if the given array `a[]` can fit in array `b[]` or not.

---

## Examples

### Example 1
- **Input:** `a[] = [7, 5, 3, 2]`, `b[] = [5, 4, 8, 7]`
- **Output:** `true`
- **Explanation:** Rearranging and sorting gives `a[] = [2, 3, 5, 7]` and `b[] = [4, 5, 7, 8]`. Now, $2 \le 4$, $3 \le 5$, $5 \le 7$, and $7 \le 8$. Thus, `a[]` can fit in `b[]`.

### Example 2
- **Input:** `a[] = [1, 2, 4]`, `b[] = [1, 2, 3]`
- **Output:** `false`
- **Explanation:** Here $1 \le 1$ and $2 \le 2$, but $4 > 3$, so `a[]` cannot fit in `b[]`.

---

## Constraints

- $0 \le 	{a.size()}, 	{a}[i], 	{b.size()}, 	{b}[i] \le 10^5$
- $	{b.size()} = {a.size()}$

---
