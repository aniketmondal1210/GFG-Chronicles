# Divisible by 8

## Problem Statement
You are given a string representation of a decimal number `s`.  
Check whether the number is divisible by **8**.

Return:
- `1` if divisible by 8
- `-1` if not divisible by 8

---

## Examples

### Example 1
**Input:**  
`s = "16"`  
**Output:**  
`1`  

**Explanation:**  
16 ÷ 8 = 2 (No remainder), so it is divisible by 8.

---

### Example 2
**Input:**  
`s = "54141111648421214584416464555"`  
**Output:**  
`-1`  

**Explanation:**  
The number is not divisible by 8.

---

## Constraints
- `1 ≤ |s| ≤ 10^6`

---

## Key Insight
A number is divisible by 8 **if and only if its last three digits form a number divisible by 8**.  
We only need to check the last three digits of the string.

---
