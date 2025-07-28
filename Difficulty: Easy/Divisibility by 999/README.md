# Check if a Large Number is Divisible by 999

## Problem Statement

You are given a large number `N` in the form of a string. Your task is to check **whether the number is divisible by 999** without directly using division or modulo operations.

---

## Divisibility Rule for 999

To check if a number is divisible by 999:
- Divide the number into groups of **three digits from the right**.
- Add all those groups as integers.
- Repeat the process if needed, until a small enough number is obtained.
- If the final number is divisible by 999, then the original number is also divisible by 999.

---

## Examples

### Example 1:
**Input:**  
`N = "1998"`  
**Output:**  
`Divisible`  
**Explanation:**  
Split into groups: `1`, `998` → Sum = 1 + 998 = 999 → 999 is divisible by 999

---

### Example 2:
**Input:**  
`N = "99999999"`  
**Output:**  
`Not divisible`  
**Explanation:**  
Split into groups: `99`, `999`, `999` → Sum = 99 + 999 + 999 = 2097 → 2097 is not divisible by 999

---

## Constraints

- `1 <= |N| <= 10³`  
- The input string `N` contains only digits and represents a non-negative integer.

---

## Expected Time Complexity

- `O(len(N))`

## Expected Auxiliary Space

- `O(1)`

---
