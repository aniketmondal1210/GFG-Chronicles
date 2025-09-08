# Search in Nearly Sorted Array

You are given a **sorted integer array** `arr[]` consisting of distinct elements, where some elements may be moved to **adjacent positions**  
(i.e., `arr[i]` may be present at `arr[i-1]` or `arr[i+1]`).  

You are also given an integer `target`.  
Return the **index (0-based)** of `target` in the array, or `-1` if `target` is not present.

---

## Examples

### Example 1
**Input:**  

arr[] = [10, 3, 40, 20, 50, 80, 70]
target = 40


**Output:**  

2


**Explanation:**  
`40` is found at index `2`.

---

### Example 2
**Input:**  

arr[] = [10, 3, 40, 20, 50, 80, 70]
target = 90


**Output:**  

-1


**Explanation:**  
`90` is not present in the array.

---

### Example 3
**Input:**  

arr[] = [-20]
target = -20


**Output:**  

0


**Explanation:**  
`-20` is the only element present.

---

## Constraints
- 1 ≤ arr.size() ≤ 10⁵  
- -10⁹ ≤ arr[i] ≤ 10⁹  

---
