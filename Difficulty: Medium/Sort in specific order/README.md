# Sort Array by Odd and Even Rules

Given an array `arr[]` of positive integers, sort them so that:  
- The **first part** of the array contains **odd numbers in descending order**.  
- The **rest of the array** contains **even numbers in ascending order**.  

---

## Examples

### Example 1
**Input:**  

arr[] = [1, 2, 3, 5, 4, 7, 10]


**Output:**  

[7, 5, 3, 1, 2, 4, 10]


**Explanation:**  
- Odd numbers → `[1, 3, 5, 7]` → sorted descending → `[7, 5, 3, 1]`  
- Even numbers → `[2, 4, 10]` → sorted ascending → `[2, 4, 10]`  

Final array = `[7, 5, 3, 1, 2, 4, 10]`.

---

### Example 2
**Input:**  

arr[] = [0, 4, 5, 3, 7, 2, 1]


**Output:**  

[7, 5, 3, 1, 0, 2, 4]


**Explanation:**  
- Odd numbers → `[5, 3, 7, 1]` → sorted descending → `[7, 5, 3, 1]`  
- Even numbers → `[0, 4, 2]` → sorted ascending → `[0, 2, 4]`  

Final array = `[7, 5, 3, 1, 0, 2, 4]`.

---

## Constraints
- 1 ≤ arr.size() ≤ 10⁵  
- 0 ≤ arr[i] ≤ 10⁹  

---
