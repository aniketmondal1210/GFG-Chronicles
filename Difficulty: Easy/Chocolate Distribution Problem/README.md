# Chocolate Distribution Problem

## Problem Statement
You are given:
- An array `arr[]` of size `n`, where each element represents the number of chocolates in a packet.  
- An integer `k`, representing the number of students.  

The task is to distribute exactly **one packet per student**, such that the **difference between the maximum chocolates and minimum chocolates** among distributed packets is minimized.

---

## Example 1
### Input

arr[] = [3, 4, 1, 9, 56, 7, 9, 12]
k = 5


### Output

6


### Explanation
- If we pick packets `[3, 4, 7, 9, 9]`,  
  - Maximum = 9, Minimum = 3  
  - Difference = 9 - 3 = **6** (minimum possible).

---

## Constraints
- `1 <= k <= n <= 100`  
- `0 <= arr[i] <= 1000`

---
