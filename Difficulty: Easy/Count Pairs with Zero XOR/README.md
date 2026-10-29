# Count Pairs with Zero XOR

## Problem Description

Given an integer array `arr[]`, find the number of pairs `(i, j)` such that:
- $0 \le i < j < \text{arr.size()}$
- $\text{arr}[i] \text{ XOR } \text{arr}[j] = 0$

Return the total number of such pairs.

---

## Examples

### Example 1
- **Input:** `arr[] = [1, 3, 4, 1, 4]`
- **Output:** `2`
- **Explanation:** The pairs at indexes `(0, 3)` and `(2, 4)` satisfy $\text{arr}[i] \text{ XOR } \text{arr}[j] = 0$.

### Example 2
- **Input:** `arr[] = [2, 2, 2]`
- **Output:** `3`
- **Explanation:** The pairs at indexes `(0, 1)`, `(0, 2)`, and `(1, 2)` satisfy $\text{arr}[i] \text{ XOR } \text{arr}[j] = 0$.

---

## Constraints

- $1 \le \text{arr.size()} \le 6 \times 10^4$
- $1 \le \text{arr}[i] \le 10^5$

---
