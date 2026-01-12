# Find First and Last Occurrence in a Sorted Array

## Problem Statement
You are given a **sorted array** `v[]` of size `N` that may contain **duplicate elements**, and an integer `X`.

Your task is to find the **indices of the first and last occurrence** of `X` in the array.

- If `X` is **not present**, return the pair `{ -1, -1 }`.

---

## Examples

### Example 1
**Input:**

N = 9
v[] = {1, 3, 5, 5, 5, 5, 67, 123, 125}
X = 5


**Output:**

2 5


**Explanation:**
- First occurrence of `5` is at index `2`
- Last occurrence of `5` is at index `5`

---

### Example 2
**Input:**

N = 9
v[] = {1, 3, 5, 5, 5, 5, 7, 123, 125}
X = 7


**Output:**

6 6


**Explanation:**
- Element `7` appears only once at index `6`

---

## Expected Complexity
- **Time Complexity:** `O(log N)`
- **Auxiliary Space:** `O(1)`

> ⚠️ Since the array is sorted, **binary search** should be used to achieve optimal performance.

---

## Constraints

- 1 ≤ N ≤ 10^5
- 1 ≤ v[i], X ≤ 10^18


---
