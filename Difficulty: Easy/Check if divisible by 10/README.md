# Check if Binary Number is Divisible by 10

## Problem
Given a binary number as a string, check whether its decimal representation is divisible by 10.  
The binary number can be very large, so direct integer conversion might not be possible.

---

## Examples

### Example 1
**Input:**

bin = "1010"

**Output:**

1

**Explanation:**

Binary "1010" = Decimal 10, which is divisible by 10. So, output is 1.


---

### Example 2
**Input:**

bin = "10"

**Output:**

0

**Explanation:**

Binary "10" = Decimal 2, which is not divisible by 10. So, output is 0.


---

## Constraints
- 1 ≤ |bin| ≤ 10⁵  
- `bin` consists only of '0' and '1'.

---

## Expected Complexity
- **Time Complexity:** O(N) — iterate through binary digits  
- **Auxiliary Space:** O(1)

---
