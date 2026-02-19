# Find Missing Numbers in a Given Range

## Problem Statement

Given:
- An array `arr[]` of **distinct integers**
- A range `[low, high]`

Return all numbers within the range `[low, high]` that are **not present** in the array.

The result must be in **sorted order**.

---

## 🧪 Example 1

**Input**

arr = [10, 12, 11, 15]
low = 10
high = 15


**Output**

[13, 14]


**Explanation**
Numbers 13 and 14 are missing in the range [10, 15].

---

## 🧪 Example 2

**Input**

arr = [1, 4, 11, 51, 15]
low = 50
high = 55


**Output**

[52, 53, 54, 55]


---

## ⏱️ Complexity Analysis

- **Time Complexity:** `O(n + (high - low + 1))`
- **Space Complexity:** `O(n)`

Where `n = arr.size()`

---

## Constraints

- 1 ≤ arr.size(), low, high ≤ 10^5
- 1 ≤ arr[i] ≤ 10^5

---
