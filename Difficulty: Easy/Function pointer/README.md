# Function Pointer Problem - Add or Subtract

## Problem Statement
Here two integers `a` and `b` are given. Their values are passed as arguments to the function `compute()` along with a **function pointer**.  
The `compute()` function should print `(a-b)` or `(a+b)` as per function calls followed by a new line.  

The `main()` function will make two calls:  
- `compute(a, b, sub)`  
- `compute(a, b, add)`  

---

## Example 1
**Input:**  

a = 2
b = 3


**Output:**  

-1
5


**Explanation:**  
- First call: `compute(a, b, sub)` → `2 - 3 = -1`  
- Second call: `compute(a, b, add)` → `2 + 3 = 5`  

---
