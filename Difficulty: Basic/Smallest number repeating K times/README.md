# Smallest Number Repeated Exactly K Times

## Problem Statement
You are given an array `arr` of integers and an integer `k`.  
Your task is to find the **smallest number** in the array that is repeated **exactly `k` times**.

If no such element exists, return `-1`.

---

## Examples

### Example 1
**Input:**

arr = [2, 2, 1, 3, 1]
k = 2


**Output:**

1


**Explanation:**
- `2` appears 2 times  
- `1` appears 2 times  
- `3` appears 1 time  

Both `1` and `2` occur exactly `k = 2` times.  
The smallest among them is `1`.

---

### Example 2
**Input:**

arr = [3, 5, 3, 2]
k = 1


**Output:**

2


**Explanation:**
- `5` appears 1 time  
- `2` appears 1 time  

Both satisfy the condition, and the smallest is `2`.

---

## Complexity Analysis
- **Time Complexity:** `O(n)`
- **Auxiliary Space:** `O(n)`

---

## Constraints

- 1 ≤ arr.size() ≤ 10^6
- 1 ≤ arr[i] ≤ 10^4


---
