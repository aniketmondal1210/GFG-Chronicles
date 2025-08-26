# Count Alphabets in a String

## Problem
Given a string `S`, count how many **alphabets** (both uppercase and lowercase letters) are present in it.  
Ignore digits and special characters.

---

## Constraints
- `1 ≤ |S| ≤ 10^5`
- String contains only:
  - Uppercase letters (`A–Z`)
  - Lowercase letters (`a–z`)
  - Digits (`0–9`)
  - Special characters: `# ! $ &`
- **Expected Time Complexity:** `O(|S|)`
- **Expected Auxiliary Space:** `O(1)`

---

## Examples

### Example 1
**Input**

S = "adjfjh23"

**Output**

6

**Explanation**  
Only the last 2 characters are digits, others are alphabets.

---

### Example 2
**Input**

S = "n0ji#k$"

**Output**

4

**Explanation**  
Characters `n, j, i, k` are alphabets.  
Others are digits/special characters.

---
