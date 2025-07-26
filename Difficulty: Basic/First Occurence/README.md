# Find First Occurrence of Pattern in Text

## Problem Statement

Given two strings `txt` and `pat`, your task is to **find the first occurrence of the string `pat` in the string `txt`**.  
Return the index of the first occurrence (0-based). If the pattern does not occur, return `-1`.

**Note:** You are **not allowed to use any inbuilt string search function** like `find()` or `index()`.

---

## Examples

### Example 1:
**Input:**  
`txt = "GeeksForGeeks"`  
`pat = "Fr"`  
**Output:**  
`-1`  
**Explanation:** `"Fr"` is not present in `"GeeksForGeeks"`.

---

### Example 2:
**Input:**  
`txt = "GeeksForGeeks"`  
`pat = "For"`  
**Output:**  
`5`  
**Explanation:** `"For"` starts at index 5 in `"GeeksForGeeks"`.

---

### Example 3:
**Input:**  
`txt = "GeeksForGeeks"`  
`pat = "gr"`  
**Output:**  
`-1`  
**Explanation:** `"gr"` is not found in `"GeeksForGeeks"`.

---

## Constraints

- `1 ≤ len(txt), len(pat) ≤ 1000`

---
