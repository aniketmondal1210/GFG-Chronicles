# Rearranging Binary Array in Increasing Order

## Problem Statement

You are given a binary array `arr[]`, where each element is either `0` or `1`.  
Your task is to **rearrange the array in increasing order** in-place (without using extra space).  
You do **not** need to return anything; simply **modify the input array**.

---

## Examples

### Example 1  
**Input:**  
`arr = [1, 0, 1, 1, 0]`  
**Output:**  
`[0, 0, 1, 1, 1]`  
**Explanation:**  
After arranging the elements in increasing order, the array becomes `0 0 1 1 1`.

---

### Example 2  
**Input:**  
`arr = [1, 0, 1, 1, 1, 1, 1, 0, 0, 0]`  
**Output:**  
`[0, 0, 0, 0, 1, 1, 1, 1, 1, 1]`  
**Explanation:**  
The elements are rearranged in increasing order (all 0s first, then 1s).

---

### Example 3  
**Input:**  
`arr = [1, 1, 1, 1]`  
**Output:**  
`[1, 1, 1, 1]`  
**Explanation:**  
Since the array already contains only 1s, no change is needed.

---

## Constraints

- `1 ≤ arr.length ≤ 10^6`  
- Each element of `arr` is either `0` or `1`

---

## Expected Time and Space Complexity

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(1)` (in-place operation)
