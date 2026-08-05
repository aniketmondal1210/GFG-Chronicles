# Check if a Number is a Narcissistic Number

## Problem Statement

Given an integer `n`, determine whether it is a **Narcissistic Number**.

A number is called **Narcissistic** if it is equal to the sum of each of its digits raised to the power of the total number of digits.

Mathematically:

```text
n = d1^k + d2^k + ... + dm^k
```

where:

- `d1, d2, ..., dm` are the digits of `n`
- `k` is the total number of digits

Return:

- `true` if `n` is a Narcissistic Number.
- `false` otherwise.

---

## Examples

### Example 1

**Input**

```text
n = 407
```

**Output**

```text
true
```

**Explanation**

```text
Number of digits = 3

4³ + 0³ + 7³
= 64 + 0 + 343
= 407
```

Since the sum equals the original number, it is a Narcissistic Number.

---

### Example 2

**Input**

```text
n = 111
```

**Output**

```text
false
```

**Explanation**

```text
Number of digits = 3

1³ + 1³ + 1³
= 1 + 1 + 1
= 3
```

Since `3 ≠ 111`, it is **not** a Narcissistic Number.

---

## Constraints:

- 1 ≤ n ≤ 10^5

---
