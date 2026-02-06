# First User with Exactly K Occurrences

## Problem Statement
You are given an array `arr[]` containing the IDs of users in chronological order of their occurrences.  

Your task is to find the **first user who has exactly `k` occurrences** in the array.  

If no such user exists, return `-1`.

---

## Example 1
**Input:**

arr = [1, 7, 4, 3, 4, 8, 7]
k = 2


**Output:**

7


**Explanation:**
- `7` occurs 2 times  
- `4` occurs 2 times  
Both have exactly 2 occurrences, but `7` appears first in the array.

---

## Example 2
**Input:**

arr = [4, 1, 6, 1, 6, 4]
k = 1


**Output:**

-1


**Explanation:**
No element occurs exactly 1 time.

---

## Expected Time Complexity

O(n)


## Expected Auxiliary Space

O(n)


---

## Constraints

- 1 ≤ arr.size() ≤ 10⁶
- 1 ≤ arr[i] ≤ 10⁶


---
