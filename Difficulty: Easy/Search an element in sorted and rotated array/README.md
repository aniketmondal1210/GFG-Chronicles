# Search in a Sorted and Rotated Array

## Problem
You are given a **sorted and rotated array** `A` of size `N` containing distinct elements.  
The array has been rotated at some pivot point. You are also given an integer `K`.  

Your task is to return the **index** of `K` in array `A`.  
If the element is not present, return `-1`.  

---

## Constraints
- `1 ≤ N ≤ 10^7`  
- `0 ≤ A[i] ≤ 10^8`  
- `1 ≤ K ≤ 10^8`  
- **Expected Time Complexity:** `O(log N)`  
- **Expected Auxiliary Space:** `O(1)`  

---

## Example 1
**Input**

N = 9
A[] = {5,6,7,8,9,10,1,2,3}
K = 10


**Output**

5


**Explanation**  
`10` is found at index `5`.

---

## Example 2
**Input**

N = 3
A[] = {3,1,2}
K = 1


**Output**

1


**Explanation**  
`1` is found at index `1`.

---
