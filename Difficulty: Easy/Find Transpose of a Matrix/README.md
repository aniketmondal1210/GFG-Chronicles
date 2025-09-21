# Transpose of a Square Matrix

## Problem
Given a matrix `mat[][]`, find the transpose of a square matrix of size `N × N`.  
Transpose of a matrix is obtained by changing rows to columns and columns to rows.

You need to do this **in-place** (update the original matrix).

---

## Examples

### Example 1
**Input:**

N = 4
mat[][] = {
{1, 1, 1, 1},
{2, 2, 2, 2},
{3, 3, 3, 3},
{4, 4, 4, 4}
}


**Output:**

{
{1, 2, 3, 4},
{1, 2, 3, 4},
{1, 2, 3, 4},
{1, 2, 3, 4}
}


---

### Example 2
**Input:**

N = 2
mat[][] = {
{1, 2},
{-9, -2}
}


**Output:**

{
{1, -9},
{2, -2}
}


---

## Constraints
- 1 ≤ N ≤ 100  
- -10³ ≤ mat[i][j] ≤ 10³  

---

## Expected Time Complexity
- **O(N × N)**  

## Expected Auxiliary Space
- **O(1)**  

---
