# Pronic Numbers

## Problem

Given an integer `n`, find all Pronic Numbers less than or equal to `n`.

A **Pronic Number** is a number that can be expressed as the product of
two consecutive non-negative integers:

`i × (i + 1)`

Return all such Pronic Numbers in increasing order.

## Examples

### Example 1

**Input:**

``` text
n = 6
```

**Output:**

``` text
0 2 6
```

**Explanation:** - `0 = 0 × 1` - `2 = 1 × 2` - `6 = 2 × 3`

### Example 2

**Input:**

``` text
n = 56
```

**Output:**

``` text
0 2 6 12 20 30 42 56
```

**Explanation:** - `0 = 0 × 1` - `2 = 1 × 2` - `6 = 2 × 3` -
`12 = 3 × 4` - `20 = 4 × 5` - `30 = 5 × 6` - `42 = 6 × 7` - `56 = 7 × 8`

## Constraints

-   `0 ≤ n ≤ 10^9`

## Approach

Every Pronic Number has the form:

``` text
i × (i + 1)
```

Start with `i = 0` and keep calculating `i × (i + 1)` while the result
is less than or equal to `n`.

Because `i × (i + 1)` increases as `i` increases, the generated numbers
are automatically in increasing order.

## Algorithm

1.  Initialize `i = 0`.
2.  Calculate `pronic = i × (i + 1)`.
3.  If `pronic > n`, stop.
4.  Add `pronic` to the result.
5.  Increment `i`.
6.  Repeat.

## Python Solution

``` python
def pronic_numbers(n):
    result = []
    i = 0

    while i * (i + 1) <= n:
        result.append(i * (i + 1))
        i += 1

    return result
```

## Example Usage

``` python
n = 56
print(pronic_numbers(n))
```

**Output:**

``` text
[0, 2, 6, 12, 20, 30, 42, 56]
```

## Complexity

The largest `i` satisfies approximately:

``` text
i² ≤ n
```

So there are about `√n` Pronic Numbers.

-   **Time Complexity:** `O(√n)`
-   **Space Complexity:** `O(√n)` for the output list

## Key Idea

Simply generate consecutive products:

``` text
0×1, 1×2, 2×3, 3×4, ...
```

and stop as soon as the product becomes greater than `n`.
