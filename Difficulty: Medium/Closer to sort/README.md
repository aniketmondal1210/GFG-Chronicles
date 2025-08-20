# Search in a Closely Sorted Array

## Problem
You are given an array `arr[]` of **distinct positive integers** that is **closely sorted**, and a target element `x`.  
Your task is to find the **index of `x`** in the array.  
If `x` is not present, return `-1`.  

A **closely sorted array** means:
- The array is initially sorted.
- Each element may have been moved to **either of its adjacent positions**.

---

## Input
- `arr[]`: array of distinct positive integers  
- `x`: target element to search  

---

## Output
- Index of `x` if found, else `-1`.  

---

## Constraints
- `1 ≤ arr.size() ≤ 10^6`  
- `1 ≤ arr[i], x ≤ 10^9`  

---

## Examples

### Example 1
**Input**  

arr = [3, 2, 10, 4, 40]
x = 2

**Output**  

1

**Explanation**  
`2` is present at index `1` (0-based indexing).  

---

### Example 2
**Input**  

arr = [2, 1, 4, 3]
x = 5

**Output**  

-1

**Explanation**  
`5` is not in the array, so answer is `-1`.  

---
