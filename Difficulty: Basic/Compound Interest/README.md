# Compound Interest Calculation

## Problem
Calculate the amount for a given principal amount **P**, time **T** (in years), compounded **N** times in a year at rate **R**.  
Return the **floor value** of the future value of the given principal amount.

---

## Formula
The amount **A** is calculated as:

A = P × (1 + R / (100 × N))^(N × T)

Where:  
- **P** = Principal amount  
- **R** = Annual interest rate (in %)  
- **N** = Number of times interest is compounded per year  
- **T** = Time in years  

---

## Examples

### Example 1
**Input:**  
P = 1000, T = 2, N = 2, R = 10

**Process:**  
A = 1000 × (1 + 10 / (100 × 2))^(2 × 2)

A = 1000 × (1 + 0.05)^4

A = 1000 × 1.21550625

A ≈ 1215.51

Floor(A) = 1215


**Output:**  
1215

---

### Example 2
**Input:**  
P = 100, T = 1, N = 1, R = 10

**Process:**  
A = 100 × (1 + 10 / (100 × 1))^(1 × 1)

A = 100 × 1.1

A = 110


**Output:**  
110
---

## Constraints
- 1 ≤ P ≤ 1000  
- 1 ≤ T ≤ 20  
- 1 ≤ N ≤ 4  
- 1 ≤ R ≤ 20  

---

## Expected Complexity
- **Time Complexity:** O(log(N × T))  
- **Auxiliary Space:** O(1)  

---
