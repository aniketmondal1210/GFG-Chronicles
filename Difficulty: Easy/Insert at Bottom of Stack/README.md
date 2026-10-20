# Insert an Element at the Bottom of a Stack

## Problem Description

Given a stack `st` containing $n$ integers and an integer `x`, insert `x` at the bottom of the stack without using any additional data structures.

Note: While displaying the stack, the bottommost element is printed first.

---

## Examples

### Example 1
- **Input:** `st = [4, 3, 2, 1, 8]`, `x = 2` (bottom to top)
- **Output:** `[2, 4, 3, 2, 1, 8]`
- **Explanation:** After insertion of `2` at the bottom, the final stack will be `[2, 4, 3, 2, 1, 8]`.

### Example 2
- **Input:** `st = [5, 3, 1]`, `x = 4`
- **Output:** `[4, 5, 3, 1]`
- **Explanation:** After insertion of `4` at the bottom, the final stack will be `[4, 5, 3, 1]`.

---

## Constraints

- $1 \le n \le 10^5$
- $0 \le x, \text{elements of stack} \le 10^9$

---
