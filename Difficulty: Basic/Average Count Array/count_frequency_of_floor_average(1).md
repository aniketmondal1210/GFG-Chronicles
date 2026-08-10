# Problem: Count Frequency of Floor Average

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

## Approach

Use a frequency map to store the number of occurrences of every value in `arr[]`.

For each element `arr[i]`:

1. Calculate:

```text
avg = floor((arr[i] + x) / 2)
```

2. Find the frequency of `avg` in the frequency map.
3. Store that frequency in `result[i]`.

This avoids repeatedly scanning the entire array.

---

## Complexity

### Time Complexity

```text
O(n)
```

The array is traversed once to build the frequency map and once to construct the result.

### Auxiliary Space

```text
O(n)
```

The frequency map may contain up to `n` distinct values.

---

## Key Idea

The frequency of every value in `arr[]` can be calculated once using a hash map.

Then each calculated average can be looked up in `O(1)` average time.
