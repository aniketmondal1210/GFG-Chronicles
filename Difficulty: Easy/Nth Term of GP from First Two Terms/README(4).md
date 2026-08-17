# Problem: Nth Term of a Geometric Series

## Problem Statement

Given the first two terms `a` and `b` of a Geometric Series, find the **nth term** of the series.

For a geometric series, the common ratio is:

```text
r = b / a
```

The nth term is given by:

```text
a * r^(n - 1)
```

---

## Example 1

**Input:**

```text
a = 2
b = 3
n = 1
```

**Output:**

```text
2
```

**Explanation:**

The first term is already given as `2`.

Therefore:

```text
1st term = 2
```

---

## Example 2

**Input:**

```text
a = 1
b = 2
n = 5
```

**Output:**

```text
16
```

**Explanation:**

The common ratio is:

```text
r = 2 / 1 = 2
```

The fifth term is:

```text
a * r^(n - 1)
= 1 * 2^(5 - 1)
= 1 * 2^4
= 16
```

Therefore, the answer is:

```text
16
```

---

## Approach

The first two terms are `a` and `b`.

The common ratio is:

```text
r = b / a
```

The nth term of a geometric series is:

```text
a * r^(n - 1)
```

An iterative approach can also be used:

1. Start with `term = a`.
2. Repeat `n - 1` times.
3. Multiply `term` by the common ratio.
4. Return `term`.

Since the constraints are small, either approach is sufficient.

---

## Complexity

### Time Complexity

```text
O(n)
```

using the iterative approach.

### Auxiliary Space

```text
O(1)
```

Only a constant amount of extra space is required.

---

## Constraints

```text
-10 <= a, b <= 10
1 <= n <= 9
```
