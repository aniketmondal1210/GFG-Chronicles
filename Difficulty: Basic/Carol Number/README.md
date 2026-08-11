# Problem: Carol Number

## Problem Statement

A Carol number is defined as:

```text
4^n - 2^(n+1) - 1
```

Equivalently:

```text
(2^n - 1)^2 - 2
```

Given a number `n`, find the `n`th Carol number.

The first few Carol numbers are:

```text
-1, 7, 47, 223, 959, ...
```

The answer is guaranteed to fit in a 32-bit signed integer.

---

## Example 1

**Input:**

```text
n = 2
```

**Output:**

```text
7
```

**Explanation:**

The 2nd Carol number is:

```text
4^2 - 2^3 - 1
= 16 - 8 - 1
= 7
```

---

## Example 2

**Input:**

```text
n = 4
```

**Output:**

```text
223
```

**Explanation:**

The 4th Carol number is:

```text
4^4 - 2^5 - 1
= 256 - 32 - 1
= 223
```

---

## Constraints

```text
1 <= n <= 15
```

The answer is guaranteed to fit in a 32-bit signed integer.
