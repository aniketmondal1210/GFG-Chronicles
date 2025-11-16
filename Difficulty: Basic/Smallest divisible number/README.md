# Smallest Number Divisible by All Numbers from 1 to N

## Problem Statement
Given an integer **N**, find the smallest positive number that is **evenly divisible** by all integers from **1 to N**.

This value is also known as the **LCM of numbers from 1 to N**.

---

## Example 1

**Input:**

N = 3


**Output:**

6


**Explanation:**  
The smallest number divisible by 1, 2, and 3 is 6.

---

## Example 2

**Input:**

N = 6


**Output:**

60


**Explanation:**  
The smallest number divisible by 1, 2, 3, 4, 5, and 6 is 60.

---

## Key Idea
To compute the smallest number divisible by all numbers from 1 to N, compute:

LCM(1, 2, 3, ..., N)


Using the formula:

LCM(a, b) = (a × b) / GCD(a, b)


Iterate from 1 to N and keep updating the LCM.

---

## Your Task
Implement the function:

getSmallestDivNum(N)


which returns the smallest number evenly divisible by all numbers from 1 to N.

---

## Expected Time Complexity

O(N)


## Expected Auxiliary Space

O(1)


---

## Constraints

1 ≤ N ≤ 25

---
