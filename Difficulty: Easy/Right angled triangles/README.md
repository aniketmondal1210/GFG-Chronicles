# Check Right Angled Triangle

## Problem Statement
Given three integers `a`, `b`, and `c`, check if it is possible to form a **right-angled triangle** with sides of these lengths.

A triangle is right-angled if it satisfies the **Pythagorean theorem**:

x² + y² = z²

where `z` is the longest side.

---

## Example 1
**Input:**  

a = 3, b = 4, c = 5

**Output:**  

Yes

**Explanation:**  
We can form a right-angled triangle with sides of length 3, 4, and 5 because 3² + 4² = 5².

---

## Example 2
**Input:**  

a = 2, b = 5, c = 8

**Output:**  

No

**Explanation:**  
We cannot form a right-angled triangle with sides 2, 5, and 8.

---

## Your Task
You don't need to read input or print anything.  
Your task is to complete the function **`rightAngTri(a, b, c)`** which takes three integers as input and returns `"Yes"` if it is possible to form a right-angled triangle, otherwise `"No"`.

---

## Expected Time Complexity

O(log(max(a, b, c)))


## Expected Auxiliary Space

O(1)


---

## Constraints

1 ≤ a, b, c ≤ 10⁸


---
