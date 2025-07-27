# Find Uncommon Characters from Two Strings

## Problem Statement

You are given two strings `s1` and `s2`. Your task is to identify the characters that appear in **either** string but **not in both** (i.e., characters that are unique to one of the strings).

Return the result as a **sorted string** of these uncommon characters.

---

## Examples

### Example 1:
**Input:**  
`s1 = "geeksforgeeks"`  
`s2 = "geeksquiz"`  
**Output:**  
`"fioqruz"`  
**Explanation:**  
The characters `'f', 'i', 'o', 'q', 'r', 'u', 'z'` are present in either `s1` or `s2`, but not both.

---

### Example 2:
**Input:**  
`s1 = "characters"`  
`s2 = "alphabets"`  
**Output:**  
`"bclpr"`  
**Explanation:**  
Characters `'b', 'c', 'l', 'p', 'r'` are unique to either `s1` or `s2`.

---

### Example 3:
**Input:**  
`s1 = "rome"`  
`s2 = "more"`  
**Output:**  
`""`  
**Explanation:**  
All characters are common between the strings.

---

## Constraints

- `1 <= s1.length, s2.length <= 10^5`
- Both strings contain only lowercase English letters (`a-z`)

---
