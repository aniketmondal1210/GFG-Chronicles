# Prefix Average of an Array

## Problem Statement
Given an integer array `arr`, find the **average (mean)** of the prefix array at every index.  
That is, for each index `i`, compute the average of all elements from index `0` to `i`.

---

## Input
- An integer array `arr` of size `n`.

**Constraints:**

1 ≤ arr.size ≤ 10⁵
1 ≤ arr[i] ≤ 10⁶


---

## Output
Return an array where the `i`-th element represents the average of the prefix `arr[0…i]`.

---

## Explanation
For each prefix ending at index `i`:

prefix_sum = arr[0] + arr[1] + ... + arr[i]
average = prefix_sum / (i + 1)


---

## Examples

### Example 1
**Input:**

arr = [10, 20, 30, 40, 50]


**Output:**

[10, 15, 20, 25, 30]


**Explanation:**

10 / 1 = 10
(10 + 20) / 2 = 15
(10 + 20 + 30) / 3 = 20
(10 + 20 + 30 + 40) / 4 = 25
(10 + 20 + 30 + 40 + 50) / 5 = 30


---

### Example 2
**Input:**

arr = [12, 2]


**Output:**

[12, 7]


**Explanation:**

12 / 1 = 12
(12 + 2) / 2 = 7


---
