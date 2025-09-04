# Sum of Middle Elements of Two Sorted Arrays

## Problem Statement
You are given **two sorted integer arrays** `arr1` and `arr2` of the same size.  
Your task is to find the **sum of the middle elements** of the combined sorted array obtained after merging both arrays.

---

## Example 1
**Input:**

arr1 = [1, 2, 4, 6, 10]
arr2 = [4, 5, 6, 9, 12]


**Output:**

11


**Explanation:**  
Merged array = `[1, 2, 4, 4, 5, 6, 6, 9, 10, 12]`  
Middle elements = `5` and `6`  
Sum = `5 + 6 = 11`

---

## Example 2
**Input:**

arr1 = [1, 12, 15, 26, 38]
arr2 = [2, 13, 17, 30, 45]


**Output:**

32


**Explanation:**  
Merged array = `[1, 2, 12, 13, 15, 17, 26, 30, 38, 45]`  
Middle elements = `15` and `17`  
Sum = `32`

---

## Constraints
- `1 <= arr1.size() == arr2.size() <= 10^3`
- `1 <= arr1[i], arr2[i] <= 10^6`

---

## Expected Complexity
- **Time Complexity:** `O(log n)`  
- **Space Complexity:** `O(1)`

---
