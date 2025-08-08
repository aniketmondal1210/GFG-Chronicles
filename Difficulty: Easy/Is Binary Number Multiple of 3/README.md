# Check if Binary Number is Divisible by 3

## Problem Statement
You are given a binary number as a string containing only `'0'` and `'1'`.  
Your task is to determine whether the binary number is divisible by **3**.

**Note:**  
- You must try to solve this using **a single traversal** of the input string.
- The input binary number can be large, so you cannot directly convert it to an integer using built-in functions in constant space.

---

## Examples

### Example 1:
**Input:**  
`s = "100"`  

**Output:**  
`false`  

**Explanation:**  
Binary `"100"` equals decimal **4**, which is not divisible by 3.

---

### Example 2:
**Input:**  
`s = "0011"`  

**Output:**  
`true`  

**Explanation:**  
Binary `"0011"` equals decimal **3**, which is divisible by 3.

---

### Example 3:
**Input:**  
`s = "110"`  

**Output:**  
`true`  

**Explanation:**  
Binary `"110"` equals decimal **6**, which is divisible by 3.

---

## Constraints
- `1 ≤ len(s) ≤ 10^6`
- `s` contains only `'0'` and `'1'`.

---
