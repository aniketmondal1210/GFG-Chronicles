# Repeat Digits with Separator

## Problem Statement

Given three inputs stored in variables `a`, `b`, and `c`, where `a` and `b` are integers and `c` is a string (typically a single character), print the digit `a` repeated `a` times, followed by the digit `b` repeated `b` times, with the separator `c` between them. The output should be in a single line.

---

## Examples

### Example 1

**Input:**  
`a = 6`, `b = 4`, `c = '&'`  
**Output:**  
666666&4444

**Explanation:**  
The digit `6` is printed 6 times, the digit `4` is printed 4 times, and they are separated by `'&'`.

---

## Constraints

- `0 <= a, b <= 9`
- `1 <= a, b <= 1000`
- `1 <= len(c) <= 10`
