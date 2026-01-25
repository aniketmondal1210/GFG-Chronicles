# Closest Value to K in a Sorted Array

## Problem Statement
You are given a **sorted array** `arr[]` of positive integers (may contain duplicates) and an integer `k`.

Your task is to **find the value in the array closest to `k`**.

### Important Rule
- If **two values are equally close** to `k`, **return the greater value**.

---

## Examples

### Example 1
**Input:**

arr = [1, 3, 6, 7], k = 4

**Output:**

3

**Explanation:**

|1 - 4| = 3
|3 - 4| = 1
|6 - 4| = 2
|7 - 4| = 3

Closest value is `3`.

---

### Example 2
**Input:**

arr = [1, 2, 3, 5, 6, 8, 9], k = 4

**Output:**

5

**Explanation:**  
Both `3` and `5` have the same difference (`1`).  
According to the rule, return the **greater value**, which is `5`.

---

### Example 3
**Input:**

arr = [6, 8, 8, 8, 9, 11, 13, 13, 15, 18, 19], k = 10

**Output:**

11


---

## Constraints

- 1 ≤ arr.size() ≤ 10^6
- 1 ≤ arr[i], k ≤ 10^9


---
