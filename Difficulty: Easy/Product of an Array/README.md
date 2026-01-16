# Product of Array Elements Under Modulo

## Problem Statement
You are given an array `arr[]` of **positive integers**.  
Your task is to compute the **product of all elements** in the array under a given modulo:

mod = 1000000007


The modulo operation gives the remainder after division.  
For example:

k mod m = k % m


---

## Examples

### Example 1
**Input:**

arr[] = [1, 2, 3, 4]


**Output:**

24


**Explanation:**  
The product of the array elements is:

1 × 2 × 3 × 4 = 24

Since `24 < 1000000007`, the result remains `24`.

---

### Example 2
**Input:**

arr[] = [100000, 100000, 100000]


**Output:**

993000007


**Explanation:**  
The product is:

100000 × 100000 × 100000 = 1000000000000000

Applying modulo:

1000000000000000 % 1000000007 = 993000007


---

## Constraints

- 1 ≤ arr.size ≤ 10^5
- 1 ≤ arr[i] ≤ 10^5


---

## Expected Complexity
- **Time Complexity:** O(n)
- **Auxiliary Space:** O(1)

---
