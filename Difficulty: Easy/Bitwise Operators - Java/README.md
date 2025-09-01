# Bitwise Operators Problem

## Problem Statement
Bitwise operators are useful when we want to work with **bits**.  
Given three positive integers `a`, `b` and `c`, perform the following bitwise operations:

1. `d = a ^ a`  
2. `e = c ^ b`  
3. `f = a & b`  
4. `g = c | (a ^ a)`  
5. `h = ~e`  

Here,  
- `^` → Bitwise XOR  
- `&` → Bitwise AND  
- `|` → Bitwise OR  
- `~` → Bitwise NOT  

---

## Example 1
**Input:**  

a = 4, b = 8, c = 2


**Output:**  

0
10
0
2
-11


**Explanation:**  
- `d = a ^ a = 4 ^ 4 = 0`  
- `e = c ^ b = 2 ^ 8 = 10`  
- `f = a & b = 4 & 8 = 0`  
- `g = c | (a ^ a) = 2 | 0 = 2`  
- `h = ~e = ~10 = -11`  

---

## Example 2
**Input:**  

a = 7, b = 7, c = 7


**Output:**  

0
0
7
7
-1


**Explanation:**  
- `d = 7 ^ 7 = 0`  
- `e = 7 ^ 7 = 0`  
- `f = 7 & 7 = 7`  
- `g = 7 | (7 ^ 7) = 7 | 0 = 7`  
- `h = ~0 = -1`  

---

## Constraints
- `1 <= a, b, c <= 10^6`

---
