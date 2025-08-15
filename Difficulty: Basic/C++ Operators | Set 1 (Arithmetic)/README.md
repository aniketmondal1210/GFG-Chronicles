# Perform Arithmetic Operations on Two Numbers

## Problem
Given two integers `A` and `B`, perform **addition**, **multiplication**, **subtraction**, and **division** on these two numbers.

If `B > A`, subtraction should be `B - A` and division should be `B / A`.  
If `A > B`, subtraction should be `A - B` and division should be `A / B`.

---

## Examples

### Example 1
**Input:**

A = 1, B = 2

**Output:**

3 2 1 2

**Explanation:**
- Addition: 1 + 2 = 3  
- Multiplication: 1 × 2 = 2  
- Since B > A:  
  - Subtraction: 2 - 1 = 1  
  - Division: 2 ÷ 1 = 2  

---

### Example 2
**Input:**

A = 5, B = 7

**Output:**

12 35 2 1

**Explanation:**
- Addition: 5 + 7 = 12  
- Multiplication: 5 × 7 = 35  
- Since B > A:  
  - Subtraction: 7 - 5 = 2  
  - Division: 7 ÷ 5 = 1 (integer division)

---

## Constraints
- 1 ≤ A, B ≤ 10,000  

---

## Expected Complexity
- **Time Complexity:** O(1)  
- **Space Complexity:** O(1)

---
