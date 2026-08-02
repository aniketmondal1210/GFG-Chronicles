# Calculate Player's Batting Average

## Problem Statement

You are given two arrays of the same size:

- `a[]` — runs scored by the player in each match.
- `b[]` — player's status in each match (`"out"` or `"notout"`).

The batting average is defined as:

```text
Total Runs / Number of Times Out
```

The result should be rounded **up** to the nearest integer (ceiling value).

If the player was **never out**, return `-1`.

---

## Examples

### Example 1

**Input**

```text
a[] = [10, 101, 49]
b[] = ["out", "notout", "out"]
```

**Output**

```text
80
```

**Explanation**

```text
Total Runs = 10 + 101 + 49 = 160

Times Out = 2

Average = ceil(160 / 2)
        = 80
```

---

### Example 2

**Input**

```text
a[] = [15, 42, 20]
b[] = ["out", "out", "notout"]
```

**Output**

```text
39
```

**Explanation**

```text
Total Runs = 15 + 42 + 20 = 77

Times Out = 2

Average = ceil(77 / 2)
        = ceil(38.5)
        = 39
```

---

## Constraints:

- 1 ≤ a.size() = b.size() ≤ 500
- 1 ≤ a[i] ≤ 300
- b[i] = "out" or b[i] = "notout"

---
