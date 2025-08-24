# Pattern Search in a String

## Problem
You are given a string **S** and a pattern **P**, both consisting of lowercase characters.  
The task is to check whether the given pattern **P** exists in the string **S**.

- Return `true` if the pattern is found in the string, otherwise `false`.

---

## Constraints
- `1 ≤ |S|, |P| ≤ 10^3`  
- `S` and `P` contain only lowercase English letters.  

---

## Examples

### Example 1
**Input**

S = "aabaacaadaabaaabaa"
P = "aaba"

**Output**

Yes

**Explanation:**  
The pattern `aaba` occurs in `S` starting at index `0`.

---

### Example 2
**Input**

S = "aabaacaadaabaaabaa"
P = "ccda"

**Output**

No

**Explanation:**  
The pattern `ccda` does not occur in `S`.

---
