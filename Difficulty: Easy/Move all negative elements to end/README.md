# Move Negative Elements to End (In-Place)

## Problem Statement

Given an unsorted array `arr[]` containing both negative and positive integers, the task is to **move all negative elements to the end** of the array **without changing the relative order** of positive and negative elements.

**Note:** Do not return a new array — modify the given array in-place.

---

## Input

An array of integers `arr[]`.

**Constraints:**

```
1 ≤ arr.size() ≤ 10^6
-10^9 ≤ arr[i] ≤ 10^9
```

---

## Output

Modify the array in-place so that all negative numbers are placed at the end while preserving the order of both positive and negative numbers.

---

## Examples

### Example 1

**Input:**

```
arr = [1, -1, 3, 2, -7, -5, 11, 6]
```

**Output:**

```
[1, 3, 2, 11, 6, -1, -7, -5]
```

**Explanation:**
All positives come first in order: [1, 3, 2, 11, 6], followed by negatives: [-1, -7, -5].

---

### Example 2

**Input:**

```
arr = [-5, 7, -3, -4, 9, 10, -1, 11]
```

**Output:**

```
[7, 9, 10, 11, -5, -3, -4, -1]
```

**Explanation:**
Relative order of positives and negatives remains unchanged.

---
