# Nth Term of a Geometric Progression

## Problem Statement

Given three integers `a`, `r`, and `n` — where:

- `a` is the first term,
- `r` is the common ratio (which is always 2 in this case),
- `n` is the term number —

calculate the **nth term** of the Geometric Progression (G.P.).

The formula for the nth term of a G.P. is:
an = a * r^(n - 1)

Since `r = 2`, the formula simplifies to:

an = a * 2^(n - 1)

---

## Examples

### Example 1

**Input:**  
`a = 2`, `n = 10`  
**Output:**  
`1024`  

**Explanation:**  
`an = 2 * 2^(10 - 1) = 2 * 512 = 1024`

---

## Constraints

- `1 <= a <= 10^6`  
- `1 <= n <= 30`  
- `r = 2` (fixed)
