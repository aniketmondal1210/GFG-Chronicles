# Determine Data Type of Input

## Problem Statement
Given an input string `A`, determine its **data type** based on the following rules:

- Sequence of digits → `"int"`  
- Sequence of digits containing a dot → `"float"`  
- Sequence of characters (length > 1) → `"string"`  
- Single non-digit character → `"char"`

Return the detected data type as a string.

---

## Example 1
**Input:**  

A = "12"

**Output:**  

"int"

**Explanation:**  
The input consists only of digits, so it is of type `"int"`.

---

## Example 2
**Input:**  

A = "gfg"

**Output:**  

"string"

**Explanation:**  
The input consists only of characters, so it is of type `"string"`.

---

## Example 3
**Input:**  

A = "3.14"

**Output:**  

"float"

**Explanation:**  
The input has digits and a dot, so it is of type `"float"`.

---

## Example 4
**Input:**  

A = "x"

**Output:**  

"char"

**Explanation:**  
The input is a single non-digit character.

---

## Your Task
You don’t need to read or print anything.  
Your task is to complete the function **`FindInputType(A)`** which takes a string `A` and returns its data type.

---

## Expected Time Complexity

O(|A|)


## Expected Auxiliary Space

O(1)


---

## Constraints

1 ≤ |A| ≤ 1000


---
