# Sum of Common Unique Elements in Two Arrays

## Problem
You are given two arrays of size `n1` and `n2`. Your task is to **find all unique elements that are common to both arrays** and return their **sum modulo (10^9 + 7)**.  

- If there are no common elements, return `0`.  
- The arrays may contain **duplicates**, but you only count each common element once.  

---

## Constraints
- `1 <= n1, n2 <= 10^6`
- `1 <= arr1[i], arr2[i] <= 10^9`
- Expected Time Complexity: **O(n1 + n2)**  
- Expected Space Complexity: **O(min(n1, n2))**

---

## Examples

### Example 1
**Input**

n1 = 5, n2 = 6
arr1 = [1, 2, 3, 4, 5]
arr2 = [2, 3, 4, 5, 6, 7]

**Output**

14

**Explanation**  
The common unique elements are `[2, 3, 4, 5]`.  
Sum = `2 + 3 + 4 + 5 = 14`.

---

### Example 2
**Input**

n1 = 5, n2 = 6
arr1 = [1, 2, 2, 3, 5]
arr2 = [3, 3, 2, 2, 6, 5]

**Output**

10

**Explanation**  
The common unique elements are `[2, 3, 5]`.  
Sum = `2 + 3 + 5 = 10`.

---
