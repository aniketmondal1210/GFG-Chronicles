# Count Digits That Divide a Number

## Problem
Given a positive integer `n`, count the digits in `n` that divide `n` evenly.  
- Ignore digit `0` (since division by zero is undefined).  
- Return the total number of such digits.

---

## Constraints
- `1 ≤ n ≤ 10^5`

---

## Examples

### Example 1
**Input**  

n = 12

**Output**  

2

**Explanation**  
Digits are `1` and `2`. Both divide `12` evenly → count = 2.

---

### Example 2
**Input**  

n = 2446

**Output**  

1

**Explanation**  
Digits = `2, 4, 4, 6`.  
Only `2` divides `2446` → count = 1.

---

### Example 3
**Input**  

n = 23

**Output**  

0

**Explanation**  
Digits = `2, 3`. Neither divides `23` → count = 0.

---
