# Find Upper Bound and Lower Bound of k

## Problem
You are given a vector `arr[]` containing integers in **increasing order** and an integer `k`.  
Your task is to print the **Upper Bound** and **Lower Bound** of `k`.

- `upper_bound()`: Returns an iterator pointing to the **first element greater than k**.  
- `lower_bound()`: Returns an iterator pointing to the **first element not less than k**.  

---

## Examples

### Example 1
**Input:**  

arr = [2, 3, 6, 8, 9]
k = 6

**Output:**  

8 6

**Explanation:**  
- The first element greater than `6` is `8` → **upper bound = 8**  
- The first element not less than `6` is `6` → **lower bound = 6**  

---

### Example 2
**Input:**  

arr = [4, 6, 8, 8]
k = 8

**Output:**  

8 8

**Explanation:**  
- The first element greater than `8` is the **second `8`** → **upper bound = 8**  
- The first element not less than `8` is `8` → **lower bound = 8**  

---

## Constraints
- `1 ≤ arr.size() ≤ 10^5`  
- `-10^9 ≤ arr[i], k ≤ 10^9`  
- Array is sorted in **non-decreasing order**

---
