# Replace All Occurrences of a Word in a String

## Problem
You are given three strings `S`, `oldW`, and `newW`.  
Find all occurrences of the word `oldW` in `S` and replace them with the word `newW`.

---

## Constraints
- `1 ≤ |S| ≤ 1000`
- `1 ≤ |oldW|, |newW| ≤ |S|`
- **Expected Time Complexity:** `O(n²)`  
- **Expected Auxiliary Space:** `O(1)`

---

## Examples

### Example 1
**Input**

S = "xxforxx xx for xx"
oldW = "xx"
newW = "geeks"

**Output**

"geeksforgeeks geeks for geeks"

**Explanation:**  
All `"xx"` are replaced with `"geeks"`.

---

### Example 2
**Input**

S = "india is the xx country"
oldW = "xx"
newW = "best"

**Output**

"india is the best country"

**Explanation:**  
All `"xx"` are replaced with `"best"`.

---
