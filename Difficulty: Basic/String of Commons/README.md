# Common Alphabets in Two Strings

You are given two strings `s1` and `s2`, containing only English alphabets (both **uppercase** and **lowercase**).  
Your task is to find the alphabets that **occur in both strings**.

---

## 🔹 Rules
1. Uppercase and lowercase are **different characters** (`'A' != 'a'`).  
2. Do not include **duplicates**, even if the letter occurs multiple times.  
3. If no common characters are found, return `"nil"`.  
4. The result string must contain:
   - All **capital letters first**, sorted in ascending order (`A-Z`).
   - All **small letters next**, sorted in ascending order (`a-z`).

---

## 🔹 Examples

### Example 1
**Input:**  

s1 = "tUvGH", s2 = "Hhev"

**Output:**  

Hv

Explanation: The common letters are `H` and `v`.  
Capital letters first → `"H"`, then small letters → `"v"`.  
Final output = `"Hv"`.

---

### Example 2
**Input:**  

s1 = "aabb", s2 = "ccll"

**Output:**  

nil

Explanation: No common letters, hence `"nil"`.

---
