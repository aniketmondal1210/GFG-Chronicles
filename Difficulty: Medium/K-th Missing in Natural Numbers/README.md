# Find K-th Smallest Number in Remaining Sequence

## Problem Description

Given an array `arr[]` of distinct positive integers and a positive integer `k`. Consider an infinite sequence of natural numbers starting from `1`. The task is to remove all elements present in `arr[]` from this sequence and find the $k$-th smallest number in the remaining sequence.

---

## Examples

### Example 1
- **Input:** `arr[] = [1, 9, 5, 2]`, `k = 6`
- **Output:** `10`
- **Explanation:** After removing `[1, 2, 5, 9]` from the natural numbers, the remaining sequence is `3, 4, 6, 7, 8, 10, 11, ...`. The 6th number in this sequence is `10`.

### Example 2
- **Input:** `arr[] = [1, 2, 3, 4]`, `k = 1`
- **Output:** `5`
- **Explanation:** After removing `[1, 2, 3, 4]` from the natural numbers, the remaining sequence is `5, 6, 7, ...`. The 1st number in the sequence is `5`.

---

## Constraints

- $1 \le \text{arr.size()} \le 10^5$
- $1 \le \text{arr}[i], k \le 10^6$
- All elements of `arr` are distinct.
- Solution must run in $\mathcal{O}(1)$ auxiliary space.

---
