# Median of Two Sorted Arrays (Equal Size)

Given two **sorted arrays** `a[]` and `b[]` of **equal size**, return the **median** of the merged array formed after combining both arrays in sorted order.

You must compute the median **without actually merging** the arrays (optimal method), but a simple merge-based method also works for explanation.

---

## Examples

### Example 1

Input:
a = [-5, 3, 6, 12, 15]
b = [-12, -10, -6, -3, 4]

Merged Array: [-12, -10, -6, -5, -3, 3, 4, 6, 12, 15]
Median = (-3 + 3) / 2 = 0
Output: 0


### Example 2

Input:
a = [2, 3, 5, 7]
b = [10, 12, 14, 16]

Merged Array: [2, 3, 5, 7, 10, 12, 14, 16]
Median = (7 + 10) / 2 = 8.5
Output: 8.5


### Example 3

Input:
a = [-5]
b = [-6]

Merged Array: [-6, -5]
Median = (-6 + -5) / 2 = -5.5
Output: -5.5


---

### Constraints

- 1 ≤ a.size(), b.size() ≤ 10^6

- -10^6 ≤ a[i], b[i] ≤ 10^6

---
