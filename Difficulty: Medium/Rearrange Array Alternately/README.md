# Rearrange Array Alternately

## Problem Description

Given a sorted array of non-negative integers, rearrange the array elements alternatively such that:
- The first element is the maximum value.
- The second element is the minimum value.
- The third element is the second maximum value.
- The fourth element is the second minimum value, and so on.

**Note:** Modify the original array itself in-place. You do not have to return anything.

---

## Examples

### Example 1
- **Input:** `arr[] = [1, 2, 3, 4, 5, 6]`
- **Output:** `[6, 1, 5, 2, 4, 3]`
- **Explanation:** Max element = 6, min = 1, second max = 5, second min = 2, and so on.

### Example 2
- **Input:** `arr[] = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110]`
- **Output:** `[110, 10, 100, 20, 90, 30, 80, 40, 70, 50, 60]`

### Example 3
- **Input:** `arr[] = [1]`
- **Output:** `[1]`

---

## Constraints

- $1 \le \text{arr.size()} \le 10^6$
- $0 \le \text{arr}[i] \le 10^6$

---
