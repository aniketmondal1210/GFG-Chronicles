# Split String into Letters, Digits, and Special Characters

## Problem Description

Given a string `s` containing letters, digits, and special characters, split `s` into three separate strings `[s1, s2, s3]` such that:
- `s1` contains all the letters (`a-z`, `A-Z`).
- `s2` contains all the digits (`0-9`).
- `s3` contains all the special characters (any character that is neither a letter nor a digit).

**Rules:**
1. The relative order of characters in each string must be preserved exactly as they appear in `s`.
2. If any category of character is completely absent from `s`, return `"-1"` in place of that string.

---

## Examples

### Example 1
- **Input:** `s = "geeks01for02geeks03!!!"`
- **Output:** `["geeksforgeeks", "010203", "!!!"]`
- **Explanation:**
  - Letters: `"geeksforgeeks"`
  - Digits: `"010203"`
  - Special characters: `"!!!"`

### Example 2
- **Input:** `s = "**Docoding123456789everyday##"`
- **Output:** `["Docodingeveryday", "123456789", "**##"]`
- **Explanation:**
  - Letters: `"Docodingeveryday"`
  - Digits: `"123456789"`
  - Special characters: `"**##"`

### Example 3
- **Input:** `s = "ab##c"`
- **Output:** `["abc", "-1", "##"]`
- **Explanation:**
  - Letters: `"abc"`
  - Digits: None $
ightarrow$ `"-1"`
  - Special characters: `"##"`

---

## Constraints

- $1 \le 	{s.size()} \le 10^5$
- `s` can contain English letters, digits, and special characters.

---
