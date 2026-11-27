# Frequencies of Limited Range Array Elements

## Problem Description

Given an array `arr[]` of size `n` containing positive integers in the range `1` to `n` (where some elements may be repeated or missing), count the frequency of every integer from `1` to `n` and return a 0-indexed list/array `result` of size `n` such that `result[i - 1]` stores the frequency of number `i` (`1 <= i <= n`).

---

## Examples

### Example 1
- **Input:** `arr[] = [2, 3, 2, 3, 5]`
- **Output:** `[0, 2, 2, 0, 1]`
- **Explanation:** Frequencies for `1..5` are `0, 2, 2, 0, 1` respectively.

### Example 2
- **Input:** `arr[] = [3, 3, 3, 3]`
- **Output:** `[0, 0, 4, 0]`
- **Explanation:** `3` appears `4` times, while `1`, `2`, and `4` appear `0` times.

### Example 3
- **Input:** `arr[] = [1]`
- **Output:** `[1]`
- **Explanation:** `1` appears once in an array of size `1`.

---

## Constraints

- $1 \le \text{arr.size()} \le 10^6$
- $1 \le \text{arr}[i] \le \text{arr.size()}$

---
