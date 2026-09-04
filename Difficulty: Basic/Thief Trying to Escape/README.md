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

