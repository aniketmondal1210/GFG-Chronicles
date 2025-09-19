# Delete Keyword in C++

## Problem Statement
We are given a **dynamic array** `A` of size `N`.  
The task is to find the **sum of array elements**.  

However, you must **comment the line** that deallocates the array (`delete[] A;`).  
This way, the driver code can still access the array after summation to print its first element.  

---

## Example 1

**Input:**  

N = 5
A[] = 1 2 3 4 5


**Output:**  

15
1


**Explanation:**  
- Sum of array elements is `1 + 2 + 3 + 4 + 5 = 15`.  
- First element of the array is `1`.  

---

## Constraints
- `1 <= N <= 100`  
- `1 <= A[i] <= 10^5`  

---
