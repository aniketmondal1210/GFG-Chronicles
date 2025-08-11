# Sum of Product of (x, y) where floor(n/x) = y

## Problem Statement
Given a positive integer `n`, find the **sum of product** of all pairs `(x, y)` such that:

```bash
\text{floor}\left(\frac{n}{x}\right) = y
```

We need to sum up \( x \times y \) for all valid pairs.

---

## Examples

### Example 1
**Input:**  
`n = 5`  
**Output:**  
`21`  

**Explanation:**  
Possible pairs `(x, y)` are:  
- (1, 5) → 1 × 5 = 5  
- (2, 2) → 2 × 2 = 4  
- (3, 1) → 3 × 1 = 3  
- (4, 1) → 4 × 1 = 4  
- (5, 1) → 5 × 1 = 5  

Sum = 5 + 4 + 3 + 4 + 5 = **21**

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
