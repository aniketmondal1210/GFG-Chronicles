# Largest Element That Is the Product of Two Array Elements

## Problem

Given an array `arr[]` of positive integers, find the **largest element** in the array that can be expressed as the product of **two elements** from the same array.

The two elements used to form the product **must be at different indices**.

If no such element exists, return **-1**.

---

## Examples

### Example 1

**Input**

```text
arr = [10, 3, 5, 30, 35]
```

**Output**

```text
30
```

**Explanation**

```text
30 = 10 × 3
```

Both `10` and `3` exist in the array at different indices.

Hence, the answer is:

```text
30
```

---

### Example 2

**Input**

```text
arr = [10, 2, 4, 30, 35]
```

**Output**

```text
-1
```

**Explanation**

No array element can be expressed as the product of two other elements in the array.

---

### Example 3

**Input**

```text
arr = [10, 2, 2, 4, 8, 30, 35]
```

**Output**

```text
8
```

**Explanation**

```text
8 = 4 × 2
```

Both factors are present at different indices.

No larger element satisfies the condition.

---

## Constraints:

- 1 ≤ arr.size() ≤ 10^5
- 1 ≤ arr[i] ≤ 10^9

---
