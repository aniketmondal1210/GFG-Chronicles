# Maximum of All Subarrays of Size k

You are given an array `arr[]` and an integer `k`.  
The task is to find the **maximum for each contiguous subarray of size `k`**.

---

## Examples

**Input:**  
`arr[] = [1, 2, 3, 1, 4, 5, 2, 3, 6], k = 3`  
**Output:**  
`3 3 4 5 5 5 6`  

**Explanation:**  
- First window `[1,2,3]` → max = 3  
- Second window `[2,3,1]` → max = 3  
- Third window `[3,1,4]` → max = 4  
- … continuing gives result `3 3 4 5 5 5 6`.

---

**Input:**  
`arr[] = [8, 5, 10, 7, 9, 4, 15, 12, 90, 13], k = 4`  
**Output:**  
`10 10 10 15 15 90 90`  

**Explanation:**  
- First window `[8,5,10,7]` → max = 10  
- Second window `[5,10,7,9]` → max = 10  
- Third window `[10,7,9,4]` → max = 10  
- … continuing gives result `10 10 10 15 15 90 90`.

---

## Constraints
- `1 ≤ arr.size() ≤ 10^7`  
- `1 ≤ k ≤ arr.size()`  
- `0 ≤ arr[i] ≤ 10^7`  

---
