# Find Peak Element in Array

## Problem Statement

Given an array `arr[]` where no two adjacent elements are equal, find the index of any peak element.

An element is considered a peak if:

```text
arr[i] > arr[i-1]
and
arr[i] > arr[i+1]
```

Boundary elements are compared with negative infinity.

---

# Examples

### Example 1

```text
Input:
arr = [1, 2, 4, 5, 7, 8, 3]

Output:
true
```

### Explanation

```text
arr[5] = 8

7 < 8 > 3
```

So index `5` is a valid peak.

---

### Example 2

```text
Input:
arr = [10, 20, 15, 2, 23, 90, 80]

Output:
true
```

### Explanation

Possible peaks:

```text
20 at index 1
90 at index 5
```

Returning any one is correct.

---

# Constraints

```text
1 ≤ arr.size() ≤ 10^6
```

---
