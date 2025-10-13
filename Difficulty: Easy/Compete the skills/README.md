# Compare Skills of Two Programmers

## Problem Statement

A and B are good friends and programmers. They decide to judge who is better by comparing their three skill values.

* Skills of A are stored in `arr1 = [a1, a2, a3]`
* Skills of B are stored in `arr2 = [b1, b2, b3]`

For each corresponding skill index `i`, the one with the higher skill value gets **1 point**. If both have equal skill values, no one gets a point.

Return the total points as `[points_of_A, points_of_B]`.

---

## Input

Two arrays of integers, `arr1` and `arr2`, each of size 3.

**Constraints:**

```
arr1.size(), arr2.size() = 3
1 ≤ arr1[i], arr2[i] ≤ 10^9
```

---

## Output

Return an array of two integers `[A_points, B_points]`.

---

## Examples

### Example 1

**Input:**

```
arr1 = [4, 2, 7]
arr2 = [5, 6, 3]
```

**Output:**

```
[1, 2]
```

**Explanation:**

```
4 < 5 → B gets 1 point
2 < 6 → B gets 1 point
7 > 3 → A gets 1 point
Result → [1, 2]
```

---

### Example 2

**Input:**

```
arr1 = [4, 2, 7]
arr2 = [5, 2, 8]
```

**Output:**

```
[0, 2]
```

**Explanation:**

```
4 < 5 → B gets 1 point
2 = 2 → no points
7 < 8 → B gets 1 point
Result → [0, 2]
```

---
