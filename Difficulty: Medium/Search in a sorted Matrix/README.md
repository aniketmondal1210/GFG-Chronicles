# Search in a Strictly Sorted 2D Matrix

## Problem
You are given an `n x m` matrix `mat[][]`, strictly sorted:
- Each row is strictly increasing.
- First element of row `i` is greater than the last element of row `i-1`.
- Given a number `x`, check whether it exists in the matrix.

---

## Constraints
- `1 ≤ n, m ≤ 1000`
- `1 ≤ mat[i][j] ≤ 10^9`
- `1 ≤ x ≤ 10^9`

---

## Examples

### Example 1
**Input**

mat = [[1, 5, 9],
[14, 20, 21],
[30, 34, 43]]
x = 14

**Output**

true

**Explanation**  
14 is present at `mat[1][0]`.

---

### Example 2
**Input**

mat = [[1, 5, 9, 11],
[14, 20, 21, 26],
[30, 34, 43, 50]]
x = 42

**Output**

false

**Explanation**  
42 is not present.

---

### Example 3
**Input**

mat = [[87, 96, 99],
[101, 103, 111]]
x = 101

**Output**

true

**Explanation**  
101 is present at `mat[1][0]`.

---
