# Last Remaining Element After Alternately Removing Maximum and Minimum

## Problem Statement

Given an array `arr[]`, repeatedly remove elements as follows until only one element remains:

1. Remove the **maximum** element.
2. Remove the **minimum** element from the remaining array.
3. Remove the **maximum** element again.
4. Continue alternating between removing the **maximum** and **minimum** elements.

Return the **last remaining element**.

---

## Examples

### Example 1

**Input**

```text
arr[] = [7, 8, 3, 4, 2, 9, 5]
```

**Output**

```text
5
```

**Explanation**

Sorted array:

```text
[2, 3, 4, 5, 7, 8, 9]
```

Removals:

```text
Remove 9 (max)
Remove 2 (min)
Remove 8 (max)
Remove 3 (min)
Remove 7 (max)
Remove 4 (min)
```

Remaining element:

```text
5
```

---

### Example 2

**Input**

```text
arr[] = [8, 1, 2, 9, 4, 3, 7, 5]
```

**Output**

```text
4
```

**Explanation**

Sorted array:

```text
[1, 2, 3, 4, 5, 7, 8, 9]
```

Removals:

```text
Remove 9
Remove 1
Remove 8
Remove 2
Remove 7
Remove 3
Remove 5
```

Remaining element:

```text
4
```

---

### Example 3

**Input**

```text
arr[] = [10]
```

**Output**

```text
10
```

---

## Constraints:

- 1 ≤ arr.size() ≤ 10^5
- 1 ≤ arr[i] ≤ 10^6

---
