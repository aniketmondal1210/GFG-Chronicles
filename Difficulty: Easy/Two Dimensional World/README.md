# Print 2D Array in Row-Column Order (C++)

## Problem Statement
In C++, a 2D array cannot be passed to a function in the normal way.  
It must be declared with fixed column size or by using other structures like vectors.

Given a 2D array `arr[][]` of size `N x N`, print all elements of the matrix in **row-wise order**.

---

## Input Format
- First line: Integer `N`  
- Next `N` lines: Each contains `N` integers representing the matrix

### Example
**Input**

3

1 2 3

4 5 6

7 8 9


**Output**

1 2 3

4 5 6

7 8 9


---

## Explanation
The elements of the 2D array are printed in the same row-column format in which they are stored.

---

## Constraints
- `1 <= T <= 10`
- `1 <= N <= 100`
- `1 <= arr[i][j] <= 10^6`

---
