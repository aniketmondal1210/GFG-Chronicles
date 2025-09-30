# Pair Elements from Array

## Problem Statement
Given an array `arr` of size `n` containing positive integers.  
The task is to form pairs such that:
- The **1st element** is paired with the **last element**,
- The **2nd element** is paired with the **2nd last element**, and so on.
- If `n` is odd, the middle element is paired with itself.  

The resulting pairs should be stored in an array of pairs `res` of size `m`.

---

## Examples

### Example 1
**Input**

n = 5
arr = [1, 2, 3, 4, 5]

**Output**

(1,5) (2,4) (3,3)

**Explanation**  
- 1 paired with 5  
- 2 paired with 4  
- 3 paired with itself  

---

### Example 2
**Input**

n = 4
arr = [4, 2, 3, 1]

**Output**

(4,1) (2,3)

**Explanation**  
- 4 paired with 1  
- 2 paired with 3  

---

## Constraints
- `1 <= n <= 1000`  
- `1 <= arr[i] <= 1000`  
- `1 <= m <= n`

---
