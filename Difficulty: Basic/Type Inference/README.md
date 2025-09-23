# Type Identification in C++

## Problem Statement
You are given two variables `a` and `b` in a C++ program.  
These variables can be of any datatype (`int`, `long`, `double`, `char`, etc.).  

Your task is to use the **`typeid`** operator to store their type ids into two variables `id1` and `id2`.

---

## Example

### Input

a = 5
b = 's'


### Output

i c


**Explanation:**  
- `a` is of type `int`, so `typeid(a).name()` returns `"i"`.  
- `b` is of type `char`, so `typeid(b).name()` returns `"c"`.  

---

## Constraints
- `a` and `b` can be of any valid C++ fundamental datatype.
- Compiler must support **RTTI (Run-Time Type Information)**.

---
