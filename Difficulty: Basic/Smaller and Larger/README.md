# Count Elements ≤ target and ≥ target in a Sorted Array

## Problem Statement
You are given a **sorted array** `arr` and an integer `target`.

Return an array of size **2** where:

1. **First value** = number of elements **≤ target**
2. **Second value** = number of elements **≥ target**

---

## Examples

### Example 1
**Input:**  

arr = [1, 2, 8, 10, 11, 12, 19], target = 0


**Output:**  

0, 7


**Explanation:**  
- Elements ≤ 0 → **0**  
- Elements ≥ 0 → **7**

---

### Example 2
**Input:**  

arr = [1, 5, 8, 12, 12, 12, 19], target = 12


**Output:**  

6, 4


**Explanation:**  
There are:
- 6 elements ≤ 12  
- 4 elements ≥ 12  

---

## Constraints

1 ≤ arr.size ≤ 100000
0 ≤ arr[i], target ≤ 1000000

---
