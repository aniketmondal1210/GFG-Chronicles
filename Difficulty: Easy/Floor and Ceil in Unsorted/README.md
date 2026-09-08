# Floor and Ceil in an Unsorted Array

## Problem Description

Given an unsorted array `arr[]` of integers and an integer `x`, find the **floor** and **ceil** of `x` in `arr[]`.

- **Floor of x:** The largest element in `arr[]` that is smaller than or equal to `x`. If no such element exists, the floor is `-1`.
- **Ceil of x:** The smallest element in `arr[]` that is greater than or equal to `x`. If no such element exists, the ceil is `-1`.

Return an array/list of two integers representing `[floor, ceil]`.

---

## Examples

### Example 1
- **Input:** `x = 7`, `arr[] = [5, 6, 8, 9, 6, 5, 5, 6]`
- **Output:** `[6, 8]`
- **Explanation:** Floor of $7$ is $6$ (largest value $\le 7$), and ceil of $7$ is $8$ (smallest value $\ge 7$).

### Example 2
- **Input:** `x = 10`, `arr[] = [5, 6, 8, 8, 6, 5, 5, 6]`
- **Output:** `[8, -1]`
- **Explanation:** Floor of $10$ is $8$, but there is no element $\ge 10$, so ceil is `-1`.

---

## Constraints

- $1 \le \text{arr.size} \le 10^5$
- $1 \le \text{arr}[i], x \le 10^6$

---
