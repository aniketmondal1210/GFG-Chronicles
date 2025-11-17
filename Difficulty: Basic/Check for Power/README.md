# Check if `y` is a Power of `x`

## Problem Statement
Given two positive integers **x** and **y**, determine whether **y is a power of x**.

Return:
- `True` → if there exists an integer `k ≥ 1` such that  
  `x^k = y`
- `False` → otherwise

---

## Example 1

**Input:**

x = 2, y = 8


**Output:**

True


**Explanation:**  
2³ = 8, so y is a power of x.

---

## Example 2

**Input:**

x = 1, y = 8


**Output:**

False


**Explanation:**  
1 raised to any power is always 1, so it can never become 8.

---

## Key Idea
To check whether **y is a power of x**:

- If **x = 1**: only `y = 1` is valid.
- Repeatedly divide `y` by `x` while divisible.
- If the result becomes `1`, then `y` is a power of `x`.

---

## Constraints

1 ≤ x ≤ 10³
1 ≤ y ≤ 10⁸


---
