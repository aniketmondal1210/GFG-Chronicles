# Count Numbers Containing Digit 4

## Problem Statement
You are given an integer `n`.  
Your task is to **count** how many numbers from `1` to `n` (inclusive) contain the digit **4** at least once.

---

## Examples

### Example 1:
**Input:**  
`n = 9`  
**Output:**  
`1`  
**Explanation:**  
Only the number `4` contains the digit `4`.

---

### Example 2:
**Input:**  
`n = 44`  
**Output:**  
`9`  
**Explanation:**  
The numbers are:  
`4, 14, 24, 34, 40, 41, 42, 43, 44`  
Total = `9` numbers.

---

## Constraints
- `1 ≤ n ≤ 10^5`

---

## Expected Complexity
- **Time:** `O(n log n)` (log factor from converting numbers to strings or digit-check loop)
- **Space:** `O(1)`

---
