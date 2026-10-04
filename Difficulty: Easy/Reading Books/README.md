# Maximum Points from Reading Books

## Problem Description

Given two arrays `arr1[]` and `arr2[]` of size $N$, and an integer $k$:
- `arr1[i]` represents the time required to read a book of kind $i$ once.
- `arr2[i]` represents the points earned after reading a book of kind $i$ once.

Geek has total time $k$ minutes and must choose **exactly one kind of book**. He can read that chosen book repeatedly as many times as possible within $k$ minutes ($\lfloor k / 	ext{arr1}[i] 
floor$ times), but cannot read books of different kinds.

Return the **maximum possible points** Geek can earn.

---

## Examples

### Example 1
- **Input:** `k = 10`, `arr1 = [3, 4, 5]`, `arr2 = [4, 4, 5]`
- **Output:** `12`
- **Explanation:**
  - Kind 0: $\lfloor 10 / 3 
floor = 3$ times $
ightarrow 3 	imes 4 = 12$ points.
  - Kind 1: $\lfloor 10 / 4 
floor = 2$ times $
ightarrow 2 	imes 4 = 8$ points.
  - Kind 2: $\lfloor 10 / 5 
floor = 2$ times $
ightarrow 2 	imes 5 = 10$ points.
  - Maximum points earned: `12`.

### Example 2
- **Input:** `k = 12`, `arr1 = [8, 5]`, `arr2 = [100, 5]`
- **Output:** `100`
- **Explanation:**
  - Kind 0: $\lfloor 12 / 8 
floor = 1$ time $
ightarrow 1 	imes 100 = 100$ points.
  - Kind 1: $\lfloor 12 / 5 
floor = 2$ times $
ightarrow 2 	imes 5 = 10$ points.
  - Maximum points earned: `100`.

---

## Constraints

- $1 \le 	{arr1.size()} = 	{arr2.size()} \le 10^5$
- $1 \le k, {arr1}[i] \le 10^4$
- $0 \le {arr2}[i] \le 10^4$

---
