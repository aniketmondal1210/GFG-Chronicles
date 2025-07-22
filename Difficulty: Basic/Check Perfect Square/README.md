# Check Perfect Square using Only Addition and Subtraction

## Problem Statement

Given a positive integer `n`, determine if it is a **perfect square**, using **only addition and subtraction operations**.

A number is a perfect square if there exists an integer `x` such that `x * x = n`.

---

## Examples

### Example 1:
**Input:**  
`n = 35`  
**Output:**  
`0`  
**Explanation:**  
35 is not a perfect square because √35 ≈ 5.91, and 5 × 5 = 25 ≠ 35.

---

### Example 2:
**Input:**  
`n = 49`  
**Output:**  
`1`  
**Explanation:**  
√49 = 7, and 7 × 7 = 49, so 49 is a perfect square.

---

## Constraints

- `1 ≤ n ≤ 10⁵`

---

## Expected Time Complexity

- `O(√n)`

## Expected Auxiliary Space

- `O(1)`

---
