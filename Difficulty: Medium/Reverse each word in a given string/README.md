# Reverse Words in a String

## Problem
You are given a string `s`. Reverse each word in the string.  
- Words are separated by spaces.  
- The string may contain:
  - Leading spaces
  - Trailing spaces
  - Multiple spaces between words  

The output should have:  
- **No leading/trailing spaces**  
- **Exactly one space between words**  

---

## Constraints
- `1 ≤ s.size() ≤ 10^5`  
- `s` contains only **lowercase English alphabets and spaces**  

---

## Examples

### Example 1
**Input**

s = " i like this program very much "

**Output**

"i ekil siht margorp yrev hcum"

**Explanation**
- `"i"` → `"i"`
- `"like"` → `"ekil"`
- `"this"` → `"siht"`
- `"program"` → `"margorp"`
- `"very"` → `"yrev"`
- `"much"` → `"hcum"`

---

### Example 2
**Input**

s = " pqr mno "

**Output**

"rqp onm"


---

### Example 3
**Input**

s = "pqr"

**Output**

"rqp"


---
