# Find Elements with Even Occurrences

## Problem Statement

Given an integer array `arr[]`, most numbers occur an **odd number of times**, except for a few elements that appear an **even number of times**. Your task is to find and return all elements that occur an even number of times.

If no such element exists, return `-1`.

Elements should be returned in their **order of first occurrence**.

---

## Input

* An integer array `arr[]`.

**Constraints:**

```
1 ≤ arr.size() ≤ 10^6
1 ≤ arr[i] ≤ 10^5
```

---

## Output

Return a list of integers that appear an even number of times, or `[-1]` if none exist.

---

## Examples

### Example 1

**Input:**

```
arr = [9, 12, 23, 10, 12, 12, 15, 23, 14, 12, 15]
```

**Output:**

```
[12, 15, 23]
```

**Explanation:**

```
12 → 4 times
15 → 2 times
23 → 2 times
All others appear an odd number of times.
```

---

### Example 2

**Input:**

```
arr = [23, 12, 56, 34, 32]
```

**Output:**

```
[-1]
```

**Explanation:**

```
Each number appears only once (odd occurrences).
```

---
