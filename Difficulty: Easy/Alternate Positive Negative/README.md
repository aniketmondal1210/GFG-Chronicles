# Rearrange Array in Alternating Positive and Negative Order

## Problem Statement
You are given an **unsorted array** `arr` containing **both positive and negative integers**.

Your task is to **rearrange the array** such that:
- The resulting array **starts with a positive integer**  
  (`0` is considered positive).
- Elements are placed in **alternate order**:  
  **positive → negative → positive → negative → ...**
- The **relative order** of positive numbers among themselves and negative numbers among themselves **must be preserved**.
- If either positives or negatives are exhausted, **append the remaining elements as they are**, maintaining order.

---

## Examples

### Example 1
**Input**

arr = [9, 4, -2, -1, 5, 0, -5, -3, 2]


**Output**

[9, -2, 4, -1, 5, -5, 0, -3, 2]


---

### Example 2
**Input**

arr = [-5, -2, 5, 2, 4, 7, 1, 8, 0, -8]


**Output**

[5, -5, 2, -2, 4, -8, 7, 1, 8, 0]


---

### Example 3
**Input**

arr = [9, 5, -2, -1, 5, 0, -5, -3, 2]


**Output**

[9, -2, 5, -1, 5, -5, 0, -3, 2]


---

## Time and Space Complexity

- **Time Complexity:** `O(N)`
- **Auxiliary Space:** `O(N)`

---

## Constraints

- 1 ≤ arr.size() ≤ 10^6
- -10^6 ≤ arr[i] ≤ 10^6


---
