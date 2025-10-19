# Count the Number of Factors of a Number

## Problem Statement
You are given an integer `n`. Your task is to find the **number of factors** (divisors) of `n`.

---

## Input
- A single integer `n`.

**Constraints:**

1 ≤ n ≤ 10⁵


---

## Output
- Print the total number of factors of `n`.

---

## Explanation
A **factor** of a number `n` is any integer `i` such that `n % i == 0`.

To count the factors:
- Loop through numbers from 1 to √n.
- If `i` divides `n`, count both `i` and `n/i` (except when `i` = `n/i`).

---

## Examples

### Example 1
**Input:**

5

**Output:**

2

**Explanation:**
Factors of 5 are **1** and **5**.

---

### Example 2
**Input:**

25

**Output:**

3

**Explanation:**
Factors of 25 are **1**, **5**, and **25**.

---
