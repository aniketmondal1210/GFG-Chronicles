# Count Elements Appearing More Than n/k Times

## Problem
Given an array `arr` of size `n` and an integer `k`, find how many distinct elements in `arr` appear **more than n/k times**.

---

## Constraints
- `1 ≤ arr.size() ≤ 10^6`
- `0 ≤ arr[i] ≤ 10^8`
- `1 ≤ k ≤ arr.size()`

---

## Examples

### Example 1
**Input**

arr = [3, 1, 2, 2, 1, 2, 3, 3], k = 4

**Output**

2

**Explanation**  
`n = 8` → `n/k = 2`.  
Elements:
- `3` appears 3 times
- `2` appears 3 times  
Both `3` and `2` appear more than `2` times.  
Answer = **2**.

---

### Example 2
**Input**

arr = [2, 3, 3, 2], k = 3

**Output**

2

**Explanation**  
`n = 4` → `n/k = 1.33`.  
- `2` appears 2 times
- `3` appears 2 times  
Both > 1.33 → Answer = **2**.

---

### Example 3
**Input**

arr = [1, 4, 7, 7], k = 2

**Output**

0

**Explanation**  
`n = 4` → `n/k = 2`.  
No element occurs more than 2 times.  
Answer = **0**.

---
