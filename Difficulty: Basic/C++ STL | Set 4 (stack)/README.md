# Stack Operations in C++

We are given an empty stack **s** and need to implement different operations on it.

---

## 🔹 Operations Supported

1. **`a x`** → Push element `x` onto the stack.  
2. **`b`** → If stack is not empty, pop the top element and print it; otherwise print `-1`.  
3. **`c`** → Print the size of the stack.  
4. **`d`** → If stack is not empty, print the top element; otherwise print `-1`.  

---

## 🔹 Example

### Input

2
5
a 4 a 6 a 7 b c
3
a 55 a 11 d


### Output

7 2
11


---

## 🔹 Explanation

**Test case 1**  
- `a 4` → push `4` → stack = [4]  
- `a 6` → push `6` → stack = [4, 6]  
- `a 7` → push `7` → stack = [4, 6, 7]  
- `b` → pop top = `7` → output `7`, stack = [4, 6]  
- `c` → size = `2` → output `2`  

Final output = `7 2`

**Test case 2**  
- `a 55` → stack = [55]  
- `a 11` → stack = [55, 11]  
- `d` → top element = `11`  

Final output = `11`

---
