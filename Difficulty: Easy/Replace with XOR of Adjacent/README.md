# Replace Each Element with XOR of Adjacent Elements

## Problem Statement

Given an array `arr[]`, replace each element as follows:

- First element:
  ```text
  arr[0] = arr[0] ^ arr[1]
  ```

- Last element:
  ```text
  arr[n-1] = arr[n-2] ^ arr[n-1]
  ```

- Middle elements:
  ```text
  arr[i] = arr[i-1] ^ arr[i+1]
  ```

**Note:** All replacements must be based on the original array values.

---

# Example 1

## Input

```text
arr = [2, 1, 4, 7]
```

## Output

```text
[3, 6, 6, 3]
```

### Explanation

```text
arr[0] = 2 ^ 1 = 3
arr[1] = 2 ^ 4 = 6
arr[2] = 1 ^ 7 = 6
arr[3] = 4 ^ 7 = 3
```

---

# Example 2

## Input

```text
arr = [5, 9, 2, 6, 7]
```

## Output

```text
[12, 7, 15, 5, 1]
```

---

## Constraints:

- 2 ≤ n ≤ 10^5
- 1 ≤ arr[i] ≤ 10^7

---
