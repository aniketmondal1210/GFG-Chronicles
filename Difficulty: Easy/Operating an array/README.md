# Array Operations: Search, Insert, Delete

## Problem
You are given an array `arr[]`. Implement the following operations:

1. **searchEle(arr, x):**  
   - Searches for element `x` in `arr`.  
   - Returns `true` if found, else `false`.  

2. **insertEle(arr, y, yi):**  
   - Inserts element `y` at index `yi`.  
   - Returns `true` if insertion is successful, else `false`.  

3. **deleteEle(arr, z):**  
   - Deletes the **first occurrence** of element `z` in `arr`.  
   - Returns `true` if deletion is successful, else `false`.  

---

## Constraints
- `1 <= arr.size() <= 1500`  
- `1 <= x, y, z <= 10^3`  
- `0 <= yi < arr.size()`  
- `0 <= arr[i] <= 10^5`  
- **Time Complexity:** O(n)  
- **Auxiliary Space:** O(1)  

---

## Example

### Input

arr = [2, 4, 1, 0, 2], x = 1, y = 2, yi = 2, z = 0


### Output

true true true


### Explanation
- `searchEle`: `1` exists → return `true`.  
- `insertEle`: Insert `2` at index `2` → `[2, 4, 2, 1, 0, 2]`.  
- `deleteEle`: Delete first `0` → `[2, 4, 2, 1, 2]`.  

---
