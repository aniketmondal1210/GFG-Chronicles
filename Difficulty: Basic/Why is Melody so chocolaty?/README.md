# Maximum Happiness from Two Adjacent Melodies

## Problem

Given an array `arr[]`, where each element represents the happiness Chunky gets by eating a melody, find the **maximum happiness** obtainable by eating **two adjacent melodies**.

In other words, find:

```text
max(arr[i] + arr[i + 1])
```

for all valid indices `i`.

---

## Example 1

### Input

```text
arr[] = [1, 2, 3, 4, 5]
```

### Output

```text
9
```

### Explanation

Adjacent sums:

```text
1 + 2 = 3
2 + 3 = 5
3 + 4 = 7
4 + 5 = 9
```

Maximum:

```text
9
```

---

## Example 2

### Input

```text
arr[] = [2, 1, 3, 4]
```

### Output

```text
7
```

### Explanation

Adjacent sums:

```text
2 + 1 = 3
1 + 3 = 4
3 + 4 = 7
```

Maximum:

```text
7
```

---

## Expected Time Complexity: O(n).
## Expected Auxiliary Space: O(1)

## Constraints:

- 2 ≤ arr.size() ≤ 10^6
- 0 ≤ arr[i] ≤ 10^5

---
