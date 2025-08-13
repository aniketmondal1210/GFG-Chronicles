# Binary Next Number

## Problem
Given a binary number in the form of a string `s`, find the binary representation of `n + 1`, where `n` is the decimal equivalent of `s`.  
The output binary string should not contain leading zeros.

---

## Examples

### Example 1
**Input:**

s = "10"

**Output:**

11

**Explanation:**

Binary "10" = Decimal 2
2 + 1 = 3 → Binary representation = "11"


---

### Example 2
**Input:**

s = "111"

**Output:**

1000

**Explanation:**

Binary "111" = Decimal 7
7 + 1 = 8 → Binary representation = "1000"


---

## Constraints
- 1 ≤ n ≤ 10⁵ (length of binary string)
- `s` contains only '0' and '1'

---

## Expected Complexity
- **Time Complexity:** O(n) — iterate through binary digits once  
- **Auxiliary Space:** O(n) — to store the result

---
