# Sum of Elements Except First and Last

## Problem Statement
You are given an array `arr` of numbers.  
Return the **sum of all elements except the first and last elements**.

---

## Examples

### Example 1
**Input:**

arr = [5, 24, 39, 60, 15, 28, 27, 40, 50, 90]

**Output:**

283

**Explanation:**  
Sum of elements excluding the first (`5`) and last (`90`) is  
`24 + 39 + 60 + 15 + 28 + 27 + 40 + 50 = 283`.

---

### Example 2
**Input:**

arr = [5, 10, 1, 11]

**Output:**

11

**Explanation:**  
Sum of middle elements = `10 + 1 = 11`.

---

### Example 3
**Input:**

arr = [5, 10]

**Output:**

0

**Explanation:**  
No middle elements exist between first and last.

---

## Constraints
- `2 <= arr.size() <= 10^5`
- `2 <= arr[i] <= 10^5`

---
