# Base Conversion to Decimal

## Problem Description

Given a string `n` representing a number in base `b`, convert it to its decimal (base 10) equivalent. 

The base `b` can be any integer such that digits are represented using `0-9` and letters `A-Z` (where `'A'` = 10, `'B'` = 11, ..., `'Z'` = 35).

---

## Examples

### Example 1
- **Input:** `b = 2`, `n = "1100"`
- **Output:** `12`
- **Explanation:** $1 	imes 2^3 + 1 	imes 2^2 + 0 	imes 2^1 + 0 	imes 2^0 = 8 + 4 + 0 + 0 = 12$.

### Example 2
- **Input:** `b = 16`, `n = "A"`
- **Output:** `10`
- **Explanation:** `'A'` represents 10 in hexadecimal.

---

## Constraints

- $1 \le b \le 16$
- $1 \le n \le 	ext{decimal equivalent } 10^9$

---
