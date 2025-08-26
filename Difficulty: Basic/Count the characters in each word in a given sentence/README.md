# Count Characters in Each Word

## Problem
Given a string `S` containing multiple words, count the number of characters in each word and display them in order.

---

## Constraints
- `1 ≤ |S| ≤ 10^5`

Expected:
- **Time Complexity:** `O(|S|)`
- **Auxiliary Space:** `O(|S|)` (for storing the result)

---

## Examples

### Example 1
**Input**

S = "the quick brown fox"

**Output**

3 5 5 3

**Explanation**
- "the" → 3  
- "quick" → 5  
- "brown" → 5  
- "fox" → 3  

---

### Example 2
**Input**

S = "geeks for geeks"

**Output**

5 3 5

**Explanation**
- "geeks" → 5  
- "for" → 3  
- "geeks" → 5  

---

✅ Time Complexity = `O(|S|)` (single pass over the string)  
✅ Space Complexity = `O(|S|)` (for output array)

---
