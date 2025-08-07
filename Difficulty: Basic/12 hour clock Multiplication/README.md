# Product on a 12-Hour Clock

## Problem Statement

Given two positive integers `num1` and `num2`, find the product of the two numbers **on a 12-hour clock** rather than a number line.  
The clock runs from **0 hour** to **11 hours**.

---

## Examples

### Example 1:
**Input:**  
`num1 = 2`, `num2 = 3`  
**Output:**  
`6`  
**Explanation:** `2 × 3 = 6` → On a 12-hour clock, it is still **6**.

---

### Example 2:
**Input:**  
`num1 = 3`, `num2 = 5`  
**Output:**  
`3`  
**Explanation:** `3 × 5 = 15` → On a 12-hour clock: `15 % 12 = 3`.

---

## Constraints

- `1 ≤ num1, num2 ≤ 10³`

---

## Expected Time Complexity

  `O(1)`

## Expected Auxiliary Space

  `O(1)`
