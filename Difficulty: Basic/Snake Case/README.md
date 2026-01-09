# Convert a Sentence to Snake Case

## Problem Statement
You are given a sentence `S` of length `N` consisting only of **English alphabet characters and spaces**.

Your task is to convert the given sentence into **snake case**.

### Snake Case Rules
- All characters must be in **lowercase**
- All **spaces** must be replaced with an underscore (`_`)
- No leading spaces are present in the input

---

## Examples

### Example 1
**Input:**

N = 14
S = "Geeks ForGeeks"


**Output:**

"geeks_forgeeks"


**Explanation:**  
- Uppercase letters are converted to lowercase  
- Space is replaced with `_`

---

### Example 2
**Input:**

N = 21
S = "Here comes the garden"


**Output:**

"here_comes_the_garden"


**Explanation:**  
- All characters are converted to lowercase  
- Spaces are replaced with underscores

---

## Complexity Analysis
- **Time Complexity:** `O(N)`
- **Auxiliary Space:** `O(1)` (excluding output string)

---

## Constraints

- 1 ≤ N ≤ 10^5


---
