# Repeating Element in a Sorted Array of Consecutive Integers

## Problem Description

Given a sorted array `arr[]` of positive integers where distinct elements are strictly consecutive (differing by exactly $1$), exactly **one element** is repeated one or more times while all other elements appear exactly once.

Find and return the **repeated element** and its **frequency (count of occurrences)**. If no element is repeated, return `[-1, -1]`.

---

## Examples

### Example 1
- **Input:** `arr[] = [1, 2, 3, 3, 4]`
- **Output:** `[3, 2]`
- **Explanation:** The number `3` appears twice.

### Example 2
- **Input:** `arr[] = [2, 3, 4, 5, 5]`
- **Output:** `[5, 2]`
- **Explanation:** The number `5` appears twice.

### Example 3
- **Input:** `arr[] = [1, 2, 3]`
- **Output:** `[-1, -1]`
- **Explanation:** All elements are unique.

---

## Constraints

- $1 \le {arr.size()} \le 10^7$
- $1 \le {arr}[i] \le \text{arr.size()}$

---
