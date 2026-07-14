# Rearrange Array Alternately (Largest, Smallest, Second Largest, Second Smallest...)

## Problem

Given an array `arr` of **distinct integers**, rearrange it so that:

- The **1st** element is the largest.
- The **2nd** element is the smallest.
- The **3rd** element is the second largest.
- The **4th** element is the second smallest.
- Continue this pattern until all elements are placed.

Return the rearranged array.

---

## Examples

### Example 1

**Input**

```text
arr = [7, 1, 2, 3, 4, 5, 6]
```

**Output**

```text
[7, 1, 6, 2, 5, 3, 4]
```

**Explanation**

Elements are arranged as:

```text
Largest        → 7
Smallest       → 1
2nd Largest    → 6
2nd Smallest   → 2
3rd Largest    → 5
3rd Smallest   → 3
Remaining      → 4
```

---

### Example 2

**Input**

```text
arr = [1, 6, 9, 4, 3, 7, 8, 2]
```

**Output**

```text
[9, 1, 8, 2, 7, 3, 6, 4]
```

**Explanation**

After sorting:

```text
[1,2,3,4,6,7,8,9]
```

Arrange alternately:

```text
9,1,8,2,7,3,6,4
```

---

## Constraints:

1 ≤ arr.size() ≤ 10^5
1 ≤ arr[i] ≤ 10^5

---
