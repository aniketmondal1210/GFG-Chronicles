# Missing Characters to Make a Pangram

## Problem

Given a string `s`, find all the missing English alphabet characters required to make it a **pangram**.

A **pangram** is a sentence that contains every letter from **'a'** to **'z'** at least once.

Return:

- A string containing all missing characters in **lowercase** and **lexicographical order**.
- `"-1"` if the string is already a pangram.

---

## Examples

### Example 1

**Input**

```text
s = "Abcdefghijklmnopqrstuvwxy"
```

**Output**

```text
"z"
```

**Explanation**

All letters except `'z'` are present.

---

### Example 2

**Input**

```text
s = "Abc"
```

**Output**

```text
"defghijklmnopqrstuvwxyz"
```

**Explanation**

Only `'a'`, `'b'`, and `'c'` are present. The remaining letters are missing.

---

## Constraints:

- 1 <= |s| <= 10^4

---
