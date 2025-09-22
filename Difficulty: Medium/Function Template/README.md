# Find the Largest Element in an Array (int or float)

## Problem Statement
You are given an array `arr[]` of size `n`.  
Your task is to find the **largest element** in the array.  

The input format includes a variable `K` that specifies the **data type** of the array elements:  
- `K = 1` → array elements are of type **int**  
- `K = 2` → array elements are of type **float**

The array may contain duplicate values.

---

## Example 1
**Input:**  

n = 5, K = 1
arr[] = [1, 8, 7, 56, 90]


**Output:**  

90


**Explanation:**  
The largest element of the given array is `90`.

---

## Example 2
**Input:**  

n = 7, K = 2
arr[] = [1.1, 2.2, 0, 3.2, 2.7, 4.6, 5.0]


**Output:**  

5.0


**Explanation:**  
The largest element of the given array is `5.0`.

---

## Constraints
- `1 ≤ n ≤ 1000`
- `K ∈ {1, 2}`
- `-10^6 ≤ arr[i] ≤ 10^6`

---
