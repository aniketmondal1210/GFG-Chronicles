# Balanced Array Adjustment

## Problem Statement
Given an array `arr` of even size, the task is to find the **minimum value** that can be added to an element so that the array becomes **balanced**.  
An array is balanced if the **sum of the left half** of the array elements is equal to the **sum of the right half**.

---

## Examples

### Example 1:
**Input:**  

arr = [1, 5, 3, 2]

**Output:**  

1

**Explanation:**  
- Left half sum = 1 + 5 = 6  
- Right half sum = 3 + 2 = 5  
To balance, we need to add **1** to the right half.  

---

### Example 2:
**Input:**  

arr = [1, 2, 1, 2, 1, 3]

**Output:**  

2

**Explanation:**  
- Left half sum = 1 + 2 + 1 = 4  
- Right half sum = 2 + 1 + 3 = 6  
To balance, we need to add **2** to the left half.  

---

## Constraints
- `2 <= arr.size() <= 10^7` (where `arr.size()` is even)  
- `1 <= arr[i] <= 10^5`  

---

## Expected Complexity
- **Time Complexity:** `O(n)`  
- **Auxiliary Space:** `O(1)`  

---
