# Find the Nth Term of an Arithmetic Series

## Problem Statement

Given the first two terms `a1` and `a2` of an arithmetic series, find the **nth** term of the series.

---

## Formula

In an Arithmetic Series, the nth term is given by:

Tn = a1 + (n - 1) * d

Where:
- `a1` = first term
- `d` = common difference = `a2 - a1`
- `n` = term to find

---

## Examples

### Example 1:

**Input:**  
`a1 = 2, a2 = 3, n = 4`  
**Output:**  
`5`  
**Explanation:**  
The series is: 2, 3, 4, 5, 6...  
The 4th term is `5`.

---

### Example 2:

**Input:**  
`a1 = 1, a2 = 3, n = 10`  
**Output:**  
`19`  
**Explanation:**  
The series is: 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21...  
The 10th term is `19`.

---

## Constraints

- `-10^4 <= a1, a2 <= 10^4`
- `1 <= n <= 10^4`

---
