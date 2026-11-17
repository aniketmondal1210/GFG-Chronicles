# Verify String Pattern ($x^n y^n$ Substrings)

## Problem Description

Given a string `s` made of two characters `'x'` and `'y'`, the task is to verify whether `s` is made by concatenating substrings that follow the pattern $x^n y^n$ (where an equal number of `'y'`s follow an equal number of `'x'`s).

---

## Examples

### Example 1
- **Input:** `s = "xxyyxy"`
- **Output:** `true`
- **Explanation:** The string can be split into `"xxyy" + "xy"`. Both substrings contain an equal number of consecutive `'x'` and `'y'` characters.

### Example 2
- **Input:** `s = "xyx"`
- **Output:** `false`
- **Explanation:** The last `'x'` cannot form a valid substring because it is not followed by a matching `'y'`.

---

## Constraints

- $1 \le \text{s.size()} \le 10^5$
- `s` consists only of the characters `'x'` and `'y'`.

---
