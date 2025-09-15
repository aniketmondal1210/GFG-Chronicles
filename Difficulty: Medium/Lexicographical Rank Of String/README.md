# Rank of a String in Lexicographic Order

## Problem
You are given a string `s` consisting of uppercase English letters.  
Find the **rank of the string** among all its permutations when sorted in lexicographical order.  
The rank starts from **1**.

---

### Examples

**Input:**

s = "ABC"

**Output:**

1

**Explanation:**  
Permutations in lexicographic order are:  
`ABC, ACB, BAC, BCA, CAB, CBA`.  
Here `"ABC"` is the **1st permutation**.

---

**Input:**

s = "CAB"

**Output:**

5

**Explanation:**  
Permutations in lexicographic order are:  
`ABC, ACB, BAC, BCA, CAB, CBA`.  
Here `"CAB"` is the **5th permutation**.

---

### Constraints
- `1 ≤ s.size() ≤ 8`

---
