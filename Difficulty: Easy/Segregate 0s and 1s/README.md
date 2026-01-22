# Segregate 0s and 1s in an Array

## Problem Statement
You are given an array `arr[]` consisting of only `0`s and `1`s in random order.

Your task is to **modify the array in-place** such that:
- All `0`s are moved to the **left side**
- All `1`s are moved to the **right side**

The **relative order does not matter**.

---

## Examples

### Example 1
**Input:**

arr = [0, 0, 1, 1, 0]


**Output:**

[0, 0, 0, 1, 1]


**Explanation:**  
After segregation, all `0`s are on the left and all `1`s are on the right.

---

### Example 2
**Input:**

arr = [1, 1, 1, 1]


**Output:**

[1, 1, 1, 1]


**Explanation:**  
There are no `0`s in the array, so it remains unchanged.

---

## Time & Space Complexity
- **Time Complexity:** `O(n)`
- **Auxiliary Space:** `O(1)` (in-place)

---

## Constraints

- 1 ≤ arr.size() ≤ 10^6
- 0 ≤ arr[i] ≤ 1


---
