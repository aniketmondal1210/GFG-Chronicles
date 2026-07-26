# Numbers with Adjacent Digits Differing by 1

## Problem

Given:

- An array `arr[]`
- An integer `k`

Find all numbers in the array that satisfy all of the following:

- The number is **less than `k`**.
- The number has **at least two digits**.
- The absolute difference between every pair of adjacent digits is **exactly 1**.

Return the resulting list. If no such number exists, return an empty list.

---

## Examples

### Example 1

**Input**

```text
arr = [7, 98, 56, 43, 45, 23, 12, 8]
k = 54
```

**Output**

```text
[43, 45, 23, 12]
```

**Explanation**

```text
43 → |4-3| = 1 ✓
45 → |4-5| = 1 ✓
23 → |2-3| = 1 ✓
12 → |1-2| = 1 ✓
```

All are less than `54` and have at least two digits.

---

### Example 2

**Input**

```text
arr = [87, 89, 45, 235, 465, 765, 123, 987, 499, 655]
k = 1000
```

**Output**

```text
[87, 89, 45, 765, 123, 987]
```

**Explanation**

```text
87  → |8-7| = 1
89  → |8-9| = 1
45  → |4-5| = 1
765 → |7-6| = 1, |6-5| = 1
123 → |1-2| = 1, |2-3| = 1
987 → |9-8| = 1, |8-7| = 1
```

---

## Constraints:

- 1 ≤ arr.size() ≤ 10^6
- 1 ≤ k, arr[i] ≤ 10^6

---
