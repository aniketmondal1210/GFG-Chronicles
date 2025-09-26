# sizeof() Operator in C

## Problem Statement
We need to learn the use of `sizeof()` operator in **C**.  
This operator is a **unary type operator** — it takes only one operand as input and outputs the size (in bytes) of that operand.

You will be given four different variables of different data types:  
- `a` → int  
- `b` → float  
- `c` → double  
- `d` → long long  

Your task is to print the size (in bytes) of these four data types.

---

## Constraints
- 1 ≤ a, b, c ≤ 10^6  
- 1 ≤ d ≤ 10^18  

---

## Example

### Input

a = 5, b = 5.0, c = 2.632424, d = 4


### Output

4 4 8 8


### Explanation
- `sizeof(int)` → 4 bytes  
- `sizeof(float)` → 4 bytes  
- `sizeof(double)` → 8 bytes  
- `sizeof(long long)` → 8 bytes  

---
