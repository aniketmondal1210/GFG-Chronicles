# Sort Character Array According to Integer Array

## Problem Statement
You are given two arrays:  
- `a[]` (integer)  
- `b[]` (char)  

The `i`th value of `a[]` corresponds to the `i`th value of `b[]`.  
The task is to **sort the array `b[]` with respect to `a[]`**.  

---

## Examples

### Example 1
**Input:**  

a[] = [3, 1, 2]
b[] = ['G', 'E', 'K']


**Output:**  

E K G


**Explanation:**  
- `3 → G`, `1 → E`, `2 → K`  
- Sorting by `a[]`: `1 → E`, `2 → K`, `3 → G`  
- Final result: `E K G`.

---

### Example 2
**Input:**  

a[] = [4, 1, 3, 2]
b[] = ['A', 'X', 'B', 'Y']


**Output:**  

X Y B A


**Explanation:**  
- `4 → A`, `1 → X`, `3 → B`, `2 → Y`  
- Sorting by `a[]`: `1 → X`, `2 → Y`, `3 → B`, `4 → A`  
- Final result: `X Y B A`.

---

## Constraints
- `1 <= N <= 1000`  
- `1 <= Ai <= 1000`  
- `'A' <= Bi <= 'Z'`  
- Values of `Ai` are distinct.  

---
