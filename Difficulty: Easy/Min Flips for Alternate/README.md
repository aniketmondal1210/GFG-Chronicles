# Minimum Bit Flips to Make Binary String Alternating

## Problem Description

Given a binary string `s`, you can flip any bit (change `'0'` to `'1'` or `'1'` to `'0'`) to make the string alternating. A string is called alternating if no two adjacent characters are the same.

Find the minimum number of bit flips required to make `s` alternating.

---

## Examples

### Example 1
- **Input:** `s = "001"`
- **Output:** `1`
- **Explanation:** Flip the bit at index `0` from `'0'` to `'1'` to obtain `"101"`, which is alternating. Minimum flips required is `1`.

### Example 2
- **Input:** `s = "0001010111"`
- **Output:** `2`
- **Explanation:** Flip the bits at indices `1` and `8` to obtain `"0101010101"`, which is alternating. Minimum flips required is `2`.

---

## Constraints

- $1 \le \text{s.size()} \le 10^5$
- `s` consists only of the characters `'0'` and `'1'`.

---
