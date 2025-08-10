# Sum of Arithmetic Progression

## Problem Statement
You are given:
- `n` → number of terms
- `a` → first term of the arithmetic progression (AP)
- `d` → common difference

Your task is to find the **sum of the series** up to the `n`th term.

The sum of an arithmetic progression can be calculated using the formula:

```
(n / 2) × [2a + (n - 1)d]
```

## Examples

### Example 1:
**Input:**  
`n = 5, a = 1, d = 3`  
**Output:**  
`35`  
**Explanation:**  
Series: `1, 4, 7, 10, 13`  
Sum = `1 + 4 + 7 + 10 + 13 = 35`

---

### Example 2:
**Input:**  
`n = 3, a = 1, d = 2`  
**Output:**  
`9`  
**Explanation:**  
Series: `1, 3, 5`  
Sum = `1 + 3 + 5 = 9`

---

## Constraints
- `1 ≤ n, a, d ≤ 100`

---
