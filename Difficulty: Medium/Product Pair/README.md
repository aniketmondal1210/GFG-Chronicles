# Pair With Given Product

## Problem Statement

Given an integer array `arr[]` and an integer `target`:

Return:

- `true` → if there exists a pair whose product equals `target`
- `false` → otherwise

---

# Examples

### Example 1

```text
Input:
arr[] = [10, 20, 9, 40]
target = 400

Output:
true
```

### Explanation

```text
10 × 40 = 400
```

---

### Example 2

```text
Input:
arr[] = [-10, 20, 9, -40]
target = 30

Output:
false
```

### Explanation

```text
No pair has product 30
```

---

### Example 3

```text
Input:
arr[] = [-10, 0, 9, -40]
target = 0

Output:
true
```

### Explanation

```text
-10 × 0 = 0
```

---

## Constraints:

- 2 ≤ arr.size ≤ 10^5
- -10^8 ≤ arr[i] ≤ 10^8
- -10^18 ≤ target ≤ 10^18

---
