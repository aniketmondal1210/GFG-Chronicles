# Goodies Redistribution Problem

## Problem Description

You are given an integer array `arr[]` of $n$ elements, where `arr[i]` represents the number of goodies currently held by the $(i+1)\text{th}$ student (1-based indexing). 

The goodies can be redistributed among the students without losing or creating any. Determine if it is possible to redistribute them such that the student at 1-based index $i$ receives **exactly** $i$ goodies.

---

## Examples

### Example 1
- **Input:** `arr[] = [7, 4, 1, 1, 2]`
- **Output:** `true`
- **Explanation:** 
  - Total goodies available: $7 + 4 + 1 + 1 + 2 = 15$.
  - Required goodies: $1 + 2 + 3 + 4 + 5 = 15$.
  - Since the available count equals the required count, redistribution is possible.

### Example 2
- **Input:** `arr[] = [1, 1, 1, 1, 1]`
- **Output:** `false`
- **Explanation:** 
  - Total goodies available: $1 + 1 + 1 + 1 + 1 = 5$.
  - Required goodies: $1 + 2 + 3 + 4 + 5 = 15$.
  - Since $5 \neq 15$, redistribution is impossible.

---

## Constraints

- $1 \le \text{arr.size()}, \text{arr}[i] \le 40000$

---
