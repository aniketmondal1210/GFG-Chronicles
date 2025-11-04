# Problem: Find the Last Digit of (aᵇ) × (cᵈ) × (eᶠ)

## Problem Statement
Given six integers `a`, `b`, `c`, `d`, `e`, and `f`, find the **last digit** of the value obtained from the expression:

(a^b) * (c^d) * (e^f)


---

## Example 1
**Input:**  

a = 3
b = 66
c = 6
d = 41
e = 7
f = 53


**Output:**  

8


**Explanation:**  
After evaluating the expression, the last digit of the final result is **8**.

---

## Example 2
**Input:**  

a = 1
b = 1
c = 1
d = 1
e = 1
f = 1


**Output:**  

1


**Explanation:**  
The expression becomes `(1^1) * (1^1) * (1^1) = 1`, and the last digit is **1**.

---

## Your Task
You don't need to read input or print anything.  
Your task is to complete the function **`theLastDigit(a, b, c, d, e, f)`** which takes six integers as input and returns the **last digit** of the result.

---

## Expected Time Complexity

O(sqrt(N))


## Expected Auxiliary Space

O(1)


---

## Constraints

1 ≤ a, b, c, d, e, f ≤ 10⁹


---
