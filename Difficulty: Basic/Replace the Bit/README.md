# Replace the Kth Bit from Left

## Problem Statement
Given two integers `N` and `K`, change the **Kth bit (1-based indexing) from the left** of the **binary representation** of `N` to `'0'` if it is `'1'`.  
If the Kth bit does not exist or is already `'0'`, return `N` unchanged.

---

## Example 1

**Input:**

N = 13, K = 2


**Output:**

9


**Explanation:**

Binary representation of 13 = 1101
The 2nd bit from the left is 1 → change it to 0
New binary = 1001 = 9 (in decimal)


---

## Example 2

**Input:**

N = 13, K = 6


**Output:**

13


**Explanation:**

Binary representation of 13 = 1101
There is no 6th bit from the left → return N unchanged.


---

## Constraints

1 ≤ N ≤ 10^6


**Expected Time Complexity:** O(log N)  
**Expected Auxiliary Space:** O(1)

---
