# Reverse Alternate Words in a String

## Problem
Given a string `str` consisting of multiple words, reverse every alternate word in the string.  
- The **1st, 3rd, 5th, ... words** remain the same.  
- The **2nd, 4th, 6th, ... words** are reversed.

---

## Constraints
- `1 ≤ str.length() ≤ 10⁴`
- **Expected Time Complexity:** `O(N)` where `N` is the length of `str`
- **Expected Auxiliary Space:** `O(N)`

---

## Examples

### Example 1
**Input**

str = "geeks for geeks"


**Output**

"geeks rof geeks"


**Explanation**  
- `geeks` → unchanged  
- `for` → reversed to `rof`  
- `geeks` → unchanged  

---

### Example 2
**Input**

str = "hello there peter pan"


**Output**

"hello ereht peter nap"


**Explanation**  
- `hello` → unchanged  
- `there` → reversed → `ereht`  
- `peter` → unchanged  
- `pan` → reversed → `nap`  

---
