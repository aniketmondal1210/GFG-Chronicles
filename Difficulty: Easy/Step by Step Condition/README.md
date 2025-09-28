# Ladder If-Else: Divisibility Check

## Problem Statement
You are given a positive integer `n`.  
Your task is to check if it is divisible as follows:

1. If divisible by **11**, print `"Eleven"`.  
2. Else if divisible by **3**, print `"Three"`.  
3. Else if divisible by **2**, print `"Two"`.  
4. Otherwise, print `"-1"`.  

⚡ **Note:**  
If `n` is divisible by more than one of the numbers, choose the **largest one** among 11, 3, and 2.

---

## Examples

### Example 1
**Input:**  

n = 3

**Output:**  

Three


---

### Example 2
**Input:**  

n = 11

**Output:**  

Eleven


---

### Example 3
**Input:**  

n = 6

**Output:**  

Three

**Explanation:**  
6 is divisible by both 2 and 3, but since 3 is larger than 2, we print `"Three"`.

---

## Constraints
- `1 <= n <= 10^6`

---

## Expected Complexity
- **Time Complexity:** `O(1)`  
- **Auxiliary Space:** `O(1)`  

---
