# Find Element Appearing Once When Others Appear Thrice

## Problem Statement
You are given an integer array `arr[]` where every element appears **exactly three times** except for **one element**, which appears only **once**.  
Your task is to find and return the element that appears once.

---

## Examples

### Example 1:
**Input:**  
`arr = [1, 10, 1, 1]`

**Output:**  
`10`

**Explanation:**  
- `10` appears **once**.  
- `1` appears **three times**.

---

### Example 2:
**Input:**  
`arr = [3, 2, 1, 34, 34, 1, 2, 34, 2, 1]`

**Output:**  
`3`

**Explanation:**  
- `3` appears once.  
- All other elements appear three times.

---

## Constraints
- `1 ≤ len(arr) ≤ 10^5`
- `len(arr) % 3 = 1`
- `-10^9 ≤ arr[i] ≤ 10^9`

---
