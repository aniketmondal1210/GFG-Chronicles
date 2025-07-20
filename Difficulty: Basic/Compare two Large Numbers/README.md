# Compare Two Large Numbers

## Problem Statement

You will be given two non-negative numbers `a` and `b` represented as **strings**. Your task is to return:
- `1` if `a < b`
- `2` if `a > b`
- `3` if `a == b`

---

## Examples

### Example 1  
**Input:**  
`a = "1234"`  
`b = "12345"`  
**Output:**  
`1`  
**Explanation:**  
Since `1234 < 12345`, return 1.

---

### Example 2  
**Input:**  
`a = "100"`  
`b = "1"`  
**Output:**  
`2`  
**Explanation:**  
Since `100 > 1`, return 2.

---

### Example 3  
**Input:**  
`a = "987654321"`  
`b = "987654321"`  
**Output:**  
`3`  
**Explanation:**  
Since both numbers are equal, return 3.

---

## Constraints

- `1 ≤ |a|, |b| ≤ 155`  
- `'0' ≤ ai, bi ≤ '9'` (Each character is a digit)

---

## Expected Time Complexity

- **O(|a| + |b|)**

## Expected Auxiliary Space

- **O(|a| - |b|)**

---
