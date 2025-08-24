# Largest Number Without 9 in a Sentence

## Problem
Given a sentence containing **words** and **numbers**, find the **largest number** among them which does **not contain digit `9`**.  
If no such number exists, return `-1`.

- Numbers and words are separated by **spaces** only.
- It is guaranteed that there are no leading zeroes in the valid answer.

---

## Constraints
- `1 ≤ n ≤ 10^6` (length of sentence)
- `1 ≤ answer ≤ 10^18`

---

## Examples

### Example 1
**Input**

"This is alpha 5057 and 97"

**Output**

5057

**Explanation:**  
`97` has a `9`, so it is not valid.  
`5057` is the only valid number → return `5057`.

---

### Example 2
**Input**

"Another input 9007"

**Output**

-1

**Explanation:**  
All numbers contain `9`, hence return `-1`.

---
