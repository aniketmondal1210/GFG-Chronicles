# Check if First Name and Last Name are Anagrams

Ankush challenges Ankit to complete his code which checks whether the **first name** and **last name** of a student are **anagrams** of each other.  

- Print `"ANAGRAM"` if they are anagrams.  
- Otherwise, print `"NOT ANAGRAM"`.  

---

## What is an Anagram?
An **anagram** of a string is another string that contains the **same characters** in a different order.  

Examples:  
- `"act"` and `"tac"` → Anagrams  
- `"hello"` and `"world"` → Not anagrams  

---

## Examples

### Example 1
**Input:**

rahul garg

**Output:**

NOT ANAGRAM

**Explanation:** First name and last name do not have the same characters.  

---

### Example 2
**Input:**

ankit kitan

**Output:**

ANAGRAM

**Explanation:** `"ankit"` and `"kitan"` contain the same characters.  

---

## Constraints
- `0 < len(first name), len(second name) ≤ 10^6`  

---

## Expected Complexity
- **Time Complexity:** O(n log n) (due to sorting)  
- **Space Complexity:** O(n)  

---
