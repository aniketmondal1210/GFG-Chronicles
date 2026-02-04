# Frequency of Elements in an Array

## Problem Statement
You are given an array `arr[]` of positive integers which may contain duplicate elements.  
Your task is to return the **frequency of each distinct element** in the array.

The output should be a list of pairs where each pair is:

[element, frequency]

The elements should appear in **ascending order**.

---

## Example 1
**Input:**

arr = [1, 2, 2, 3, 3, 5]


**Output:**

[[1, 1], [2, 2], [3, 2], [5, 1]]


**Explanation:**
- Element `1` occurs 1 time
- Element `2` occurs 2 times
- Element `3` occurs 2 times
- Element `5` occurs 1 time

---

## Example 2
**Input:**

arr = [1, 5, 6, 7, 7]


**Output:**

[[1, 1], [5, 1], [6, 1], [7, 2]]


**Explanation:**
- Elements `1`, `5`, and `6` occur 1 time
- Element `7` occurs 2 times

---

## Constraints

1 ≤ arr.size() ≤ 10⁵
1 ≤ arr[i] ≤ 10⁹


---
