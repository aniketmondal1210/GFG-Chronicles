# Count Unique Sums of Digits in an Array

## Problem Statement
You are given an array of integers `arr[]`.

For each element in the array, compute the **sum of its digits**.  
Your task is to find the **total number of unique digit sums** obtained from all elements of the array.

---

## Examples

### Example 1
**Input:**

arr = [123, 42, 45, 78, 12345]


**Output:**

3


**Explanation:**
- Sum of digits:
  - 123 → 1 + 2 + 3 = 6
  - 42 → 4 + 2 = 6
  - 45 → 4 + 5 = 9
  - 78 → 7 + 8 = 15
  - 12345 → 1 + 2 + 3 + 4 + 5 = 15  
- Unique sums = `{6, 9, 15}`
- Total unique sums = `3`

---

### Example 2
**Input:**

arr = [1, 2, 1]


**Output:**

2


**Explanation:**
- Sum of digits:
  - 1 → 1
  - 2 → 2
  - 1 → 1  
- Unique sums = `{1, 2}`
- Total unique sums = `2`

---

## Complexity Analysis
- **Time Complexity:** `O(n × log10(arr[i]))`
- **Auxiliary Space:** `O(1)` (ignoring the set used for unique sums)

---

## Constraints

- 1 ≤ arr.size() ≤ 10^5
- 1 ≤ arr[i] ≤ 10^6

---
