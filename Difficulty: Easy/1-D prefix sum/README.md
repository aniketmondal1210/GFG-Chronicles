# Prefix Sum Array

## Problem

Given an array `arr[]`, compute its **prefix sum array**.

For each index `i`:

```text
prefixSum[i] = arr[0] + arr[1] + ... + arr[i]
```

The resulting array should have the same length as the original array.

---

## Example 1

### Input

```text
arr[] = [10, 20, 10, 5, 15]
```

### Output

```text
[10, 30, 40, 45, 60]
```

### Explanation

```text
prefixSum[0] = 10
prefixSum[1] = 10 + 20 = 30
prefixSum[2] = 10 + 20 + 10 = 40
prefixSum[3] = 10 + 20 + 10 + 5 = 45
prefixSum[4] = 10 + 20 + 10 + 5 + 15 = 60
```

---

## Example 2

### Input

```text
arr[] = [30, 10, 10, 5, 50]
```

### Output

```text
[30, 40, 50, 55, 105]
```

### Explanation

```text
prefixSum[0] = 30
prefixSum[1] = 30 + 10 = 40
prefixSum[2] = 30 + 10 + 10 = 50
prefixSum[3] = 30 + 10 + 10 + 5 = 55
prefixSum[4] = 30 + 10 + 10 + 5 + 50 = 105
```

---

## Constraints:

- 1 ≤ arr.size() ≤ 10^5
- 1 ≤ arr[i] ≤ 10^4

---
