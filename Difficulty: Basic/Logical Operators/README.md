# Logical Operators in Python

## Problem Statement

Logical operators `and`, `or`, and `not` are used in condition checking.

- `a and b`: Evaluates to `b` if both `a` and `b` are `True`. If `a` is `False`, returns `a`.
- `a or b`: Evaluates to `a` if `a` is `True`; otherwise evaluates to `b`.
- `not a`: Returns `True` if `a` is `False`, otherwise returns `False`.

Note:  
- `0` and empty strings (`""`) are considered `False`.
- All other values are considered `True`.

You are given two values `a` and `b`. Print:
- The result of `a and b`
- The result of `a or b`
- The result of `not a`

---

## Examples

### Example 1

**Input:**  
`a = 0`  
`b = 2`  

**Output:**  
0 2 True

**Explanation:**  
- `a and b` → `0` (since `a` is `False`)  
- `a or b` → `2` (since `a` is `False`, evaluates `b`)  
- `not a` → `True` (since `a` is `False`)  

---

### Example 2

**Input:**  
`a = 3`  
`b = 4`  

**Output:**  
4 3 False

**Explanation:**  
- `a and b` → `4` (both `a` and `b` are `True`)  
- `a or b` → `3` (`a` is `True`, so returns immediately)  
- `not a` → `False` (since `a` is `True`)  

---

## Constraints

- `a` and `b` can be integers or strings.
