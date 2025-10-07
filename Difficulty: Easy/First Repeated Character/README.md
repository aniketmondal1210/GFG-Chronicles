# Find the First Repeated Character in a String

## Problem Statement
Given a string `s` containing only lowercase English letters, find the **first repeated character** — i.e., the character that appears more than once, and whose **second occurrence** has the smallest index.

If no character repeats, return `-1`.

---

## Examples

### Example 1
**Input:**

s = "geeksforgeeks"

**Output:**

"e"

**Explanation:**  
The character `'e'` repeats, and its second occurrence appears first among all repeated characters.

---

### Example 2
**Input:**

s = "hellogeeks"

**Output:**

"l"

**Explanation:**  
The letter `'l'` repeats first (second occurrence at index 3).

---

### Example 3
**Input:**

s = "abc"

**Output:**

"-1"

**Explanation:**  
No character repeats in the string.

---

## Constraints
- 1 ≤ |s| ≤ 10⁵  
- `s` contains only lowercase English letters (`a`–`z`).

---
