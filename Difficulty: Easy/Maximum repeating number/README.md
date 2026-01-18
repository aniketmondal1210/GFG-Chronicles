# Maximum Repeating Number in an Array

## Problem Statement
You are given an array `arr[]` of size `n`.  
The array contains integers ranging from `0` to `k-1`, where `k` is a positive integer.

Your task is to **find the maximum repeating number** in the array.

- If **multiple elements** have the same maximum frequency, return the **smallest such element**.

---

## Examples

### Example 1
**Input:**

k = 3
arr = [2, 2, 1, 2]


**Output:**

2


**Explanation:**
- Frequency of `2` = 3
- Frequency of `1` = 1  
So, `2` is the most frequent element.

---

### Example 2
**Input:**

k = 3
arr = [2, 2, 1, 0, 0, 1]


**Output:**

0


**Explanation:**
- Frequency of `0` = 2
- Frequency of `1` = 2
- Frequency of `2` = 2  

All have the same frequency, so we return the **smallest element**, which is `0`.

---

## Time & Space Complexity
- **Time Complexity:** `O(n + k)`
- **Auxiliary Space:** `O(k)`

---

## Constraints

- 1 ≤ arr.size() ≤ 10^5
- 1 ≤ k ≤ 10^5
- 0 ≤ arr[i] ≤ k - 1


---
