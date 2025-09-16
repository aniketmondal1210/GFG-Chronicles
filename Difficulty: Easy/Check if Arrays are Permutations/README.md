# Check if Two Arrays are Permutations using STL

## Problem
Given two arrays `arr1` and `arr2` of equal size.  
The task is to check whether the second array is a **permutation** of the first using the STL function `is_permutation()`.

---

### Examples

**Input:**

arr1[] = [1, 2, 3, 4, 5]
arr2[] = [5, 4, 3, 2, 1]

**Output:**

true

**Explanation:** Both arrays contain the same elements, only the order differs.

---

**Input:**

arr1[] = [7, 5, 2, 3]
arr2[] = [7, 2, 3]

**Output:**

false

**Explanation:** `arr2` is missing the element `5`.

---

### Constraints
- `1 ≤ arr1.size(), arr2.size() ≤ 1000`

---
