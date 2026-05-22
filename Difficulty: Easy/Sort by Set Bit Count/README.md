# Sort Array According to Count of Set Bits

## Problem Statement

Given an array `arr[]` of integers, sort the array in **descending order** according to the number of set bits (`1s`) in their binary representation.

### Note

- If two numbers have the same count of set bits, maintain their original order (**stable sort**).

---

# Example 1

```text
Input:
arr[] = [5, 2, 3, 9, 4, 6, 7, 15, 32]

Output:
[15, 7, 5, 3, 9, 6, 2, 4, 32]
```

---

# Example 2

```text
Input:
arr[] = [1, 2, 3, 4, 5, 6]

Output:
[3, 5, 6, 1, 2, 4]
```

---

## Constraints:

- 1 ≤ arr.size() ≤ 10^5
- 1 ≤ arr[i] ≤ 10^6

---
