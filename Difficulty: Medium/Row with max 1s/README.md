# Row With Maximum Number of 1s

## Problem Statement

Given a binary matrix `arr[][]` where each row is sorted in non-decreasing order, find the index of the first row having the maximum number of `1s`.

Return `-1` if no `1` exists in the matrix.

---

# Examples

### Example 1

```text
Input:
arr = [
 [0,1,1,1],
 [0,0,1,1],
 [1,1,1,1],
 [0,0,0,0]
]

Output:
2
```

### Explanation

```text
Row 2 contains 4 ones,
which is the maximum.
```

---

### Example 2

```text
Input:
arr = [
 [0,0],
 [1,1]
]

Output:
1
```

---

### Example 3

```text
Input:
arr = [
 [0,0],
 [0,0]
]

Output:
-1
```

---

## Constraints:

- 1 ≤ arr.size(), arr[i].size() ≤ 10^3
- 0 ≤ arr[i][j] ≤ 1 

---
