# Find Pair with Given Sum

## Problem

Given:

- An integer array `arr[]`
- An integer `target`

Return the pair of elements whose sum is equal to `target`.

**Note:**

- An element cannot be used twice unless it appears multiple times in the array.
- If no such pair exists, return an empty array.

---

## Examples

### Example 1

**Input**

```text
arr = [2, 9, 10, 4, 15]
target = 12
```

**Output**

```text
[2, 10]
```

**Explanation**

```text
2 + 10 = 12
```

---

### Example 2

**Input**

```text
arr = [3, 2, 4]
target = 8
```

**Output**

```text
[]
```

**Explanation**

```text
No pair has sum equal to 8.
```

---

### Example 3

**Input**

```text
arr = [1, 4, 5, 6, 1]
target = 2
```

**Output**

```text
[1, 1]
```

**Explanation**

```text
There are two occurrences of 1.

1 + 1 = 2
```

---

## Constraints:

- 1 ≤ arr.size() ≤ 10^5
- 0 ≤ arr[i] ≤ 10^4
- 1 ≤ target ≤ 10^4

---
