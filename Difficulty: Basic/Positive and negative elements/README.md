# Rearrange Array with Alternate Positive and Negative Elements

## Problem

Given an array `arr[]` containing an **equal number of positive and negative integers**, rearrange it such that:

- Every **positive** element is followed by a **negative** element.
- The arrangement **always starts with a positive element**.
- The **relative order** of positive and negative elements must be preserved.

Return the rearranged array.

---

## Examples

### Example 1

**Input**

```text
arr = [-1, 2, -3, 4, -5, 6]
```

**Output**

```text
[2, -1, 4, -3, 6, -5]
```

**Explanation**

Positive numbers (in order):

```text
2, 4, 6
```

Negative numbers (in order):

```text
-1, -3, -5
```

Arrange alternately starting with a positive:

```text
[2, -1, 4, -3, 6, -5]
```

---

### Example 2

**Input**

```text
arr = [-3, 2, -4, 1]
```

**Output**

```text
[2, -3, 1, -4]
```

**Explanation**

Positive numbers:

```text
2, 1
```

Negative numbers:

```text
-3, -4
```

Alternate arrangement:

```text
[2, -3, 1, -4]
```

---

## Constraints:

- 2 ≤ arr.size() ≤ 10^5
- -10^6 ≤ arr[i] ≤ 10^6

---
