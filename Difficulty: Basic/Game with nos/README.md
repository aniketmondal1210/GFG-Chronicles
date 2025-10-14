# Reconstruct Array using XOR of Consecutive Elements

## Problem Statement

You are given an array `arr[]`, and you have to re-construct a new array where each element is obtained by performing **XOR** between consecutive elements of the original array.

Formally,

```
arr[i] = arr[i] XOR arr[i + 1] for i in range(0, n - 1)
```

The last element remains unchanged since there is no next element.

---

## Input

* An integer `n` representing the size of the array.
* An integer array `arr[]` of size `n`.

**Constraints:**

```
1 ≤ N ≤ 10^5
1 ≤ arr[i] ≤ 10^7
```

---

## Output

Return the reconstructed array after applying XOR operation between consecutive elements.

---

## Examples

### Example 1

**Input:**

```
n = 5
arr = [10, 11, 1, 2, 3]
```

**Output:**

```
[1, 10, 3, 1, 3]
```

**Explanation:**

```
arr[0] = 10 XOR 11 = 1
arr[1] = 11 XOR 1  = 10
arr[2] = 1  XOR 2  = 3
arr[3] = 2  XOR 3  = 1
arr[4] = 3         = 3 (no next element)
```

---

### Example 2

**Input:**

```
n = 4
arr = [5, 9, 7, 6]
```

**Output:**

```
[12, 14, 1, 6]
```

**Explanation:**

```
arr[0] = 5 XOR 9 = 12
arr[1] = 9 XOR 7 = 14
arr[2] = 7 XOR 6 = 1
arr[3] = 6        = 6 (no next element)
```

---
