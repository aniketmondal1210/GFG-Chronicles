# K-th Smallest Distinct Pair Sum From Two Arrays

## Problem Description

Given two integer arrays `a[]` and `b[]` and a positive integer `k`, form all possible sums `a[i] + b[j]` such that `0 <= i < a.size()` and `0 <= j < b.size()`.

Consider only **distinct** sums sorted in ascending order (1-indexed), and return the `k`-th smallest distinct sum. If there are fewer than `k` distinct sums, return `-1`.

---

## Examples

### Example 1
- **Input:** `a = [1, 2]`, `b = [3, 4]`, `k = 3`
- **Output:** `6`
- **Explanation:** All pair sums are `1 + 3 = 4`, `1 + 4 = 5`, `2 + 3 = 5`, and `2 + 4 = 6`. The distinct sums in sorted order are `4, 5, 6`, so the 3rd smallest is `6`.

### Example 2
- **Input:** `a = [1, 3, 4, 8, 10]`, `b = [20, 22, 30, 40]`, `k = 4`
- **Output:** `25`
- **Explanation:** The smallest distinct sums in order are `21` (`1 + 20`), `23` (`1 + 22`), `24` (`3 + 20` / `4 + 20`), and `25` (`3 + 22`). The 4th smallest distinct sum is `25`.

---

## Constraints

- $1 \le \text{a.size()}, \text{b.size()} \le 500$
- $1 \le \text{a}[i], \text{b}[i] \le 10^4$
- $1 \le k \le \text{a.size()} \times \text{b.size()}$

---
