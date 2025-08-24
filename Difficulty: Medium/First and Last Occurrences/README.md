# First and Last Occurrence of an Element in a Sorted Array

## Problem
Given a **sorted array** `arr[]` (with possible duplicates), find the **first** and **last occurrences** of an element `x` in the array.

- If `x` is not present, return `[-1, -1]`.

---

## Constraints
- `1 ≤ arr.size() ≤ 10^6`
- `1 ≤ arr[i], x ≤ 10^9`

---

## Examples

### Example 1
**Input**

arr = [1, 3, 5, 5, 5, 5, 67, 123, 125], x = 5

**Output**

[2, 5]

**Explanation:**  
First occurrence of 5 is at index `2` and last occurrence is at index `5`.

---

### Example 2
**Input**

arr = [1, 3, 5, 5, 5, 5, 7, 123, 125], x = 7

**Output**

[6, 6]

**Explanation:**  
First and last occurrence of `7` is at index `6`.

---

### Example 3
**Input**

arr = [1, 2, 3], x = 4

**Output**

[-1, -1]

**Explanation:**  
Since `4` is not in the array, return `[-1, -1]`.

---
