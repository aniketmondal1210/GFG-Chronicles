# Check String Length with Appended Number

## Problem Statement
You are given a string `s` where **a number is appended at the end** of the string.

Your task is to check whether the **length of the string excluding the last number** is **equal to the number appended at the end**.

- Return **1** if the condition is true
- Return **0** otherwise

---

## Examples

### Example 1
**Input:**

s = "geeks5"


**Output:**

1


**Explanation:**  
- String excluding the last number: `"geeks"`
- Length of `"geeks"` = 5  
- Appended number = 5  
Since both are equal, return `1`.

---

### Example 2
**Input:**

s = "geek5"


**Output:**

0


**Explanation:**  
- String excluding the last number: `"geek"`
- Length of `"geek"` = 4  
- Appended number = 5  
Since they are not equal, return `0`.

---

## Complexity Analysis
- **Time Complexity:** `O(|s|)`
- **Auxiliary Space:** `O(1)`

---

## Constraints

- 1 <= |s| <= 10^5

---
