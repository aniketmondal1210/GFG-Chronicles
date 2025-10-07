# Friendliness of a Circular Array

## Problem Statement
Numbers have a **measure of friendliness** defined as the **absolute difference** between them.  
Given a **circular array** `arr[]` of integers, calculate the **friendliness** of the array — the sum of absolute differences between each element and its **closest friend** (its immediate circular neighbors).

---

## Examples

### Example 1
**Input:**

arr = [4, 1, 5]

**Output:**

8

**Explanation:**  
Since the array is circular, the pairs are:  
|4 - 1| + |1 - 5| + |5 - 4| = 3 + 4 + 1 = **8**

---

### Example 2
**Input:**

arr = [1, 1, 1]

**Output:**

0

**Explanation:**  
All numbers are identical → no difference → **0**

---

## Constraints
- 2 < arr.size() ≤ 10⁶  
- 1 ≤ arr[i] ≤ 10⁵  
- Expected Time Complexity: **O(n)**  
- Expected Auxiliary Space: **O(1)**  

---
