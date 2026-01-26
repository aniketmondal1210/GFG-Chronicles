# Sum of Elements Between K1th and K2th Smallest Elements

## Problem Statement
Given an array `A[]` of `N` positive integers and two integers `K1` and `K2`  
(1 ≤ K1 < K2 ≤ N), find the **sum of all elements strictly between the K1th and K2th smallest elements** in the array.

---

## Examples

### Example 1
**Input**

N = 7
A = [20, 8, 22, 4, 12, 10, 14]
K1 = 3, K2 = 6


**Output**

26


**Explanation**
- Sorted array → [4, 8, 10, 12, 14, 20, 22]
- 3rd smallest = 10
- 6th smallest = 20
- Elements between them → 12, 14
- Sum = 26

---

### Example 2
**Input**

N = 6
A = [10, 2, 50, 12, 48, 13]
K1 = 2, K2 = 6


**Output**

73

---

## Time & Space Complexity
- **Time Complexity:** O(N log N)
- **Auxiliary Space:** O(N)

---

## Constraints:
- 1 ≤ N ≤ 10^5
- 1 ≤ K1, K2 ≤ 10^5

---
