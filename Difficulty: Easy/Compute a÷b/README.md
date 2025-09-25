# Division of Two Integers (Precise Double Value)

## Problem Statement
Given two integers `a` and `b`, compute the value of `a / b`.  
- `b` will never be zero.  
- The result must be returned in **double/float format** with precise values.

---

## Constraints
- -10³ ≤ a, b ≤ 10³  
- b ≠ 0  

---

## Examples

### Example 1
**Input:**  

a = 5, b = 2

**Output:**  

2.5


---

### Example 2
**Input:**  

a = 4, b = 4

**Output:**  

1.0


---

## Explanation
- Perform normal division but ensure at least one operand is casted to **double/float** to avoid integer division.  
- This guarantees the result will have decimal precision.

---
