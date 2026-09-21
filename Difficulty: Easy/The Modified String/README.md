# Minimum Insertions to Avoid Three Consecutive Identical Characters

## Problem Description

Given a string `s`, a string is considered **valid** if it does not contain three consecutive identical characters. You may insert characters at any position in the string.

Return the **minimum number of insertions** required to make `s` valid.

---

## Examples

### Example 1
- **Input:** `s = "aabbbcc"`
- **Output:** `1`
- **Explanation:** In `"aabbbcc"`, three `'b'`s occur consecutively. We can insert a different character (e.g., `'d'`) inside the `'b'` sequence to get `"aabbdbcc"`, which is valid.

### Example 2
- **Input:** `s = "aaaaa"`
- **Output:** `2`
- **Explanation:** In `"aaaaa"`, five `'a'`s occur consecutively. Inserting 2 characters turns it into `"aababaa"`, which is valid.

---

## Constraints

- $1 \le 	ext{s.length} \le 10^5$
- `s` consists of characters.

---
