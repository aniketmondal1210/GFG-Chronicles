# Largest Even Number

## Problem Description

Given a string `s` representing an integer, rearrange its digits to form the largest possible number such that the resulting number is even. A number is even if its last digit is divisible by 2.

If it is not possible to form any even number using the digits of `s`, return the largest possible number formed by rearranging all digits of `s` (which will be an odd number).

---

## Examples

### Example 1
- **Input:** `s = "1324"`
- **Output:** `"4312"`
- **Explanation:** The largest possible even number formed by rearranging the digits is `4312`.

### Example 2
- **Input:** `s = "3555"`
- **Output:** `"5553"`
- **Explanation:** No even number is possible since all digits are odd. Thus, the largest possible odd number `5553` is returned.

---

## Constraints

- $1 \le s.\text{size()} \le 10^5$

---
