# Counting Bits

## Problem Statement
Given an integer `n`, return an array `ans` of size `n + 1`, where each element `i` (`0 ≤ i ≤ n`) represents the **count of 1s** in the binary representation of `i`.

---

## Examples

### Example 1
**Input:**

n = 2

**Binary Representations:**

0 → 0 → 0 ones
1 → 1 → 1 one
2 → 10 → 1 one

**Output:**

[0, 1, 1]


---

### Example 2
**Input:**

n = 5

**Binary Representations:**

0 → 000 → 0
1 → 001 → 1
2 → 010 → 1
3 → 011 → 2
4 → 100 → 1
5 → 101 → 2

**Output:**

[0, 1, 1, 2, 1, 2]


---

## Constraints
- 0 ≤ `n` ≤ 10⁵  
---
