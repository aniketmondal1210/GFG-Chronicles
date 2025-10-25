# Compute (a × b) % c for Large Numbers

## Problem Statement
Given three large integers `a`, `b`, and `c` (each up to 10¹⁸), compute the result of:

(a * b) % c


Since direct multiplication of `a * b` can overflow standard data types, you must use a method that avoids overflow (like modular multiplication).

---

## Examples

### Example 1
**Input:**

a = 4, b = 3, c = 5

**Output:**

2

**Explanation:**

(4 * 3) % 5 = 12 % 5 = 2


---

### Example 2
**Input:**

a = 1000000000007
b = 10000000000005
c = 1000000000000003

**Output:**

74970000000035


---

## Constraints

1 ≤ a, b, c ≤ 10¹⁸


**Expected Time Complexity:** O(log(min(a, b)))  
**Expected Space Complexity:** O(log(min(a, b)))

---

## Explanation
We use **modular multiplication** to avoid overflow.  
Instead of directly computing `a * b`, we repeatedly add `(a % c)` using the **binary exponentiation (doubling)** approach.

### Formula:

(a * b) % c = ((a % c) * (b % c)) % c


To handle large numbers safely:
- Repeatedly double `a` (mod c)
- Add to result only when the corresponding bit of `b` is set

---
