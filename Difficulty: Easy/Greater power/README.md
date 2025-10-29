# Compare Powers — `greaterPower()`

## Problem Statement
Given four integers **a**, **b**, **m**, and **n**, determine whether **pow(a, b)** (i.e., \( a^b \)) is **greater than**, **less than**, or **equal to** **pow(m, n)** (i.e., \( m^n \)).

- Output **1** if \( a^b > m^n \)  
- Output **0** if \( a^b < m^n \)  
- Output **-1** if both are equal  

Since **b** and **n** can be very large (up to \( 10^{18} \)), directly computing the powers is **not feasible**.

---

## 🧮 Example

### **Example 1**
**Input:**
a = 2, b = 2, m = 3, n = 2

Computation:
2^2=4,3^2=9

Output:

0

Explanation: 4<94<9, so the output is 0.
Example 2

Input:

a = 1, b = 23, m = 1, n = 989

Computation:
1^23=1,1^989=1

Output:

-1

Explanation: Both values are equal, so the output is -1.
