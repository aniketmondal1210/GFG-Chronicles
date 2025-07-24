# Check Sum of Digits at Odd and Even Places

## Problem Statement

Given a number `S` in the form of a string, check whether the **sum of digits at odd places** is equal to the **sum of digits at even places** or not.

Positions are **1-based**, i.e., the first character of the string is at position 1 (odd), second at position 2 (even), and so on.

---

## Examples

### Example 1:

**Input:**  
`S = "132"`  
**Output:**  
`1`  
**Explanation:**  
Odd positions (1 and 3): 1 + 2 = 3  
Even position (2): 3  
Since both sums are equal, return `1`.

---

### Example 2:

**Input:**  
`S = "123"`  
**Output:**  
`0`  
**Explanation:**  
Odd positions (1 and 3): 1 + 3 = 4  
Even position (2): 2  
Since sums are not equal, return `0`.

---

## Constraints

- `1 ≤ |S| ≤ 10^5`

---

## Expected Time Complexity

- `O(|S|)`

## Expected Auxiliary Space

- `O(1)`

---
