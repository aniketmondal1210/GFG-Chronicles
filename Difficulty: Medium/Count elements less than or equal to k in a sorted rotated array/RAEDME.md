# Count Elements ≤ x in a Rotated Sorted Array

## Problem Statement
You are given a **sorted array** `arr[]` containing **distinct positive integers** that has been **rotated at some unknown pivot**.  
Also given a value `x`.  

Your task is to **count the number of elements in the array that are less than or equal to `x`**.

---

## Example 1
**Input:**  

arr = [4, 5, 8, 1, 3], x = 6


**Output:**  

4


**Explanation:**  
Elements `1, 3, 4, 5` are ≤ `6`.  
Hence, the count is `4`.

---

## Example 2
**Input:**  

arr = [6, 10, 12, 15, 2, 4, 5], x = 14


**Output:**  

6


**Explanation:**  
All elements except `15` are ≤ `14`.  
So the count is `6`.

---

## Constraints
- `1 ≤ arr.size() ≤ 10^5`  
- `0 ≤ arr[i], x ≤ 10^9`  
- Array contains **distinct integers**.  

---
