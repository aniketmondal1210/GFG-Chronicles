# Bitwise Operators in C++

## Problem Statement
Bitwise operators are useful when we want to work directly with **bits**.  
We are given three positive integers `a`, `b`, and `c`.  
We need to perform the following bitwise operations:

1. `d = a ^ a`  
2. `e = c ^ b`  
3. `f = a & b`  
4. `g = c | (a ^ a)`  
5. `h = ~e`  

Finally, print all 5 results in **different lines** in the order given.

---

## Constraints
- 1 ≤ a, b, c ≤ 10^6  

---

## Example

### Input

a = 4
b = 8
c = 2


### Output

0
10
0
2
-11


### Explanation
- `d = a ^ a = 4 ^ 4 = 0`  
- `e = c ^ b = 2 ^ 8 = 10`  
- `f = a & b = 4 & 8 = 0`  
- `g = c | (a ^ a) = 2 | 0 = 2`  
- `h = ~e = ~(10) = -11`  

---
