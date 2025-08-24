# Pattern Search in Text

## Problem
You are given a text string and a pattern string.  
The task is to check if the pattern exists in the text.

- Return `1` if the pattern is found in the text.  
- Return `0` otherwise.

---

## Constraints
- `1 ≤ |text|, |pat| ≤ 10^5`
- Strings contain only lowercase English letters.
- **Expected Time Complexity:** `O(|text| + |pat|)`
- **Expected Space Complexity:** `O(|text| + |pat|)`

---

## Examples

### Example 1
**Input**

text = "geeksforgeeks"
pat = "geek"

**Output**

1

**Explanation:** Pattern `"geek"` exists inside `"geeksforgeeks"`.

---

### Example 2
**Input**

text = "geeksforgeeks"
pat = "gfg"

**Output**

0

**Explanation:** `"gfg"` does not exist in the given text.

---
