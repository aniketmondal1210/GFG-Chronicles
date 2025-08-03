# Find Opposite Face of Dice

## Problem Statement

You are given a **cubic dice** with 6 faces. All the faces are labeled with numbers **1 to 6** like any standard dice.  

Given the number on one face (`n`), your task is to **determine the number on the opposite face** of the dice.

---

## Examples

### Example 1:
**Input:**  
n = 6  
**Output:**  
1  
**Explanation:** The number opposite to 6 on a standard dice is 1.

### Example 2:
**Input:**  
n = 2  
**Output:**  
5  
**Explanation:** The number opposite to 2 is 5.

---

## Dice Face Mapping

In a standard dice:
- 1 is opposite to 6  
- 2 is opposite to 5  
- 3 is opposite to 4  

Thus, the rule is:  
**opposite_face = 7 - n**

---

## Constraints

- 1 ≤ n ≤ 6

---
