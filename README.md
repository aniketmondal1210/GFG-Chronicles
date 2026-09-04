# Thief Escaping from Jail

## Problem

A thief has to cross `n` walls whose heights are given in `arr[]`.

In one jump:
- He climbs `x` feet.
- If he has not crossed the wall, he slips back by `y` feet.

After crossing a wall, he starts from ground level for the next wall.

Return the total number of jumps required to cross all walls.

## Examples

### Example 1

```text
Input: arr[] = {11, 10, 10, 9}, x = 10, y = 1
Output: 5
```

Explanation:

- Wall `11` → 2 jumps
- Wall `10` → 1 jump
- Wall `10` → 1 jump
- Wall `9` → 1 jump

Total = `5`.

### Example 2

```text
Input: arr[] = {25, 9}, x = 10, y = 2
Output: 4
```

Explanation:

For wall `25`:

```text
Jump 1: 0 → 10, slip to 8
Jump 2: 8 → 18, slip to 16
Jump 3: 16 → 26
```

So it takes `3` jumps. Wall `9` takes `1` jump.

Total = `4`.

## Constraints

```text
1 <= n <= 10^5
1 <= arr[i] <= 10^4
1 <= y < x <= 100
```

## Key Observation

If the wall height `h` is less than or equal to `x`, the thief crosses it in one jump.

Otherwise, every unsuccessful jump gives a net progress of:

```text
x - y
```

The final jump does not cause a slip because the wall has already been crossed.

For `h > x`:

```text
jumps = 1 + ceil((h - x) / (x - y))
```

Using integer arithmetic:

```text
ceil(a / b) = (a + b - 1) // b
```

## Python Solution

```python
def total_jumps(arr, x, y):
    total = 0
    net = x - y

    for h in arr:
        if h <= x:
            total += 1
        else:
            additional = (h - x + net - 1) // net
            total += 1 + additional

    return total
```

## Walkthrough

For:

```text
h = 25
x = 10
y = 2
```

Net progress:

```text
x - y = 8
```

The first jump reaches `10`, leaving `15` feet.

Additional jumps:

```text
ceil(15 / 8) = 2
```

Therefore:

```text
Total jumps = 1 + 2 = 3
```

## Why No Slip After the Final Jump?

The thief slips only if he has not crossed the wall.

For:

```text
h = 10
x = 10
```

the first jump reaches the top:

```text
0 → 10
```

Therefore, only `1` jump is needed.

## Complexity

- **Time:** `O(n)`
- **Space:** `O(1)`

Each wall is processed exactly once.

## Key Takeaway

For every wall:

```text
if h <= x:
    jumps = 1
else:
    jumps = 1 + ceil((h - x) / (x - y))
```

This gives an efficient `O(n)` solution with constant extra space.
