# First and Last Occurrence of an Element in a Sorted Array

## Problem Statement
You are given:
- A **sorted array** `arr[]`
- An element `x`

Your task is to find the **indices of the first and last occurrence** of `x` in the array.

If `x` does **not exist**, return an array containing only `-1`.

---

## Examples

### Example 1
**Input:**

x = 3
arr = [1, 3, 3, 4]


**Output:**

[1, 2]


**Explanation:**  
The first occurrence of `3` is at index `1` and the last occurrence is at index `2`.

---

### Example 2
**Input:**

x = 5
arr = [1, 2, 3, 4]


**Output:**

[-1]


**Explanation:**  
`5` is not present in the array.

---

## Time & Space Complexity
- **Time Complexity:** `O(log n)`
- **Auxiliary Space:** `O(1)`

---

## Constraints

- 1 ≤ arr.size() ≤ 10^5
- 0 ≤ arr[i], x ≤ 10^9


---
