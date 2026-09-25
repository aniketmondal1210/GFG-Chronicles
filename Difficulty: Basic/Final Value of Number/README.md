# Number Trick Game - Find the Final Value

## Problem Description

A person randomly chooses a number $n$ between 1 and 10 and performs the following sequence of arithmetic operations:

1. **Double** the chosen number $n$.
2. **Add** an even number $k$ (given as input) to the result obtained in Step 1.
3. **Divide** the result from Step 2 by $2$.
4. **Subtract** the original chosen number $n$ from the result obtained in Step 3.

Your task is to calculate and return the final value obtained after performing all four operations.

---

## Examples

### Example 1
- **Input:** `k = 10`
- **Output:** `5`
- **Explanation:** 
  Suppose the chosen number $n = 3$:
  - **Step 1:** $3 \times 2 = 6$
  - **Step 2:** $6 + 10 = 16$
  - **Step 3:** $16 / 2 = 8$
  - **Step 4:** $8 - 3 = 5$

### Example 2
- **Input:** `k = 2`
- **Output:** `1`
- **Explanation:** 
  Suppose the chosen number $n = 8$:
  - **Step 1:** $8 \times 2 = 16$
  - **Step 2:** $16 + 2 = 18$
  - **Step 3:** $18 / 2 = 9$
  - **Step 4:** $9 - 8 = 1$

---

## Constraints

- $2 \le k \le 10^8$
- $k$ is an even integer.

---
