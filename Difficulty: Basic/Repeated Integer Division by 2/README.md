# Halve a Number M - 1 Times

## Problem Statement

Given two integers `n` and `m`, halve `n` exactly `m - 1` times using integer division.

Return the resulting value.

Integer division discards the fractional part after each division.

---

## Example 1

**Input:**

```text
n = 100
m = 4
```

**Output:**

```text
12
```

**Explanation:**

The number is halved exactly `3` times:

```text
100 / 2 = 50
50 / 2 = 25
25 / 2 = 12
```

Therefore, the result is:

```text
12
```

---

## Example 2

**Input:**

```text
n = 10
m = 5
```

**Output:**

```text
0
```

**Explanation:**

The number is halved exactly `4` times:

```text
10 / 2 = 5
5 / 2 = 2
2 / 2 = 1
1 / 2 = 0
```

Therefore, the result is:

```text
0
```

---

## Constraints

```text
1 <= n <= 10^9
1 <= m <= 31
```
