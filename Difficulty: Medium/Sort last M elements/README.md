# Sort Last m Elements in an Array

## Problem Statement
You are given an array `nums` of length `n + m` where the **first `n` elements are already sorted**.  
Your task is to **sort the last `m` elements in-place** such that the entire array becomes sorted.

---

## Example 1
**Input:**

nums = [1, 3, 6, 19, 11, 16]
n = 3
m = 3


**Output:**

[1, 3, 6, 11, 16, 19]


**Explanation:**  
- First 3 elements `[1, 3, 6]` are already sorted.  
- Last 3 elements `[19, 11, 16]` are sorted → `[11, 16, 19]`.  
- After merging → `[1, 3, 6, 11, 16, 19]`.

---

## Example 2
**Input:**

nums = [7, 8, 11]
n = 2
m = 1


**Output:**

[7, 8, 11]


**Explanation:**  
The last element is already in order, so no change is required.

---

## Constraints
- `1 ≤ n, m ≤ 10^5`
- `1 ≤ nums[i] ≤ 10^6`

---

## Expected Complexity
- **Time Complexity:** `O(m * log m)`
- **Auxiliary Space:** `O(m)`

---
