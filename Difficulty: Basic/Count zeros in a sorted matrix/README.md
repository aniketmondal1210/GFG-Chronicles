# Count Zeros in a Sorted Binary Matrix

## Problem Statement

Given an N × N binary matrix `A` where each **row and column** is sorted in ascending order, your task is to count the total number of zeros present in the matrix.

---

## Input

- `N`: int — the size of the matrix (0 < N ≤ 10³)
- `A`: List[List[int]] — 2D binary matrix where each row and column is sorted

## Output

- int — the total number of zeros in the matrix

---

## Examples

### Example 1

**Input:**

N = 3
A = [[0, 0, 0],
[0, 0, 1],
[0, 1, 1]]


**Output:**  
`6`

**Explanation:**  
- Row 1: 3 zeros  
- Row 2: 2 zeros  
- Row 3: 1 zero  
Total = 6 zeros

---

### Example 2

**Input:**
N = 2
A = [[1, 1],
[1, 1]]


**Output:**  
`0`

**Explanation:**  
No zeros in the matrix.

---
