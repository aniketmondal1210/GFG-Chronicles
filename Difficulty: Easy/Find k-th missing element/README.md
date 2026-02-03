# K-th Missing Element in an Increasing Sequence

## Problem Statement
You are given two arrays:
- `arr1[]`: an **increasing sequence**
- `arr2[]`: a **normal (unsorted) sequence**

Your task is to find the **k-th element in `arr1` that is NOT present in `arr2`**.

If the k-th missing element does not exist, return `-1`.

---

## Example 1
**Input:**

arr1 = [0, 2, 4, 6, 8, 10, 12, 14, 15]
arr2 = [4, 10, 6, 8, 12]
k = 3


**Output:**

14


**Explanation:**

Elements in arr1 not present in arr2: [0, 2, 14, 15]
3rd missing element = 14


---

## Example 2
**Input:**

arr1 = [1, 2, 3, 4, 5]
arr2 = [5, 4, 3, 1, 2]
k = 3


**Output:**

-1


**Explanation:**
All elements of `arr1` are present in `arr2`, so no missing element exists.

---

## Expected Time Complexity

O(n + m)


## Expected Auxiliary Space

O(m)


---

## Constraints

- 1 ≤ arr1.size(), arr2.size(), k ≤ 10⁵
- 1 ≤ arr1[i] ≤ 10⁵
- 1 ≤ arr2[i] ≤ 10⁵


---
