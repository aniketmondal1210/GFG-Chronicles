# Rearrange Array So That arr[i] = i

## Problem Statement
You are given an array `arr[]` with indices ranging from `0` to `arr.size() - 1`.

Your task is to rearrange the array such that:

arr[i] = i


If an element `i` is not present in the array, place `-1` at index `i`.

### Note:
- The array does **not** contain duplicate non-negative values.
- Values range from `-1` to `arr.size() - 1`.

---

## Example 1

**Input:**

arr = [-1, -1, 6, 1, 9, 3, 2, -1, 4, -1]


**Output:**

[-1, 1, 2, 3, 4, -1, 6, -1, -1, 9]


**Explanation:**
Array size = 10  
Expected arrangement: `[0,1,2,3,4,5,6,7,8,9]`

Missing elements: `0, 5, 7, 8`  
So their positions contain `-1`.

---

## Example 2

**Input:**

arr = [2, 0, 1]


**Output:**

[0, 1, 2]


**Explanation:**
All elements `0, 1, 2` are present.  
So no `-1` is needed.

---

## Constraints

- 0 ≤ arr.size() ≤ 10⁵
- -1 ≤ arr[i] ≤ arr.size() - 1


---
