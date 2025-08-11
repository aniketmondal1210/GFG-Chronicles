# Sum of Product of (x, y) Pairs

## Problem Statement
You are given a positive integer `n`.  
Find the sum of the product of `x` and `y` for all possible pairs `(x, y)` such that:

```bash
floor(n\x) = y
```

---

## Examples

### Example 1
**Input:**  
`n = 5`  
**Output:**  
`21`  

**Explanation:**  
Possible pairs `(x, y)` are:  
(1, 5), (2, 2), (3, 1), (4, 1), (5, 1)  

Sum of products:  
1×5 + 2×2 + 3×1 + 4×1 + 5×1  
= 5 + 4 + 3 + 4 + 5 = **21**  

---

### Example 2
**Input:**  
`n = 10`  
**Output:**  
`87`  

---

## Constraints
- 1 <= n <= 10^6

---
