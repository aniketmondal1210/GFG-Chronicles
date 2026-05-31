# Search in a Step Array

## Idea

Since the array is a **step array**, the difference between adjacent elements is at most `k`.

If we are at index `i` and `arr[i] != x`, then we can safely skip:

```text
max(1, |arr[i] - x| / k)
```

positions.

This is because the value can change by at most `k` per step.

---

# Example 1

## Input

```text
arr = [4, 5, 6, 7, 6]
k = 1
x = 6
```

## Output

```text
2
```

---

# Example 2

## Input

```text
arr = [20, 40, 50]
k = 20
x = 70
```

## Output

```text
-1
```

---

## Expected Time Complexity: O(n)
## Expected Auxiliary Space: O(1)

## Constraints:

-  1 ≤ arr.size ≤ 10^5
- 1 ≤ k ≤ 10^2
- 1 ≤ arr[i], x ≤ 10^5

---
