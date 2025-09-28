# Pattern Matching with x and y

## Problem Statement
You are given a string `s` consisting only of characters `'x'` and `'y'`.  
Your task is to verify whether the string follows the **pattern** `x^n y^n`.  

This means the string is valid **only if equal numbers of `'y'` immediately follow equal numbers of `'x'`** (like blocks).  

---

## Examples

### Example 1
**Input:**  

s = "xxyy"

**Output:**  

1


---

### Example 2
**Input:**  

s = "xyx"

**Output:**  

0


---

### Example 3
**Input:**  

s = "xxyyxxyy"

**Output:**  

1


---

### Example 4
**Input:**  

s = "xxyyx"

**Output:**  

0


---

## Complexity
- **Time Complexity:** `O(|s|)` (single scan of the string).  
- **Auxiliary Space:** `O(1)` (only counters are used).  

---

## Constraints
- `1 <= |s| <= 100`  
- String contains only characters `'x'` and `'y'`.

---
