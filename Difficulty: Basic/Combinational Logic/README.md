# Construct a 6-Input Logic Gate

## Problem Statement
Construct a 6-input logic gate that performs the following logical operation:

(not(A)).B + C.D +E.(not(F))

Where `A`, `B`, `C`, `D`, `E`, and `F` are binary inputs (0 or 1).  
Return the result of this logical expression.

---

## Example 1

**Input:**

A = 1, B = 1, C = 0, D = 0, E = 1, F = 1


**Output:**

0


**Explanation:**
(not(1)).1 + 0.0 +1.(not(1))
= 0

---

## Example 2

**Input:**

A = 1, B = 1, C = 1, D = 1, E = 1, F = 1


**Output:**

1


**Explanation:**
(not(1)).1 + 1.1 +1.(not(1))
= 1

---

## Constraints

0 <= A, B, C, D, E, F <= 1


**Expected Time Complexity:** O(1)  
**Expected Auxiliary Space:** O(1)

---
