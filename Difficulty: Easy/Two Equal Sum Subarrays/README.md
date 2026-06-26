# Split Array into Two Equal Sum Subarrays

## Problem

Given an array of integers `arr[]`, determine whether it can be split into **two contiguous subarrays** (without changing the order of elements) such that the sum of both subarrays is equal.

Return:

- `true` if such a split exists.
- `false` otherwise.

---

## Example 1

### Input

```text
arr = [1, 2, 3, 4, 5, 5]
```

### Output

```text
true
```

### Explanation

Split the array as:

```text
[1, 2, 3, 4] | [5, 5]
```

Sum of left subarray:

```text
1 + 2 + 3 + 4 = 10
```

Sum of right subarray:

```text
5 + 5 = 10
```

Both sums are equal.

---

## Example 2

### Input

```text
arr = [4, 3, 2, 1]
```

### Output

```text
false
```

### Explanation

No valid split exists where both subarrays have equal sum.

---

## Constraints:

- 1 ≤ arr.size() ≤ 10^5 
- 1 ≤ arr[i] ≤ 10^6

---
