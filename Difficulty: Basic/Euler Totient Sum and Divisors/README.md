# Sum of Euler Totient Values of All Divisors

## Problem

Given a number `n`, find the sum of the Euler Totient values of all the divisors of `n`.

## Examples

### Example 1

```text
Input:
n = 5

Output:
5
```

**Explanation:**  
The factors of `5` are `1` and `5`.

- `Φ(1) = 1`
- `Φ(5) = 4`

Therefore, the sum is `1 + 4 = 5`.

### Example 2

```text
Input:
n = 1

Output:
1
```

**Explanation:**  
`1` is the only factor of `1`, and `Φ(1) = 1`.

## Constraints

- `1 ≤ n ≤ 10^9`
