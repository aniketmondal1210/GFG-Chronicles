# Count Equal Character Index Pairs

## Problem Description

Given a string `s` consisting only of lowercase English characters, count the number of pairs of indices `[i, j]` such that `s[i] == s[j]`.

Pairs `[i, j]` and `[j, i]` are counted separately, and pairs where `i == j` are also valid and counted.

---

## Examples

### Example 1
- **Input:** `s = "air"`
- **Output:** `3`
- **Explanation:** All characters are distinct, so the only valid pairs are `[0, 0]`, `[1, 1]`, and `[2, 2]`.

### Example 2
- **Input:** `s = "aa"`
- **Output:** `4`
- **Explanation:** The character `'a'` appears twice, forming `[0, 0]`, `[0, 1]`, `[1, 0]`, and `[1, 1]`.

---

## Constraints

- $1 \le \text{s.size()} \le 10^5$
- `s` contains only lowercase English characters (`'a'`–`'z'`).

---
