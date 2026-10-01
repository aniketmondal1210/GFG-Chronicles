# Search in a Row-Column Sorted Matrix

## Problem Description

Given a 2D integer matrix `mat[][]` of size $n 	imes m$, where every row and column is sorted in increasing order, and a target integer `x`, determine if `x` is present in the matrix. Return `true` if found, otherwise `false`.

---

## Examples

### Example 1
- **Input:** `mat = [[3, 30, 38], [20, 52, 54], [35, 60, 69]]`, `x = 62`
- **Output:** `false`
- **Explanation:** 62 is not present in the matrix.

### Example 2
- **Input:** `mat = [[18, 21, 27], [38, 55, 67]]`, `x = 55`
- **Output:** `true`
- **Explanation:** 55 is present at row index 1, column index 1.

### Example 3
- **Input:** `mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]`, `x = 3`
- **Output:** `true`
- **Explanation:** 3 is present at row index 0, column index 2.

---

## Constraints

- $1 \le n, m \le 1000$
- $1 \le 	{mat}[i][j], x \le 10^9$

---
