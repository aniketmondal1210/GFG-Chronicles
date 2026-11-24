# Count Pairs With Given Sum in Sorted Array

## Problem Description

Given a sorted array `arr[]` of size `n` and an integer `target`, find the number of pairs `(i, j)` with `0 <= i < j < n` such that `arr[i] + arr[j] == target`.

Pairs must consist of elements at distinct indices.

---

## Examples

### Example 1
- **Input:** `arr[] = [-1, 1, 5, 5, 7]`, `target = 6`
- **Output:** `3`
- **Explanation:** Valid pairs summing to `6` are `arr[1] + arr[2] = 1 + 5`, `arr[1] + arr[3] = 1 + 5`, and `arr[0] + arr[4] = -1 + 7`.

### Example 2
- **Input:** `arr[] = [1, 1, 1, 1]`, `target = 2`
- **Output:** `6`
- **Explanation:** Any two distinct indices from the four `1`s form a pair summing to `2`, giving $\binom{4}{2} = 6$ pairs.

### Example 3
- **Input:** `arr[] = [-1, 10, 10, 12, 15]`, `target = 125`
- **Output:** `0`
- **Explanation:** No two elements sum to `125`.

---

## Constraints

- $2 \le \text{arr.size()} \le 10^5$
- $-10^5 \le \text{arr}[i], \text{target} \le 10^5$

---
