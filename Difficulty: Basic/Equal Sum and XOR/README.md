# Count Integers Satisfying `n + i = n ^ i`

## Problem

Given a positive integer `n`, count the number of integers `i` such that `0 <= i <= n` and `n + i = n ^ i`, where `^` is bitwise XOR.

## Examples

### Example 1
```text
Input: n = 7
Output: 1
```
Only `i = 0` satisfies the condition.

### Example 2
```text
Input: n = 12
Output: 4
```
The valid values are `i = 0, 1, 2, 3`.

## Constraints

- `1 <= n <= 10^3`

## Key Observation

For any two integers `a` and `b`:

```text
a + b = (a ^ b) + 2 * (a & b)
```

Therefore:

```text
n + i = n ^ i
```

holds exactly when:

```text
n & i = 0
```

So we only need to count the values of `i` from `0` to `n` for which `(n & i) == 0`.
