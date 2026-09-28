# Trimorphic Number Checker

## Problem Description

Given an integer $n$, determine whether it is a **Trimorphic Number**. 

A number $n$ is called **Trimorphic** if its cube ($n^3$) ends in $n$ itself. More formally, if $d$ is the number of digits in $n$, then $n$ is trimorphic if:

$$n^3 \pmod{10^d} = n$$

---

## Examples

### Example 1
- **Input:** `n = 1`
- **Output:** `true`
- **Explanation:** $1^3 = 1$. The cube ends with $1$.

### Example 2
- **Input:** `n = 2`
- **Output:** `false`
- **Explanation:** $2^3 = 8$. The cube does not end with $2$.

### Example 3
- **Input:** `n = 24`
- **Output:** `true`
- **Explanation:** $24^3 = 13824$. The last 2 digits of $13824$ are $24$.

---

## Constraints

- $0 \le n \le 1290$

---
