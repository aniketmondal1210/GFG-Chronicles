# Nth Term of an Arithmetic Progression

## Problem Statement

Given three integers `a`, `d` and `n` — where:

- `a` is the first term,
- `d` is the common difference,
- `n` is the term number —

calculate the **nth term** of the Arithmetic Progression (A.P.).

The formula for the nth term of an A.P. is:

an = a + (n - 1) * d

---

## Examples

### Example 1

**Input:**  
`a = 5`, `d = 2`, `n = 5`  
**Output:**  
`13`  

**Explanation:**  
`an = 5 + (5 - 1) * 2 = 5 + 8 = 13`

---

### Example 2

**Input:**  
`a = 10`, `d = 10`, `n = 101`  
**Output:**  
`1010`

**Explanation:**  
`an = 10 + (101 - 1) * 10 = 10 + 1000 = 1010`

---

## Constraints

- `-10^6 <= a, d <= 10^6`  
- `1 <= n <= 10^6`
