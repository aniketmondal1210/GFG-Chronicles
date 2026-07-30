# Modify Array by Doubling Adjacent Equal Elements

## Problem

Given an array `arr[]` of size `n`, modify it using the following rules:

1. Traverse the array from left to right.
2. If two adjacent elements are equal and non-zero:
   - Double the first element.
   - Replace the second element with `0`.
3. After processing the entire array, move all `0`s to the end while maintaining the relative order of the non-zero elements.
4. Return the modified array.

---

## Examples

### Example 1

**Input**

```text
arr[] = [2, 2, 0, 4, 0, 8]
```

**Output**

```text
[4, 4, 8, 0, 0, 0]
```

**Explanation**

```text
2 and 2 are equal and non-zero.

Array becomes:
[4, 0, 0, 4, 0, 8]

After shifting all zeros:
[4, 4, 8, 0, 0, 0]
```

---

### Example 2

**Input**

```text
arr[] = [0, 2, 2, 2, 0, 6, 6, 0, 0, 8]
```

**Output**

```text
[4, 2, 12, 8, 0, 0, 0, 0, 0, 0]
```

**Explanation**

```text
2 and 2 become 4 and 0.

6 and 6 become 12 and 0.

After moving all zeros to the end:
[4, 2, 12, 8, 0, 0, 0, 0, 0, 0]
```

---

## Constraints:

- 1 ≤ arr.size() ≤ 10^5
- 0 ≤ arr[i] ≤ 10^6

---
