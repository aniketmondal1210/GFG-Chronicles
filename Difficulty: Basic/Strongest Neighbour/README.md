# Maximum of Adjacent Pairs

## Problem Statement
You are given an array `arr[]` consisting of positive integers.  

Your task is to return a new array containing the **maximum of every adjacent pair** in the given array.

For each index `i`, compute:

max(arr[i], arr[i+1])


---

## Example 1

**Input:**

arr = [1, 2, 2, 3, 4, 5]


**Output:**

[2, 2, 3, 4, 5]


**Explanation:**
- max(1, 2) = 2  
- max(2, 2) = 2  
- max(2, 3) = 3  
- max(3, 4) = 4  
- max(4, 5) = 5  

---

## Example 2

**Input:**

arr = [5, 5]


**Output:**

[5]


**Explanation:**
Only one adjacent pair exists → max(5, 5) = 5

---

## Constraints

- 2 ≤ arr.size ≤ 10⁵
- 1 ≤ arr[i] ≤ 10⁶


---

## Time and Space Complexity
- **Time Complexity:** `O(n)`
- **Auxiliary Space:** `O(n)`

---
