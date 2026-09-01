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

## Approach

Because `n <= 1000`, iterate through every `i` from `0` to `n`:

1. Compute `n & i`.
2. If it equals `0`, increment the answer.
3. Return the count.

## Python Solution

```python
def count_values(n):
    count = 0

    for i in range(n + 1):
        if (n & i) == 0:
            count += 1

    return count
```

## Walkthrough

For `n = 12`:

```text
12 = 1100 (binary)
```

The valid values are `0, 1, 2, 3` because none shares a set bit with `12`.

For example, with `i = 2`:

```text
12 = 1100
 2 = 0010
     ----
&    0000
```

Thus:

```text
12 + 2 = 14
12 ^ 2 = 14
```

But for `i = 4`:

```text
12 = 1100
 4 = 0100
     ----
&    0100
```

The result is not zero, so `i = 4` is not valid.

## Complexity

- **Time:** `O(n)`
- **Space:** `O(1)`

## Key Takeaway

Transform the original equation:

```text
n + i = n ^ i
```

into the simpler bitwise condition:

```text
n & i = 0
```

Then count all `i` in `[0, n]` satisfying that condition.
