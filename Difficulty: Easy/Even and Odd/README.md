# Rearrange Array with Even and Odd Indices

## Problem Statement

Given an array containing equal numbers of even and odd integers, rearrange the array such that:

- Even numbers are placed at even indices.
- Odd numbers are placed at odd indices.

Use **0-based indexing**.

---

# Example 1

```text
Input:
arr[] = {3, 6, 12, 1, 5, 8}

Output:
6 3 12 1 8 5
```

### Explanation

```text
Index 0 -> 6  (even)
Index 1 -> 3  (odd)
Index 2 -> 12 (even)
Index 3 -> 1  (odd)
Index 4 -> 8  (even)
Index 5 -> 5  (odd)
```

---

# Example 2

```text
Input:
arr[] = {1, 2, 3, 4}

Output:
2 1 4 3
```

---

## Expected Time Complexity: O(N)
## Expected Auxiliary Space: O(1)


## Constraints:

- 1 ≤ N ≤ 10^5
- 1 ≤ arr[i] ≤ 10^5

---
