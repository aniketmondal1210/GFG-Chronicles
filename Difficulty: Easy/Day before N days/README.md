# Day Index n Days Before a Given Day

## Problem Statement

Given two integers `d` and `n`, where:

- `d` is the current day of the week represented as an index:
  - `0` → Sunday
  - `1` → Monday
  - `2` → Tuesday
  - `3` → Wednesday
  - `4` → Thursday
  - `5` → Friday
  - `6` → Saturday

Return the **index** of the day that is `n` days **before** day `d`.

---

## Examples

### Example 1

**Input:**  
`d = 4`, `n = 3`  
**Output:**  
`1`  
**Explanation:**  
3 days before Thursday (4) is Monday (1).

---

### Example 2

**Input:**  
`d = 2`, `n = 19`  
**Output:**  
`4`  
**Explanation:**  
19 days before Tuesday (2) is Thursday (4).

---

## Constraints

- `0 <= d <= 6`  
- `n >= 0`

---
