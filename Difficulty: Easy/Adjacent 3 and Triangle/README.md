# Consecutive Triplet Triangle Check

## Problem Statement

Given an integer array `arr[]`, consider every group of three consecutive elements in the array.

For each triplet `(arr[i], arr[i + 1], arr[i + 2])`, determine whether the three values can represent the sides of a valid triangle.

Return an array of length `n - 2` where the `i`th element is:

- `1` if `arr[i]`, `arr[i + 1]`, and `arr[i + 2]` can form a valid triangle.
- `0` otherwise.

Three sides `a`, `b`, and `c` form a valid triangle if and only if:

- `a + b > c`
- `a + c > b`
- `b + c > a`

## Examples

### Example 1

**Input:**
```text
arr[] = [1, 2, 2, 4]
```

**Output:**
```text
[1, 0]
```

**Explanation:**

The consecutive triplets are `[1, 2, 2]` and `[2, 2, 4]`.

- `[1, 2, 2]` forms a valid triangle.
- `[2, 2, 4]` does not form a valid triangle because `2 + 2 = 4`.

### Example 2

**Input:**
```text
arr[] = [2, 10, 2, 10, 2]
```

**Output:**
```text
[0, 1, 0]
```

**Explanation:**

The consecutive triplets are `[2, 10, 2]`, `[10, 2, 10]`, and `[2, 10, 2]`.

- `[2, 10, 2]` is not a valid triangle.
- `[10, 2, 10]` is a valid triangle.
- `[2, 10, 2]` is not a valid triangle.

## Constraints

- `3 ≤ n ≤ 10^5`
- `1 ≤ arr[i] ≤ 10^9`
