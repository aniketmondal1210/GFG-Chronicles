# Delete k Elements Smaller Than Next Element

## Problem Statement
You are given an array `arr[]` of integers and a number `k`. The task is to **delete k elements** from the array such that:

- You delete `arr[i]` if `arr[i] < arr[i+1]`.
- Or if after deletions, `arr[i]` becomes smaller than its new next element.  

After deleting exactly `k` elements, return the remaining array.

---

## Examples

### Example 1
**Input:**  

arr = [20, 10, 25, 30, 40], k = 2


**Output:**  

[25, 30, 40]


**Explanation:**  
- Delete `10` because `10 < 25`.  
- After deletion, array = `[20, 25, 30, 40]`.  
- Now delete `20` because `20 < 25`.  
- Final array = `[25, 30, 40]`.

---

### Example 2
**Input:**  

arr = [3, 100, 1], k = 1


**Output:**  

[100, 1]


**Explanation:**  
- Delete `3` because `3 < 100`.  
- Final array = `[100, 1]`.

---

## Constraints
- `2 ≤ arr.size() ≤ 10^6`  
- `1 ≤ k < arr.size()`

---
