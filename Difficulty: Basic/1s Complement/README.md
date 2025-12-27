# One's Complement of a Binary Number

## Problem Statement
You are given an **N-bit binary number** represented as a string `S`.

Your task is to find the **1's complement** of the given binary number.

The **1's complement** of a binary number is obtained by:
- Replacing every `'1'` with `'0'`
- Replacing every `'0'` with `'1'`

Return the resulting binary string of length `N`.

---

## Examples

### Example 1
**Input:**  

N = 3
S = "101"


**Output:**  

010


**Explanation:**  
- `'1' → '0'`
- `'0' → '1'`
- `'1' → '0'`

---

### Example 2
**Input:**  

N = 2
S = "10"


**Output:**  

01


**Explanation:**  
Each bit in the binary string is inverted.

---

## Time and Space Complexity
- **Time Complexity:** `O(N)`
- **Space Complexity:** `O(N)`

---

## Constraints

1 ≤ N ≤ 100

---
