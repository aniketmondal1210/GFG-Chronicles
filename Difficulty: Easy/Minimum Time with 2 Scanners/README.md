# Minimum Time to Scan Documents

## Problem Description

Geek has `n` documents that need to be scanned using two scanners. 
- Scanner 1 takes `s_1` units of time to scan one document.
- Scanner 2 takes `s_2` units of time to scan one document.

Both scanners can operate simultaneously, and each scanner can scan only one document at a time. A scanner can start scanning its next document immediately after finishing the current one. Find the minimum time required to scan all `n` documents.

---

## Examples

### Example 1
- **Input:** `n = 2`, `s1 = 2`, `s2 = 4`
- **Output:** `4`
- **Explanation:** Scan both documents using scanner 1 ($2 \times 2 = 4$), or one document on each scanner simultaneously ($\max(2, 4) = 4$). Both approaches require $4$ units of time.

### Example 2
- **Input:** `n = 2`, `s1 = 1`, `s2 = 3`
- **Output:** `2`
- **Explanation:** The optimal approach is to scan both documents using scanner 1, which takes $2 \times 1 = 2$ units of time.

---

## Constraints

- $1 \le n, s_1, s_2 \le 10^6$
- $1 \le s_1 \cdot n, s_2 \cdot n \le 10^9$

---
