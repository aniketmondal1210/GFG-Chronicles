# Segregate Even and Odd Numbers in Sorted Order

## Problem Statement

Given an array `arr`, write a program that segregates even and odd numbers.  
The program should:
- Put all **even numbers** first in **sorted order**
- Followed by all **odd numbers** in **sorted order**

📝 Note: Modify the array **in-place**. No return is required.

---

## Examples

### Example 1
**Input:**  
`arr = [12, 34, 45, 9, 8, 90, 3]`  
**Output:**  
`[8, 12, 34, 90, 3, 9, 45]`  
**Explanation:**  
Even: 8, 12, 34, 90 → Sorted  
Odd: 3, 9, 45 → Sorted

---

### Example 2  
**Input:**  
`arr = [0, 1, 2, 3, 4]`  
**Output:**  
`[0, 2, 4, 1, 3]`  
**Explanation:**  
Even: 0, 2, 4 → Sorted  
Odd: 1, 3 → Sorted

---

### Example 3  
**Input:**  
`arr = [10, 22, 4, 6]`  
**Output:**  
`[4, 6, 10, 22]`  
**Explanation:**  
All elements are even, sorted accordingly.

---

## Constraints

- `1 ≤ arr.size() ≤ 10^6`
- `0 ≤ arr[i] ≤ 10^5`

---
