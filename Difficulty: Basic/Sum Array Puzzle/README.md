# Sum of Array Except Self

## Problem Statement

Given an integer array **arr[]**, modify the array such that:

```
arr[i] = sum of all elements of the array except arr[i]
```

In other words:

```
arr[i] = arr[0] + arr[1] + ... + arr[i-1] + arr[i+1] + ... + arr[n-1]
```

---

# Examples

### Example 1

**Input**
```
arr = [3, 6, 4, 8, 9]
```

**Output**
```
[27, 24, 26, 22, 21]
```

**Explanation**

```
i = 0 → 6 + 4 + 8 + 9 = 27
i = 1 → 3 + 4 + 8 + 9 = 24
i = 2 → 3 + 6 + 8 + 9 = 26
i = 3 → 3 + 6 + 4 + 9 = 22
i = 4 → 3 + 6 + 4 + 8 = 21
```

---

### Example 2

**Input**
```
arr = [0, 0, 1]
```

**Output**
```
[1, 1, 0]
```

**Explanation**

```
i = 0 → 0 + 1 = 1
i = 1 → 0 + 1 = 1
i = 2 → 0 + 0 = 0
```

---

## Constraint :

- 1 <= arr.size() <= 10^6
- 1 <= arr[i]<= 10^8

---
