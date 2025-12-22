# Reciprocal String

## Problem Statement
You are given a string `S`.  
Your task is to find the **reciprocal** of the string based on the following rules:

### Reciprocal Rules
- For **uppercase letters (`A`–`Z`)**:
  - Find the distance from `'A'`
  - Move the same distance backward from `'Z'`
- For **lowercase letters (`a`–`z`)**:
  - Find the distance from `'a'`
  - Move the same distance backward from `'z'`
- For **non-alphabetic characters**:
  - The character remains unchanged

Special cases:
- Reciprocal of `'A'` is `'Z'` and vice versa
- Reciprocal of `'a'` is `'z'` and vice versa

---

## Examples

### Example 1
**Input:**  

S = "ab C"


**Output:**  

zy X


**Explanation:**  
- `'a' → 'z'`  
- `'b' → 'y'`  
- `' '` → `' '`  
- `'C' → 'X'`

---

### Example 2
**Input:**  

S = "Ish"


**Output:**  

Rhs


**Explanation:**  
- `'I' → 'R'`  
- `'s' → 'h'`  
- `'h' → 's'`

---

## Time and Space Complexity
- **Time Complexity:** `O(|S|)`
- **Auxiliary Space:** `O(|S|)`

---

## Constraints

1 ≤ |S| ≤ 10⁴

---
