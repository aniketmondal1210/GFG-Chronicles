# Check if Pair with Given Sum Exists

## Problem Statement

Given an array `arr[]` and an integer `target`, determine whether there exist **two distinct indices** such that:

```text
arr[i] + arr[j] = target
```

Return `true` if such a pair exists, otherwise return `false`.

---

# Example 1

```text
Input:
arr[] = [0, -1, 2, -3, 1]
target = -2

Output:
true
```

### Explanation

```text
arr[3] + arr[4] = -3 + 1 = -2
```

---

# Example 2

```text
Input:
arr[] = [1, -2, 1, 0, 5]
target = 0

Output:
false
```

---

# Example 3

```text
Input:
arr[] = [11]
target = 11

Output:
false
```

### Explanation

```text
Only one element exists, so no pair is possible.
```

---

## Constraints:

- 1 ≤ arr.size ≤ 10^5
- -10^5 ≤ arr[i] ≤ 10^5
- -2*10^5 ≤ target ≤ 2*10^5

---
