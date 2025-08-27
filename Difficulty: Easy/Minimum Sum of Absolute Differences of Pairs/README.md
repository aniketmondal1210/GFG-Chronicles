# Minimum Sum of Absolute Differences of Pairs

## Problem Statement
You are given two arrays `A` and `B` of equal length `N`.  
Your task is to **pair each element of array `A` to an element in array `B`**, such that the **sum of the absolute differences of all the pairs is minimum**.

---

## Examples

### Example 1:
**Input:**  

N = 4
A = {4, 1, 8, 7}
B = {2, 3, 6, 5}

**Output:**  

6

**Explanation:**  
If we pair as:  
- (1,2), (4,3), (7,5), (8,6)  
The sum = `|1-2| + |4-3| + |7-5| + |8-6| = 6`.  
This is the minimum possible.

---

### Example 2:
**Input:**  

N = 3
A = {4, 1, 2}
B = {2, 4, 1}

**Output:**  

0

**Explanation:**  
If we pair as:  
- (4,4), (1,1), (2,2)  
The sum = `|4-4| + |1-1| + |2-2| = 0`.  
This is the minimum possible.

---

## Constraints
- `1 <= N <= 10^5`  
- `0 <= A[i] <= 10^9`  
- `0 <= B[i] <= 10^9`  
- Sum of `N` over all test cases ≤ `10^6`  

---

## Expected Complexity
- **Time Complexity:** `O(N log N)`  
- **Auxiliary Space:** `O(1)`  

---
