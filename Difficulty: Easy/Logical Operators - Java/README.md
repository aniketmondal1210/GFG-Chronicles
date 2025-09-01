# Logical Operators

## Problem Statement
Logical operators are used when we want to check the **truth value** of certain statements.  
They help us evaluate **multiple conditions together**.  

We will learn these three logical operators:
- **AND (`&&`)**
- **OR (`||`)**
- **NOT (`!`)**

These operators always produce either `true` or `false` as output.

---

## Examples

### Example 1
**Input:**  

true false

**Output:**  

false true false


**Explanation:**  
- `true && false → false`  
- `true || false → true`  
- `!(true) && !(false) → false`

---

### Example 2
**Input:**  

true true

**Output:**  

true true false


**Explanation:**  
- `true && true → true`  
- `true || true → true`  
- `!(true) && !(true) → false`

---

## Constraints
- `a, b ∈ {true, false}`  

---
