# Upper Bound in a Sorted Array

## Problem

Given a **sorted** array `arr[]` and an integer `target`, find the **upper bound** of `target`.

The **upper bound** is defined as the **smallest index** such that:

```text
arr[index] > target
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
arr[3] = 10 > 9
```

Index `3` is the first position where the element is greater than `9`.

---

### Example 2

**Input**

```text
arr = [2, 3, 7, 10, 11, 11, 25]
target = 11
```

**Output**

```text
6
```

**Explanation**

The first element greater than `11` is:

```text
arr[6] = 25
```

Hence, the answer is `6`.

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

There is no element greater than `100`, so return the array length.

---

## Constraints:

- 1 ≤ arr.size() ≤ 10^6
- 1 ≤ arr[i] ≤ 10^6
- 1 ≤ target ≤ 10^6

---
