# Binomial Coefficient (nCr)

## Problem
Given two integers `n` and `r`, find the value of the binomial coefficient:

```bash
C(n, r) =  nCr 
```

It represents the number of ways to choose `r` objects from a set of `n` objects **without considering the order**.

**Note:**  
- If `r > n`, return `0`.  
- It is guaranteed that the result will fit within a **32-bit integer**.

---

## Examples

### Example 1
**Input:**

n = 5, r = 2

**Output:**

10

**Explanation:**

C(5, 2) = 5! / (3! * 2!) = 10


---

### Example 2
**Input:**

n = 2, r = 4

**Output:**

0

**Explanation:**

Since r > n, result is 0.


---

### Example 3
**Input:**

n = 5, r = 0

**Output:**

1

**Explanation:**

C(5, 0) = 5! / (5! * 0!) = 1


---

## Constraints
- 1 ≤ n ≤ 100  
- 0 ≤ r ≤ 100  

---
