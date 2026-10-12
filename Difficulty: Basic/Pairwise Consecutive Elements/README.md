# Check if Stack Elements are Pairwise Consecutive

## Problem Description

Given a stack of $n$ integers, determine whether its elements are pairwise consecutive. Starting from the top of the stack, group the elements into consecutive pairs.

- A pair is said to be **pairwise consecutive** if the absolute difference between the two elements is exactly 1 (`abs(a - b) == 1`).
- The two elements in a pair may be in either increasing or decreasing order.
- If the stack contains an odd number of elements, the topmost element is **not included** in any pair and is ignored for validation.
- **Note:** The original contents and order of the stack must remain unchanged after the function returns.

---

## Examples

### Example 1
- **Input:** `stack = [4, 5, -2, -3, 11, 10, 5, 6, 20]` (rightmost element represents the top)
- **Output:** `true`
- **Explanation:** Since the stack contains 9 elements (odd), the top element `20` is ignored. The remaining pairs starting from the top are `(6, 5)`, `(10, 11)`, `(-3, -2)`, and `(5, 4)`. Each pair has an absolute difference of 1.

### Example 2
- **Input:** `stack = [4, 6, 7, 8, 10, 11]`
- **Output:** `false`
- **Explanation:** The pairs formed from the top are `(11, 10)`, `(8, 7)`, and `(6, 4)`. While the first two pairs are consecutive, `(6, 4)` has a difference of 2.

---

## Constraints

- $1 \le 	{st.size()} \le 10^5$
- $-10^9 \le 	{st}[i] \le 10^9$

---
