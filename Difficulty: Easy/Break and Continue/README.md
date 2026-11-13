# Generate Numbers with Divisibility Rules

## Problem Description

Given an integer `n`, generate and return a list of numbers from `1` to `n` according to the following rules:
- Skip any number divisible by `3`.
- Stop the iteration when a number divisible by `7` is encountered.
- Include all other numbers in the result.

---

## Examples

### Example 1
- **Input:** `n = 15`
- **Output:** `[1, 2, 4, 5]`
- **Explanation:** 
  - `3` is skipped because it is divisible by `3`.
  - `6` is skipped for the same reason.
  - When `7` is encountered, the loop terminates.

### Example 2
- **Input:** `n = 20`
- **Output:** `[1, 2, 4, 5]`
- **Explanation:** 
  - `3` and `6` are skipped.
  - When `7` is encountered, the loop terminates early.

---

## Constraints

- $1 \le n \le 10^5$

---
