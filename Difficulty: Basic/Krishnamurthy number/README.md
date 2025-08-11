# Krishnamurthy Number

## Problem
A **Krishnamurthy Number** is a number whose sum of the factorial of its digits is equal to the number itself.  
Given a number **N**, determine if it is a Krishnamurthy Number.  

Print `"YES"` if it is, otherwise print `"NO"`.

---

## Examples

### Example 1
**Input:**

N = 145

**Process:**

1! + 4! + 5! = 1 + 24 + 120 = 145
→ Equal to original number

**Output:**

YES


---

### Example 2
**Input:**

N = 14

**Process:**

1! + 4! = 1 + 24 = 25
→ Not equal to original number

**Output:**

NO


---

## Constraints
- 1 ≤ N ≤ 10^8

---

## Expected Complexity
- **Time Complexity:** O(|N|) — where |N| is the number of digits in **N**  
- **Auxiliary Space:** O(1)

---
