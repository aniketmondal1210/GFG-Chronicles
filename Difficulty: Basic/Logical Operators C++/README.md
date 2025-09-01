# Logical Operators with Integers

## Problem Statement
Logical operators are used when we want to check the **truth value** of certain statements.  
They also help us in checking multiple statements together for their **truthness**.

Here we will learn logical operators:
- **AND (`&&`)**
- **OR (`||`)**
- **NOT (`!`)**

These operators produce either **1 (true)** or **0 (false)** as an output when applied to integers.

---

## Example

### Example 1
**Input:**  

a = 6
b = 7


**Output:**  

1 1 0


**Explanation:**  
- `a && b = 1` (since both are non-zero → true)  
- `a || b = 1` (at least one is non-zero → true)  
- `(!a) && (!b) = 0` (since `!6 = 0` and `!7 = 0`, result = 0)  

---

## Constraints
- `1 <= a, b <= 100`

---
