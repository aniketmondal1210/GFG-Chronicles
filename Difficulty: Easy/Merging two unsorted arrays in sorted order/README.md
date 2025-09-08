# Merge Two Unsorted Arrays and Return a Sorted Array

Given two different arrays `arr1[]` and `arr2[]`, the task is to **merge** the two unsorted arrays and return a **sorted array**.

---

## Examples

### Example 1
**Input:**  

arr1[] = [10, 5, 15]
arr2[] = [20, 3, 2]


**Output:**  

[2, 3, 5, 10, 15, 20]


**Explanation:**  
After merging both arrays → `[10, 5, 15, 20, 3, 2]`  
Sorting gives → `[2, 3, 5, 10, 15, 20]`

---

### Example 2
**Input:**  

arr1[] = [1, 10, 5, 15]
arr2[] = [20, 0, 2]


**Output:**  

[0, 1, 2, 5, 10, 15, 20]


---

## Constraints
- 1 ≤ arr1.size(), arr2.size() ≤ 10⁵  
- -10⁵ ≤ arr1[i], arr2[i] ≤ 10⁵  

---

## Expected Complexity
- **Time Complexity:** O(n log n + m log m + (n + m))  
- **Space Complexity:** O(n + m)  

---
