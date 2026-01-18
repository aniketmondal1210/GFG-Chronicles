# Elements Occurring More Than ⌊n/3⌋ Times

## Problem Statement
Given an integer array `nums[]` of size `n`, find **all elements that occur more than ⌊n/3⌋ times** in the array.

- If **no such element exists**, return `[-1]`.
- The solution must run in **O(n)** time and **O(1)** extra space.

---

## Examples

### Example 1
**Input:**

nums = [2, 1, 5, 5, 5, 5, 6, 6, 6, 6, 6]


**Output:**

[5, 6]


**Explanation:**
- `n = 11`, so `n/3 ≈ 3`
- `5` occurs 4 times
- `6` occurs 5 times  
Both occur more than `n/3` times.

---

### Example 2
**Input:**

nums = [1, 2, 3, 4, 5]


**Output:**

[-1]


**Explanation:**
No element appears more than `n/3` times.

---

## Complexity Analysis
- **Time Complexity:** `O(n)`
- **Auxiliary Space:** `O(1)`

---

## Constraints

- 1 ≤ nums.size() ≤ 10^6
- -10^9 ≤ nums[i] ≤ 10^9


---
