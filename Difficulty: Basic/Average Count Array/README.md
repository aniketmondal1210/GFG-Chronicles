# Count Frequency of Floor Average

## Problem Statement

Given an integer array `arr[]` and an integer `x`, perform the following steps for each index `i` (0-based):

1. Calculate the floor value of the average of `arr[i]` and `x`:

```text
avg = floor((arr[i] + x) / 2)
```

2. Count how many times this calculated value occurs in the original array `arr[]`.
3. Store this count at index `i` of a new array `result[]`.

Return the array `result[]`.

---

## Example 1

**Input:**

```text
arr[] = [2, 4, 8, 6, 2]
x = 2
```

**Output:**

```text
[2, 0, 0, 1, 2]
```

**Explanation:**

For each element:

```text
arr[0] = 2:
floor((2 + 2) / 2) = 2
Value 2 appears 2 times.

arr[1] = 4:
floor((4 + 2) / 2) = 3
Value 3 does not appear.

arr[2] = 8:
floor((8 + 2) / 2) = 5
Value 5 does not appear.

arr[3] = 6:
floor((6 + 2) / 2) = 4
Value 4 appears 1 time.

arr[4] = 2:
floor((2 + 2) / 2) = 2
Value 2 appears 2 times.
```

Therefore:

```text
result[] = [2, 0, 0, 1, 2]
```

---

## Example 2

**Input:**

```text
arr[] = [9, 5, 2, 4, 0, 3]
x = 3
```

**Output:**

```text
[0, 1, 1, 1, 0, 1]
```

**Explanation:**

The calculated average values are:

```text
[6, 4, 2, 3, 1, 3]
```

Their frequencies in `arr[]` are:

```text
[0, 1, 1, 1, 0, 1]
```

Therefore:

```text
result[] = [0, 1, 1, 1, 0, 1]
```

---

## Constraints:

- 1 ≤ arr.size() ≤ 10^5
- 0 ≤ x ≤ 10^5
- 0 ≤ arr[i] ≤ 10^5

---
