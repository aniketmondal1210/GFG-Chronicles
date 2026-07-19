# Lower Bound in a Sorted Array

## Problem

Given a **sorted** array `arr[]` (0-based indexing) and an integer `target`, find the **lower bound** of the target.

The **lower bound** is defined as the **smallest index** such that:

```text
arr[index] >= target
```

If no such index exists, return the **length of the array**.

---

## Examples

### Example 1

**Input**

```text
arr = [2, 3, 7, 10, 11, 11, 25]
target = 9
```

**Output**

```text
3
```

**Explanation**

```text
arr[3] = 10
```

`10` is the first element greater than or equal to `9`.

---

### Example 2

**Input**

```text
arr = [2, 3, 7, 10, 11, 11, 25]
target = 11
```

**Output**

```text
4
```

**Explanation**

The first occurrence of `11` is at index `4`.

---

### Example 3

**Input**

```text
arr = [2, 3, 7, 10, 11, 11, 25]
target = 100
```

**Output**

```text
7
```

**Explanation**

There is no element greater than or equal to `100`, so return the array length.

---

## Constraints:

- 1 ≤ arr.size() ≤ 10^6
- 1 ≤ arr[i] ≤ 10^6
- 1 ≤ target ≤ 10^6

---
