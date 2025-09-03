# Remove Two Greatest Elements

## Problem Statement
You are given an array `arr` of distinct elements.  
Your task is to return an array of all elements **except the two greatest elements**, in **sorted order**.

---

## Example 1
**Input:**

arr = [2, 8, 7, 1, 5]


**Output:**

[1, 2, 5]


**Explanation:**  
The two greatest elements are `7` and `8`.  
The remaining elements are `[1, 2, 5]`.

---

## Example 2
**Input:**

arr = [7, -2, 3, 4, 9, -1]


**Output:**

[-2, -1, 3, 4]


**Explanation:**  
The two greatest elements are `7` and `9`.  
The remaining elements are `[-2, -1, 3, 4]`.

---

## Constraints
- `3 ≤ arr.size ≤ 10^5`
- `-10^6 ≤ arr[i] ≤ 10^6`
- Elements are **distinct**.

---

## Expected Complexity
- **Time Complexity:** `O(n log n)` (due to sorting)  
- **Space Complexity:** `O(n)`

---
