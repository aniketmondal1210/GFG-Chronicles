# Check if a Number (String) is Divisible by 36

## Problem Statement
You are given a number **S** in the form of a **string**.  
Your task is to determine whether this number is **divisible by 36**.

Return:
- `1` → if divisible by 36  
- `0` → otherwise

---

## Divisibility Rule for 36
A number is divisible by **36** if and only if:

1. It is divisible by **4**  
2. It is divisible by **9**

Why?  

36 = 4 × 9
gcd(4, 9) = 1

So both conditions must be satisfied.

---

### Check Divisible by 4
Last **two digits** of the number must form a number divisible by 4.

### Check Divisible by 9
Sum of digits must be divisible by 9.

---

## Example 1
**Input:**

S = "72"


**Output:**

1


**Explanation:**  
- 72 % 4 = 0  
- Sum of digits = 7 + 2 = 9 → divisible by 9  
So 72 is divisible by 36.

---

## Example 2
**Input:**

S = "7"


**Output:**

0


**Explanation:**  
7 is not divisible by 36.

---

## Your Task
Implement the function:

checkDivisible36(S)


The function should:
- Process the number as a string
- Return `1` if divisible by 36, else `0`

---

## Expected Time Complexity

O(|S|)


## Expected Auxiliary Space

O(1)

---

## Constraints

1 ≤ |S| ≤ 10⁵

---
