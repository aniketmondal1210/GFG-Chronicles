## Problem Description

Given a number `n`, find all 1 to `n` bit numbers with no consecutive 1's in their binary representation.

---

## Examples

### Example 1
- **Input:** `n = 3`
- **Output:** `[1, 2, 4, 5]`
- **Explanation:** The binary representations from 1 to 7 are `1`, `10`, `11`, `100`, `101`, `110`, and `111`. Numbers `3 (11)`, `6 (110)`, and `7 (111)` contain consecutive 1's, leaving `[1, 2, 4, 5]`.

### Example 2
- **Input:** `n = 2`
- **Output:** `[1, 2]`
- **Explanation:** The binary representations from 1 to 3 are `1`, `10`, and `11`. Number `3 (11)` contains consecutive 1's, leaving `[1, 2]`.

---

## Constraints

- $1 \le n \le 20$

---
