# Arrange String (Alphabets in Lexicographical Order + Sum of Digits)

## Problem Statement
You are given a string **S** containing only **uppercase English letters** (`A–Z`) and **digits** (`0–9`).

Your task is to:
1. Extract all **alphabets** and sort them in **lexicographical order**.
2. Compute the **sum of all digits** in the string.
3. Append the digit sum at the **end** of the sorted alphabets.
4. Return the resulting string.

---

## Examples

### Example 1
**Input:**

S = "AC2BEW3"


**Output:**

"ABCEW5"


**Explanation:**
- Alphabets → `A, C, B, E, W` → Sorted → `A, B, C, E, W`
- Digits → `2 + 3 = 5`
- Result → `"ABCEW" + "5"`

---

### Example 2
**Input:**

S = "ACCBA10D2EW30"


**Output:**

"AABCCDEW6"


**Explanation:**
- Alphabets → `A, C, C, B, A, D, E, W`
- Sorted → `A, A, B, C, C, D, E, W`
- Digits → `1 + 0 + 2 + 3 + 0 = 6`
- Result → `"AABCCDEW6"`

---

## Time and Space Complexity:
- Expected Time Complexity: O(|S|)
-  Expected Auxiliary Space: O(26)

## Constraints:

- 1 ≤ |S| ≤ 105
- S contains only upper case alphabets and digits.

---
