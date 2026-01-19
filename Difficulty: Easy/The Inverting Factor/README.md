# Smallest Inverting Factor

## Problem Statement
You are given an array `arr[]` of **positive integers**.  
Your task is to find the **smallest possible Inverting Factor** among all **pairs of integers** in the array.

### Inverting Factor
The **Inverting Factor** of two integers is defined as:

| reverse(a) - reverse(b) |


👉 While reversing a number, **trailing zeros are ignored**  
Example:  
`1200 → 21`

---

## Examples

### Example 1
**Input**

arr = [56, 20, 47, 93, 45]


**Output**

9


**Explanation**
- Reverse values:
  - 56 → 65
  - 47 → 74
- Absolute difference = `|65 - 74| = 9`
- This is the minimum among all pairs.

---

### Example 2
**Input**

arr = [48, 23, 100, 71, 56, 89]


**Output**

14


---

## Time and Space Complexity
- **Time Complexity:** `O(n log n)` (due to sorting)
- **Auxiliary Space:** `O(1)` (in-place operations)

---

## Constraints

- 2 ≤ arr.size() ≤ 10^5
- 1 ≤ arr[i] ≤ 10^5


---
