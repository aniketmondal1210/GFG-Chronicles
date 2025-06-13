# Bitwise Operations

## Problem Statement

Given three positive integers `a`, `b`, and `c`, perform the following bitwise operations:

1. `d = a ^ a`  
2. `e = c ^ b`  
3. `f = a & b`  
4. `g = c | (a ^ a)`  
5. `e = ~e`  

Then, print the values of `d`, `e`, `f`, and `g`, space-separated, followed by a newline.

Note:  
- `^` is the bitwise XOR operator  
- `&` is the bitwise AND operator  
- `|` is the bitwise OR operator  
- `~` is the bitwise NOT (complement) operator

---

## Examples

### Example 1

**Input:**  
`a = 1, b = 2, c = 3`  

**Output:**  
0 -2 0 3

**Explanation:**  
- `d = 1 ^ 1 = 0`  
- `e = 3 ^ 2 = 1`, then `~1 = -2`  
- `f = 1 & 2 = 0`  
- `g = 3 | (1 ^ 1) = 3 | 0 = 3`  

---

### Example 2

**Input:**  
`a = 4, b = 5, c = 6`  

**Output:**  
0 -4 4 6

**Explanation:**  
- `d = 4 ^ 4 = 0`  
- `e = 6 ^ 5 = 3`, then `~3 = -4`  
- `f = 4 & 5 = 4`  
- `g = 6 | (4 ^ 4) = 6 | 0 = 6`  

---

## Constraints

- `1 <= a, b, c <= 10^6`
