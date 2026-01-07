# Find the Leftmost Magical Number

## Problem Statement
You are given a **sorted array of distinct integers** `arr`.

A number `arr[i]` is called a **Magical Number** if:

arr[i] = i (0-based indexing)


Your task is to **find and return the leftmost magical number** present in the array.

- If no magical number exists, return `-1`.

---

## Examples

### Example 1
**Input:**

arr = [-2, -1, 2, 4, 6]


**Output:**

2


**Explanation:**  
Only one magical number exists:
- `arr[2] = 2`

---

### Example 2
**Input:**

arr = [-1, 1, 2, 3, 5, 7]


**Output:**

1


**Explanation:**  
Magical numbers are:
- `arr[1] = 1`
- `arr[2] = 2`
- `arr[3] = 3`  

The **leftmost** magical number is `1`.

---

### Example 3
**Input:**

arr = [-12, 0, 1, 2, 3, 4]


**Output:**

-1


**Explanation:**  
No index satisfies `arr[i] = i`.

---

## Constraints

- 1 ≤ arr.size() ≤ 10^6
- -10^9 ≤ arr[i] ≤ 10^9


---
