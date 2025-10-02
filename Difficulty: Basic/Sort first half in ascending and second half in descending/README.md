# Sort Half Ascending and Half Descending

## Problem Statement
Given an array `arr` of **even size**, sort:
- the **first half** of the array in **ascending order**,  
- the **second half** of the array in **descending order**.

---

## Examples

### Example 1
**Input**

arr = [10, 20, 30, 40]

**Output**

[10, 20, 40, 30]

**Explanation**  
- First half: [10, 20] → ascending order → [10, 20]  
- Second half: [30, 40] → descending order → [40, 30]  

Final array: `[10, 20, 40, 30]`

---

### Example 2
**Input**

arr = [5, 4, 6, 2, 3, 8, 9, 7]

**Output**

[2, 4, 5, 6, 9, 8, 7, 3]

**Explanation**  
- First half: [5, 4, 6, 2] → ascending → [2, 4, 5, 6]  
- Second half: [3, 8, 9, 7] → descending → [9, 8, 7, 3]  

Final array: `[2, 4, 5, 6, 9, 8, 7, 3]`

---

## Constraints
- `1 <= arr.size() <= 10^5`
- `1 <= arr[i] <= 10^6`
- Array size is **even**
- Expected Time Complexity: **O(n log n)**
- Expected Auxiliary Space: **O(1)**

---
