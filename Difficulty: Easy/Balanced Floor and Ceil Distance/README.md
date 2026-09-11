# Equal Distance to Floor and Ceil

## Problem Description

Given a sorted array `arr[]` and an integer `x`, determine if the absolute difference between `x` and its **floor** is equal to the absolute difference between `x` and its **ceil**.

- **Floor of `x`:** The largest element in the array that is less than or equal to `x`.
- **Ceil of `x`:** The smallest element in the array that is greater than or equal to `x`.

> **Note:** If `x` itself is present in the array, its floor and ceil will both equal `x`, making the absolute differences equal ($0 = 0$), so the result is `true`. If `x` lies strictly outside the range of elements in `arr[]` (i.e., `x` is smaller than `arr[0]` or larger than `arr[n-1]`), either the floor or ceil will not exist, making the answer `false`.

---

## Examples

### Example 1
- **Input:** `arr[] = [1, 2, 8, 10, 10, 12, 19]`, `x = 5`
- **Output:** `true`
- **Explanation:** 
  - Floor of `5` = `2`
  - Ceil of `5` = `8`
  - Distance to floor: $|5 - 2| = 3$
  - Distance to ceil: $|8 - 5| = 3$
  - Since distances are equal ($3 = 3$), output is `true`.

### Example 2
- **Input:** `arr[] = [1, 2, 5, 7, 8, 11, 12, 15]`, `x = 9`
- **Output:** `false`
- **Explanation:** 
  - Floor of `9` = `8`
  - Ceil of `9` = `11`
  - Distance to floor: $|9 - 8| = 1$
  - Distance to ceil: $|11 - 9| = 2$
  - Since distances are not equal ($1 
eq 2$), output is `false`.

### Example 3
- **Input:** `arr[] = [1, 2, 10]`, `x = 2`
- **Output:** `true`
- **Explanation:** `x = 2` is present in the array. Floor = `2`, Ceil = `2`. Both distances are $0$.

---

## Constraints

- $1 \le 	{arr.size()} \le 10^5$
- $0 \le 	{arr}[i] \le 10^6$
- $1 \le x \le 10^6$
- The array `arr[]` is sorted in non-decreasing order.

---
