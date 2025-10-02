# Divide Array into Two Subarrays and Multiply Their Sums

## Problem Statement
You are given an array of integers. Divide it into two subarrays:
- **Left half**: contains half of the elements.
- **Right half**: contains the remaining elements.  
  - If the array size is **odd**, the right half will contain **one element more** than the left half.

Find:
1. The **sum of elements** in both subarrays.
2. Return the **product** of these two sums.

---

## Examples

### Example 1
**Input**

arr = [1, 2, 3, 4]

**Output**

21

**Explanation**  
- Left half = [1, 2] → sum = 3  
- Right half = [3, 4] → sum = 7  
- Multiply = 3 × 7 = 21  

---

### Example 2
**Input**

arr = [1, 2]

**Output**

2

**Explanation**  
- Left half = [1] → sum = 1  
- Right half = [2] → sum = 2  
- Multiply = 1 × 2 = 2  

---

### Example 3
**Input**

arr = [1, 2, 3, 4, 5]

**Output**

90

**Explanation**  
- Left half = [1, 2] → sum = 3  
- Right half = [3, 4, 5] → sum = 12  
- Multiply = 3 × 12 = 36  

---

## Constraints
- `1 ≤ arr.size() ≤ 1000`
- `1 ≤ arr[i] ≤ 100`
- Expected Time Complexity: **O(n)**
- Expected Auxiliary Space: **O(1)**

---
