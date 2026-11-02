# Check if Floating-Point Number is Even

## Problem Description

Given a floating-point number represented as a string `s`, determine whether it is even or odd:
- Ignore all trailing zeros in the fractional part.
- If the fractional part becomes empty after removing the trailing zeros, determine the parity using the last digit of the integer part.
- Otherwise, determine the parity using the last non-zero digit of the fractional part.

Return `true` if the number is even, otherwise return `false`. It is guaranteed that `s` contains at least one non-zero digit.

---

## Examples

### Example 1
- **Input:** `s = "97.8"`
- **Output:** `true`
- **Explanation:** The last significant digit is `8`, which is even.

### Example 2
- **Input:** `s = "100.70"`
- **Output:** `false`
- **Explanation:** Trailing zeros after the decimal point are ignored. The last significant digit is `7`, which is odd.

### Example 3
- **Input:** `s = "990.00"`
- **Output:** `true`
- **Explanation:** After removing trailing zeros from the fractional part, the number becomes `990`. The last digit of the integer part is `0`, which is even.

---

## Constraints

- $1 \le \vert{}s\vert{} \le 10^5$

---
