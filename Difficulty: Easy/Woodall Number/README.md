# Woodall Number

## Problem

Given a positive integer `n`, find if it is a Woodall number.

A Woodall number is a positive integer that can be expressed in the form:

```text
k × 2^k − 1
```

for some positive integer `k`.

Return `true` if `n` is a Woodall number; otherwise, return `false`.

## Examples

### Example 1

```text
Input: n = 383
Output: true
```

Explanation:

```text
383 = 6 × 2^6 − 1
    = 6 × 64 − 1
    = 384 − 1
    = 383
```

Hence, `383` is a Woodall number.

### Example 2

```text
Input: n = 200
Output: false
```

Explanation:

There is no positive integer `k` such that:

```text
k × 2^k − 1 = 200
```

Therefore, `200` is not a Woodall number.

## Constraints

- `1 <= n <= 10^6`
