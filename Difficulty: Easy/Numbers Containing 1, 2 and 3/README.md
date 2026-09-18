# Numbers Containing Only 1, 2, and 3

## Problem Description

Given an array `arr` of integers, find all numbers in the array whose digits consist **only of `[1, 2, 3]`**.

- The original relative order of elements in the output must match the input array.
- If no element satisfies the condition, return `[-1]`.

---

## Examples

### Example 1
- **Input:** `arr = [14, 31, 7]`
- **Output:** `[31]`
- **Explanation:** Only `31` contains digits restricted entirely to the set `{1, 2, 3}`.

### Example 2
- **Input:** `arr = [1, 2, 13, 4]`
- **Output:** `[1, 2, 13]`
- **Explanation:** `1`, `2`, and `13` consist solely of digits `{1, 2, 3}`.

### Example 3
- **Input:** `arr = [56, 51, 7]`
- **Output:** `[-1]`
- **Explanation:** No number consists solely of digits `{1, 2, 3}`.

---

## Constraints

- $1 \le 	ext{arr.size()} \le 10^5$
- $1 \le 	ext{arr}[i] \le 10^6$

---
