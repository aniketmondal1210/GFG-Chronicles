# One's Complement of an Integer

## Problem Statement

Given an integer `N`, find its **one’s complement**.

The one’s complement of a number is obtained by flipping all bits in its binary representation — converting `0` to `1` and `1` to `0`.

---

## Input

* A single integer `N`.

**Constraints:**

```
1 ≤ N ≤ 10^6
```

---

## Output

Return the one’s complement of the integer `N` as a decimal number.

---

## Examples

### Example 1

**Input:**

```
N = 5
```

**Output:**

```
2
```

**Explanation:**

```
Binary of 5 = 101
One’s complement = 010
Which equals 2 in decimal.
```

---

### Example 2

**Input:**

```
N = 255
```

**Output:**

```
0
```

**Explanation:**

```
Binary of 255 = 11111111
One’s complement = 00000000 → 0
```

---

**Expected Complexity:**

* Time Complexity: **O(1)**
* Space Complexity: **O(1)**

---
