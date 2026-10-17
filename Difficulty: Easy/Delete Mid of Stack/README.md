# Delete middle element of a stack

## Problem Description

Given a stack `s`, delete the middle element of the stack without using any additional data structure. 

The middle element is defined as the $\lfloor(	ext{size of stack} + 1) / 2
floor$-th element from the bottom of the stack (using 1-based indexing).

---

## Examples

### Example 1
- **Input:** `s = [10, 20, 30, 40, 50]` (bottom to top)
- **Output:** `[10, 20, 40, 50]` (output shown from top to bottom: `[50, 40, 20, 10]`)
- **Explanation:** The middle element is 30 (index 3 from the bottom). Deleting 30 results in the stack `[10, 20, 40, 50]`.

### Example 2
- **Input:** `s = [10, 20, 30, 40]` (bottom to top)
- **Output:** `[10, 30, 40]` (output shown from top to bottom: `[40, 30, 10]`)
- **Explanation:** The middle element is 20 (index 2 from the bottom). Deleting 20 results in the stack `[10, 30, 40]`.

---

## Constraints

- $2 \le 	{s.size()} \le 10^4$
- $-10^6 \le 	{s}[i] \le 10^6$

---
