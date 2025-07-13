# Calculate Median of an Array

## Problem Statement

Given an array `arr[]` of integers, calculate and return the **median** of the array.

- If the array contains an **odd** number of elements, the median is the **middle** element after sorting.
- If the array contains an **even** number of elements, the median is the **average of the two middle** elements after sorting.

---

## Examples

### Example 1
**Input:**  
`arr[] = [90, 100, 78, 89, 67]`  
**Output:**  
`89`  
**Explanation:**  
Sorted array: `[67, 78, 89, 90, 100]`.  
Middle element: `89`.

---

### Example 2  
**Input:**  
`arr[] = [56, 67, 30, 79]`  
**Output:**  
`61.5`  
**Explanation:**  
Sorted array: `[30, 56, 67, 79]`.  
Average of middle elements: `(56 + 67)/2 = 61.5`.

---

### Example 3  
**Input:**  
`arr[] = [1, 2]`  
**Output:**  
`1.5`  
**Explanation:**  
Sorted array: `[1, 2]`.  
Average: `(1 + 2)/2 = 1.5`.

---

## Constraints

- `1 ≤ arr.size() ≤ 10^5`
- `1 ≤ arr[i] ≤ 10^5`

---
