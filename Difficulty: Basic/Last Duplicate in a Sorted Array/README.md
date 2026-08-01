# Find the Last Occurrence of Any Duplicate Element

## Problem Statement

You are given a **sorted** array `arr[]` that may contain duplicate elements.

Your task is to find:

- The **index of the last occurrence** of any duplicate element.
- The **value** of that duplicate element.

If multiple duplicate elements exist, return the one whose **last occurrence appears last** in the array.

If no duplicate element exists, return:

```text
[-1, -1]
```

---

## Examples

### Example 1

**Input**

```text
arr[] = [1, 5, 5, 6, 6, 7]
```

**Output**

```text
[4, 6]
```

**Explanation**

Duplicate elements are:

```text
5 → last occurrence at index 2
6 → last occurrence at index 4
```

The last duplicate occurrence is:

```text
Index = 4
Value = 6
```

---

### Example 2

**Input**

```text
arr[] = [1, 2, 3, 4, 5]
```

**Output**

```text
[-1, -1]
```

**Explanation**

There are no duplicate elements.

---

## Constraints:

- 1 ≤ arr.size() ≤ 10^6
- 1 ≤ arr[i] ≤ 10^6

---
