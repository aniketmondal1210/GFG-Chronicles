# Unique Usernames with Suffix

## Problem Statement
You are given a string array `arr[]` denoting usernames.  
Whenever you encounter a new string, you don't need to modify that string.  
If you encounter a string that already exists, then you append a number as a suffix to it (starting from 1).  

- If you encounter a string, say `"ab"`, then you don't have to modify it.  
- Again if you encounter `"ab"`, you will modify it to `"ab1"` and so on.  
- You need to return the modified string array.

---

## Example
**Input:**  

arr[] = ["aba", "ab", "aba", "aba", "ab"]


**Output:**  

["aba", "ab", "aba1", "aba2", "ab1"]


**Explanation:**  
- `"aba"` → first occurrence, keep `"aba"`.  
- `"ab"` → first occurrence, keep `"ab"`.  
- `"aba"` → already exists, rename to `"aba1"`.  
- `"aba"` → already exists, rename to `"aba2"`.  
- `"ab"` → already exists, rename to `"ab1"`.  

---

## Constraints
- `1 <= arr.size() <= 10^3`

---
