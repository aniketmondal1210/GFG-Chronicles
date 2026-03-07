# Minimum Difference Between Any Pair in an Array

## Problem Statement

Given an array `arr[]`, find the **minimum absolute difference** between any pair of elements in the array.

---

## Examples

### Example 1

**Input**
```
arr[] = [2, 4, 5, 9, 7]
```

**Output**
```
1
```

**Explanation**

After sorting:
```
[2, 4, 5, 7, 9]
```

Differences:
```
4 - 2 = 2
5 - 4 = 1
7 - 5 = 2
9 - 7 = 2
```

Minimum difference = **1**

---

### Example 2

**Input**
```
arr[] = [3, 10, 8, 6]
```

**Output**
```
2
```

**Explanation**

After sorting:
```
[3, 6, 8, 10]
```

Differences:
```
6 - 3 = 3
8 - 6 = 2
10 - 8 = 2
```

Minimum difference = **2**

---

## Constraints:

- 2 <= arr.size() <= 10^5
- 1 <= arr[i] <= 10^9

---
