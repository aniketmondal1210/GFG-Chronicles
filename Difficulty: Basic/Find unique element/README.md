# Unique Element Appearing Not in Multiples of K

## Problem Statement

Given an array of elements where **every element occurs in multiples of `k`**, except **one element** which doesn't, return that **unique element**.

---

## Examples

### Example 1
**Input:**  
`k = 3`  
`arr = [6, 2, 5, 2, 2, 6, 6]`  
**Output:**  
`5`  
**Explanation:**  
Every element appears 3 times except `5`.

---

### Example 2
**Input:**  
`k = 4`  
`arr = [2, 2, 2, 10, 2]`  
**Output:**  
`10`  
**Explanation:**  
Every element appears 4 times except `10`.

---

## Constraints

- `3 ≤ arr.size() ≤ 2 * 10^5`
- `2 ≤ k ≤ 2 * 10^5`
- `1 ≤ arr[i] ≤ 10^9`

---

## Expected Time and Space Complexity

- **Time Complexity:** `O(n * log(arr[i]))`
- **Auxiliary Space:** `O(log(arr[i]))`
