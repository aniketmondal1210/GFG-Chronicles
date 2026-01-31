# Transform the String

## Problem Statement
Given a string `str`, transform it using the following rules **in order**:

1. **Delete all vowels** from the string (`a, e, i, o, u` in both lowercase and uppercase).
2. **Insert `#` in front of every consonant**.
3. **Change the case** of every remaining letter  
   - Uppercase → Lowercase  
   - Lowercase → Uppercase  

If the resulting string is **empty**, return `"-1"`.

---

## Example

### Example 1
**Input:**

str = "aBAcAba"


**Output:**

#b#C#B


**Explanation:**
- Vowels (`a, A, A, a`) are removed.
- Remaining consonants: `B, c, b`
- Add `#` before each consonant.
- Change case:
  - `B → b`
  - `c → C`
  - `b → B`

Final result: `#b#C#B`

---

## Time & Space Complexity
- **Time Complexity:** `O(N)`  
- **Auxiliary Space:** `O(N)`  

where `N` is the length of the string.

---

## Constraints

- 1 <= str.length() <= 10^4


---
