# GCD of LCM Problem

## Problem Statement
Given three integers `x`, `y`, `z`, the task is to compute the value of:

GCD(LCM(x,y), LCM(x,z))

where,  
- **GCD** = Greatest Common Divisor  
- **LCM** = Least Common Multiple  

Return the result as an integer.

---

## Examples

### Example 1:
**Input:**  

x = 15, y = 20, z = 100


**Process:**  
- LCM(15, 20) = 60  
- LCM(15, 100) = 300  
- GCD(60, 300) = 60  

**Output:**  

60


---

### Example 2:
**Input:**  

x = 30, y = 40, z = 400


**Process:**  
- LCM(30, 40) = 120  
- LCM(30, 400) = 1200  
- GCD(120, 1200) = 120  

**Output:**  

120

---
