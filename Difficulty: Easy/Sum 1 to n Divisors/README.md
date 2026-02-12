# Sum of All Divisors from 1 to n

## Problem Statement
Given a positive integer `n`, find the value of:



Σ F(i) where i = 1 to n


Where `F(i)` is defined as the **sum of all divisors of i**.

---

## Example 1

**Input:**


n = 4


**Output:**


15


**Explanation:**


F(1) = 1

F(2) = 1 + 2 = 3

F(3) = 1 + 3 = 4

F(4) = 1 + 2 + 4 = 7

Total = 1 + 3 + 4 + 7 = 15


---

## Example 2

**Input:**


n = 5


**Output:**


21


**Explanation:**


F(1) = 1

F(2) = 3

F(3) = 4

F(4) = 7

F(5) = 6

Total = 1 + 3 + 4 + 7 + 6 = 21


---

## Example 3

**Input:**


n = 1


**Output:**


1


---

## Constraints


1 ≤ n ≤ 10⁵


---

## Time and Space Complexity

- **Time Complexity:** `O(n)`
- **Auxiliary Space:** `O(1)`

---
