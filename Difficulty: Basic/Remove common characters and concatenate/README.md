# Remove Common Characters and Combine Strings

## Problem Statement
Given two strings `s1` and `s2`, remove **all characters that are common** in both strings.  
Then, concatenate the **remaining (uncommon) characters** from `s1` followed by those from `s2`, while **preserving their original order**.

If no characters remain after removal, return `"-1"`.

---

## Examples

### Example 1
**Input:**

s1 = "aacdb"
s2 = "gafd"


**Output:**

cbgf


**Explanation:**
- Common characters: `a`, `d`
- Uncommon in `s1`: `c`, `b`
- Uncommon in `s2`: `g`, `f`
- Result: `cbgf`

---

### Example 2
**Input:**

s1 = "abcs"
s2 = "cxzca"


**Output:**

bsxz


**Explanation:**
- Common characters: `a`, `c`
- Uncommon in `s1`: `b`, `s`
- Uncommon in `s2`: `x`, `z`
- Result: `bsxz`

---

## Constraints

1 ≤ Length of s1, s2 ≤ 10^5

---
