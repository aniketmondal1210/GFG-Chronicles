# Sum of All Elements in a Matrix

## Problem Statement

Given a non-null integer matrix `Grid` of dimensions `N x M`, calculate the sum of all its elements.

---

## Examples

### Example 1:
**Input:**  
`N = 2, M = 3`  
`Grid = [[1, 0, 1], [-8, 9, -2]]`  
**Output:**  
`1`  
**Explanation:**  
Sum = 1 + 0 + 1 - 8 + 9 - 2 = 1

---

### Example 2:
**Input:**  
`N = 3, M = 5`  
`Grid = [[1,0,1,0,1], [0,1,0,1,0], [-1,-1,-1,-1,-1]]`  
**Output:**  
`0`  
**Explanation:**  
Sum = 1+0+1+0+1+0+1+0+1+0-1-1-1-1-1 = 0

---

## Your Task

You don't need to read input or print anything.  
Your task is to complete the function `sumOfMatrix()` which takes two integers `N`, `M` and a 2D array `Grid` as input parameters and returns the sum of all the elements of the Grid.

---

## Constraints

- `1 <= N, M <= 1000`  
- `-1000 <= Grid[i][j] <= 1000`

---

## Expected Time Complexity

- `O(N * M)`

## Expected Auxiliary Space

- `O(1)`

---
