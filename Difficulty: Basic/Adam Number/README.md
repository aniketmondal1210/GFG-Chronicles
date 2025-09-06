# Adam Number Check

## Problem Statement
Given a number `N`, check whether it is an **Adam Number**.  

A number is called an **Adam Number** if:
- Let `square1 = N^2`
- Let `rev(N)` be the reverse of `N`
- Let `square2 = (rev(N))^2`
- Then, `square1` should be the reverse of `square2`.

Return `"YES"` if `N` is an Adam Number, otherwise return `"NO"`.

---

## Examples

### Example 1
**Input:**

N = 12

**Output:**

YES

**Explanation:**  
- 12^2 = 144  
- Reverse of 12 = 21 → 21^2 = 441  
- Reverse of 144 = 441 → Matches. Hence, **Adam Number**.

---

### Example 2
**Input:**

N = 14

**Output:**

NO

**Explanation:**  
- 14^2 = 196  
- Reverse of 14 = 41 → 41^2 = 1681
- Reverse of 196 = 691 → Does not match 1681. Hence, **Not Adam Number**.

---

## Constraints
- 1 <= N <= 10^4
  
---
