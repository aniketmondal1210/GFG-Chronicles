# Problem: Count Elements With Exact Frequency

## Problem Statement

Given an array `arr[]` that may contain duplicates and a positive integer `k`, count the number of elements whose occurrence is exactly equal to:

```text
floor(arr.size() / k)
```

In other words, find the frequency threshold by dividing the size of the array by `k` and taking the floor value. Then count how many distinct elements occur exactly that many times.

---

## Example 1

**Input:**

```text
k = 2
arr[] = [1, 4, 1, 2, 4]
```

**Output:**

```text
2
```

**Explanation:**

The size of the array is `5`.

```text
floor(5 / 2) = 2
```

The frequencies are:

```text
1 -> 2 times
4 -> 2 times
2 -> 1 time
```

Both `1` and `4` occur exactly `2` times.

Therefore, the answer is:

```text
2
```

---

## Example 2

**Input:**

```text
k = 4
arr[] = [1, 1, 7, 1]
```

**Output:**

```text
1
```

**Explanation:**

The size of the array is `4`.

```text
floor(4 / 4) = 1
```

The frequencies are:

```text
1 -> 3 times
7 -> 1 time
```

Only `7` occurs exactly `1` time.

Therefore, the answer is:

```text
1
```

---

## Approach

Use a frequency map to count the occurrences of each distinct element.

1. Calculate the required frequency:

```text
frequency = floor(n / k)
```

where `n` is the size of `arr`.

2. Traverse the array and store the frequency of each element.
3. Count how many distinct elements have a frequency exactly equal to `frequency`.
4. Return the count.

---

## Complexity

### Time Complexity

```text
O(n)
```

The array is traversed once to build the frequency map.

### Auxiliary Space

```text
O(n)
```

In the worst case, all elements can be distinct.

---

## Constraints

```text
1 <= arr.size() <= 10^5
1 <= arr[i] <= 10^6
1 <= k <= arr.size()
```
