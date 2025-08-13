# Binary Representation of (n-1)

## Problem
You are given the binary representation of a number `n` as a string `S`.  
Your task is to return the binary representation of `n - 1`.  
It is guaranteed that `n > 0`.

---

## Examples

### Example 1
**Input:**

S = "11"

**Output:**

10

**Explanation:**

"11" in binary = 3 in decimal.
n - 1 = 2, whose binary representation is "10".


---

### Example 2
**Input:**

S = "1000"

**Output:**

111

**Explanation:**

"1000" in binary = 8 in decimal.
n - 1 = 7, whose binary representation is "111".


---

## Constraints
- 1 ≤ N ≤ 10⁴  (`N` is the length of binary string `S`)

---

## Expected Complexity
- **Time Complexity:** O(N)  
- **Auxiliary Space:** O(N) — to store the resulting binary string.

---
