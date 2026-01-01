# Merge Two Strings Alternately

## Problem Statement
You are given two strings **S1** and **S2**.  
Your task is to merge them **alternatively**, starting with the first character of **S1**, then the first character of **S2**, and so on.

🔹 If one string ends before the other, append the **remaining characters** of the longer string to the result.

---

## Examples

### Example 1
**Input:**

S1 = "Hello"
S2 = "Bye"


**Output:**

HBeylelo


**Explanation:**  
Characters are merged alternately:

H (S1) + B (S2) + e (S1) + y (S2) + l (S1) + l (S1) + o (S1)


---

### Example 2
**Input:**

S1 = "abc"
S2 = "def"


**Output:**

adbecf


**Explanation:**  
Each character from both strings is added alternately.

---

## Function Description
**Function Name:** `merge(S1, S2)`  
**Parameters:**  
- `S1`: First input string  
- `S2`: Second input string  

**Return Type:**  
- `string` — the merged string

---

## Complexity Analysis
- **Time Complexity:** `O(|S1| + |S2|)`
- **Auxiliary Space Complexity:** `O(1)` (excluding output string)

---

## Constraints

- 1 ≤ |S1|, |S2| ≤ 10³

---
