# Check if Two Arrays are Equal

## Problem
Given two arrays `a[]` and `b[]` of equal size, determine whether they contain the same elements.  
Two arrays are considered equal if:
- They contain exactly the same set of elements.
- The counts of repeated elements are the same.
- The arrangement of elements does not matter.

---

## Examples

### Example 1
**Input:**

a = [1, 2, 5, 4, 0]
b = [2, 4, 5, 0, 1]

**Output:**

true

**Explanation:**
Both arrays can be rearranged to `[0, 1, 2, 4, 5]`.

---

### Example 2
**Input:**

a = [1, 2, 5]
b = [2, 4, 15]

**Output:**

false

**Explanation:**
The arrays do not contain the same elements.

---

## Constraints
- 1 ≤ `a.size()`, `b.size()` ≤ 10^7  
- 0 ≤ `a[i]`, `b[i]` ≤ 10^9  

---
