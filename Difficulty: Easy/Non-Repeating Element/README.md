# First Non-Repeating Element in an Array

## Problem Statement
You are given an array `arr[]` of integers consisting of **positive and negative numbers (excluding zero)**.

Your task is to find the **first non-repeating element** in the array.  
If **no such element exists**, return `0`.

---

## Examples

### Example 1
**Input:**

arr = [-1, 2, -1, 3, 2]


**Output:**

3


**Explanation:**  
- `-1` appears twice  
- `2` appears twice  
- `3` appears only once  

The first element that does not repeat is `3`.

---

### Example 2
**Input:**

arr = [1, 1, 1]


**Output:**

0


**Explanation:**  
All elements are repeating, so there is no non-repeating element.

---

## Complexity Analysis
- **Time Complexity:** `O(n)`
- **Auxiliary Space:** `O(n)`

---

## Constraints

- 1 <= arr.size <= 10^6
- -10^9 <= arr[i] <= 10^9
- arr[i] != 0


---
