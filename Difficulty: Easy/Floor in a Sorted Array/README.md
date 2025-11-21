# Floor of X in a Sorted Array

## Problem Statement
Given a **sorted array** `arr[]` and an integer `x`, find the **index (0-based)** of the **largest element** in `arr[]` that is **less than or equal to** `x`.  
This element is called the **floor** of `x`.

If no such element exists, return **-1**.

**Note:**  
If the floor occurs multiple times, return the **index of its last occurrence**.

---

## Examples

### Example 1
**Input:**  

arr = [1, 2, 8, 10, 10, 12, 19], x = 5

**Output:**  

1

**Explanation:**  
The largest number ≤ 5 is **2**, located at index **1**.

---

### Example 2
**Input:**  

arr = [1, 2, 8, 10, 10, 12, 19], x = 11

**Output:**  

4

**Explanation:**  
The largest number ≤ 11 is **10**.  
Its last occurrence is at index **4**.

---

### Example 3
**Input:**  

arr = [1, 2, 8, 10, 10, 12, 19], x = 0

**Output:**  

-1

**Explanation:**  
No element ≤ 0 exists.

---
