# Sort Array While Keeping One Element Fixed

## Problem

Given an array `arr[]` and an integer `k`, sort the array in **ascending order** while keeping the element at index `k` fixed at its original position.

Return the resulting array.

---

## Examples

### Example 1

**Input**

```text
arr = [10, 4, 11, 7, 6, 20]
k = 2
```

**Output**

```text
[4, 6, 11, 7, 10, 20]
```

**Explanation**

The element `11` at index `2` remains fixed.

The remaining elements `[10, 4, 7, 6, 20]` are sorted to:

```text
[4, 6, 7, 10, 20]
```

Placing them back while keeping index `2` unchanged gives:

```text
[4, 6, 11, 7, 10, 20]
```

---

### Example 2

**Input**

```text
arr = [30, 20, 10]
k = 0
```

**Output**

```text
[30, 10, 20]
```

**Explanation**

The element `30` remains at index `0`.

The remaining elements `[20, 10]` are sorted to:

```text
[10, 20]
```

Result:

```text
[30, 10, 20]
```

---

## Constraints:

- 1 ≤ arr.size() ≤ 10^5
- 1 ≤ arr[i] ≤ 10^5

---
