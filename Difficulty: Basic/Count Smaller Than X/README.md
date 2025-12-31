# Count Elements Smaller Than X

## Problem Statement
You are given an **unsorted array `arr[]` of size `N`** containing non-negative integers.  
You are also given an integer `X`.

Your task is to **count how many elements in the array are strictly smaller than `X`**.  
The value `X` **may or may not be present** in the array.

---

## Examples

### Example 1
**Input:**

N = 5
arr[] = {4, 5, 3, 1, 2}
X = 3


**Output:**

2


**Explanation:**  
Elements smaller than `3` are `1` and `2`.

---

### Example 2
**Input:**

N = 6
arr[] = {2, 2, 2, 2, 2, 2}
X = 3


**Output:**

6


**Explanation:**  
All elements are smaller than `3`.

---

## Your Task
This is a **functional problem**.

You need to complete the function:

smallerThanX(arr, N, X)


- **Parameters:**
  - `arr[]` → input array
  - `N` → size of the array
  - `X` → given integer

- **Return:**
  - Count of elements strictly smaller than `X`

⚠️ Input reading and output printing are handled by the driver code.

---

## Expected Complexity
- **Time Complexity:** `O(N)`
- **Auxiliary Space:** `O(1)`

---

## Constraints

- 1 ≤ N ≤ 10^6
- 1 ≤ arr[i], X ≤ 10^5


---
