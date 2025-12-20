# Difference Between Highest and Lowest Frequency

## Problem Statement
You are given an integer array `arr`.  
Your task is to find the **difference between the highest occurrence and the lowest occurrence** of any number in the array.

**Note:**  
If the array contains **only one distinct element**, return `0`.

---

## Examples

### Example 1
**Input:**  

arr = [1, 2, 2]

**Output:**  

1

**Explanation:**  
- Lowest occurring element: `1` → occurs `1` time  
- Highest occurring element: `2` → occurs `2` times  
- Difference = `2 - 1 = 1`

---

### Example 2
**Input:**  

arr = [7, 8, 4, 5, 4, 1, 1, 7, 7, 2, 5]

**Output:**  

2

**Explanation:**  
- Lowest occurring element: `2` → occurs `1` time  
- Highest occurring element: `7` → occurs `3` times  
- Difference = `3 - 1 = 2`

---

### Constraints

- 1 ≤ arr.size() ≤ 10⁶
- 1 ≤ arr[i] ≤ 10⁶

---
