# Count Function Calls with Static Variable

## Problem Statement
You are given a function `utility()` which prints `count` every time it is called.  
The function will be called `n` times by the driver code.  
You need to declare the `count` variable in the right place so that it persists across function calls.

---

## Examples

### Example 1
**Input:**  

n = 4

**Output:**  

1 2 3 4


---

### Example 2
**Input:**  

n = 2

**Output:**  

1 2


---

## Explanation
- If we declare `count` as a normal variable inside the function, it will reset each time.  
- We should use a **static variable** inside the function so that it remembers its value across multiple calls.  

---
