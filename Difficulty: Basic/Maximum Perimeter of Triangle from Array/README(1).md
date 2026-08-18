# Maximum Perimeter of a Triangle

## Problem Statement

Given an array `arr[]` of positive integers, find the **maximum perimeter of a triangle** that can be formed using three elements from the array.

For three side lengths `a`, `b`, and `c` to form a valid triangle, the following condition must hold:

```text
a + b > c
```

where `c` is the largest side.

If no valid triangle can be formed, return `-1`.

---

## Example 1

**Input:**

```text
arr[] = [6, 1, 6, 5, 8, 4]
```

**Output:**

```text
20
```

**Explanation:**

The triangle is formed using:

```text
8, 6, 6
```

Check the triangle condition:

```text
6 + 6 > 8
```

Perimeter:

```text
8 + 6 + 6 = 20
```

---

## Example 2

**Input:**

```text
arr[] = [7, 55, 20, 1, 4, 33, 12]
```

**Output:**

```text
-1
```

**Explanation:**

No three elements satisfy the triangle inequality condition.

Therefore:

```text
-1
```

---

## Constraints

```text
1 <= arr.size() <= 10^6
1 <= arr[i] <= 10^5
```
