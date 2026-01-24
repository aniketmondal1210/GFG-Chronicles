# Count Same Characters at Corresponding Positions (Case-Insensitive)

## Problem Statement
You are given **two strings `A` and `B` of equal length**.  
Your task is to count how many times the characters at the **same index** in both strings are **exactly the same**, ignoring case differences.

---

## Examples

### Example 1
**Input:**

A = "choice"

B = "chancE"


**Output:**

4


**Explanation:**  
Matching positions (case-insensitive):
- Index 0 → c == c  
- Index 1 → h == h  
- Index 4 → e == e  
- Index 5 → e == E  

Total = **4**

---

### Example 2
**Input:**

A = "Geek"

B = "gang"


**Output:**

1


**Explanation:**  
Only index 0 matches:
- g == g  

Total = **1**

---

## Time & Space Complexity
- **Time Complexity:** `O(N)`
- **Auxiliary Space:** `O(1)`

---

## Constraints

- 1 ≤ A.length(), B.length() ≤ 10^4


---
