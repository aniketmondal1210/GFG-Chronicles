# Minimum Product of Any Two Numbers in an Array

## Problem

Given an array `arr[]` of positive integers, find the **minimum product** that can be obtained by multiplying any two distinct elements of the array.

---

## Examples

### Example 1

**Input**

```text
arr = [2, 7, 3, 4]
```

**Output**

```text
6
```

**Explanation**

Possible products are:

```text
2 × 7 = 14
2 × 3 = 6
2 × 4 = 8
7 × 3 = 21
7 × 4 = 28
3 × 4 = 12
```

The minimum product is:

```text
2 × 3 = 6
```

---

### Example 2

**Input**

```text
arr = [198, 76, 544, 123, 154, 675]
```

**Output**

```text
9348
```

**Explanation**

The two smallest numbers are:

```text
76 and 123
```

Their product is:

```text
76 × 123 = 9348
```

---

## Constraints:

- 2 <= arr.size() <=10^6
- 1 <= arr[i] <=10^6

---
