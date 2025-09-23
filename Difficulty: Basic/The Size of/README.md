# Using `sizeof` Operator in C++

## Problem Statement
We will learn how to use the `sizeof` operator in C++.  
This operator is a **unary type operator**—it takes only one operand as input and outputs the size (in bytes) of that operand.

You are given **five variables**:
- `a` → `int`  
- `b` → `float`  
- `c` → `double`  
- `l` → `long long`  
- `d` → `string`  

Perform the following steps:

1. Divide `b` by `c`.  
2. Divide `b` by `a`.  
3. Divide `c` by `a`.  
4. Add result of step 3 with `l`.  
5. Print the `sizeof(result)` of each step in a **single line** separated by spaces.  
6. Print `sizeof(d)` and `sizeof(d[3])` separated by a space on the next line.  

---

## Example

### Input:

a = 1
b = 2
c = 3
l = 5
d = gfgc


### Output:

4 8 4 8
32 1


**Explanation:**  
- Step 1: `b / c` → result is `float / double` → promoted to `double` → size = 8 bytes.  
- Step 2: `b / a` → result is `float / int` → promoted to `float` → size = 4 bytes.  
- Step 3: `c / a` → result is `double / int` → promoted to `double` → size = 8 bytes.  
- Step 4: result from step 3 (`double`) + `l` (`long long`) → promoted to `double` → size = 8 bytes.  
- For string:  
  - `sizeof(d)` = size of string object (implementation-dependent, often 32).  
  - `sizeof(d[3])` = size of one character (`char`) → 1 byte.  

---

## Constraints
- `1 <= a, b, c <= 10^6`  
- `1 <= l <= 10^18`  

---
