# Binary String Modulo

## Problem
You are given:
- A binary string `s`
- An integer `m`

You need to return:

r = k % m

Where:
- `k` is the decimal value of binary string `s`
- `%` is the modulo operator

---

## Examples

### Example 1
**Input:**

s = "101"
m = 2

**Output:**

1

**Explanation:**

Binary "101" = Decimal 5
5 % 2 = 1


---

### Example 2
**Input:**

s = "1000"
m = 4

**Output:**

0

**Explanation:**

Binary "1000" = Decimal 8
8 % 4 = 0


---

## Constraints
- 1 ≤ len(s) ≤ 10⁷
- 1 ≤ m ≤ 100

---

## Expected Complexity
- **Time Complexity:** O(N) — process each bit once  
- **Auxiliary Space:** O(1) — modulo can be computed without storing the full number

---
