# Count Character Types in a String

## Problem Statement  
Given a string `S`, write a program to count the occurrence of:  
1. **Uppercase characters**  
2. **Lowercase characters**  
3. **Numeric values (0–9)**  
4. **Special characters**  

👉 Note: There are no white spaces in the string.  

---

## Examples  

### Example 1
**Input:**  

S = "#GeeKs01fOr@gEEks07"


**Output:**  

5
8
4
2


**Explanation:**  
- Uppercase = `5` (G, K, O, E, E)  
- Lowercase = `8` (e, e, s, f, r, g, k, s)  
- Numeric = `4` (0, 1, 0, 7)  
- Special = `2` (#, @)  

---

### Example 2
**Input:**  

S = "GeEkS4GeEkS"


**Output:**  

6
4
1
2


**Explanation:**  
- Uppercase = `6` (G, E, E, S, G, E)  
- Lowercase = `4` (e, k, k, s)  
- Numeric = `1` (4)  
- Special = `2` (*, *)  

---

## Constraints
- `1 ≤ |S| ≤ 10^5`  

---
