# Value Equal to Index

## Problem
You are given an array `arr` of size `n`.  
Your task is to find all elements whose value is equal to their **1-based index**.

- Use **1-based indexing** for comparisons.
- If there are multiple such elements, return all of their indices in increasing order.

---

## Examples

### Example 1
**Input:**

arr = [15, 2, 45, 4, 7]

**Output:**

[2, 4]

**Explanation:**
- `arr[2] = 2`
- `arr[4] = 4`  
Both match their index.

---

### Example 2
**Input:**

arr = [1]

**Output:**

[1]

**Explanation:**
- `arr[1] = 1` matches the index.

---

## Constraints
- 1 ≤ `arr.size` ≤ 10^5  
- 1 ≤ `arr[i]` ≤ 10^6

---
