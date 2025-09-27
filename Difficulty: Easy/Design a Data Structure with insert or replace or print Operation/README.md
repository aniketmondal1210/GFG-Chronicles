# Custom Data Structure Implementation

## Problem Statement
Design a data structure that supports the following operations:

1. **insert(x):** Inserts an element `x` at the end of the data structure.  
2. **print():** Prints all elements of the data structure (space separated).  
3. **replace(x, sequence):** Replaces the **first occurrence** of element `x` with the given sequence.

---

## Example

### Input

insert(3), insert(10), print(), insert(3), replace(3,[1,2,3]), print()


### Output

3 10
1 2 3 10 3


**Explanation**  
- After `insert(3)` and `insert(10)`: Data structure → `[3, 10]`  
- After `print()`: Output → `3 10`  
- After another `insert(3)`: Data structure → `[3, 10, 3]`  
- After `replace(3, [1, 2, 3])`: Data structure → `[1, 2, 3, 10, 3]`  
- After `print()`: Output → `1 2 3 10 3`  

---

## Constraints
- 1 ≤ number of operations ≤ 1000  
- Elements can be integers.  
- Sequence in `replace` will be non-empty.  

---
