# Minimum Index Character

## Problem Statement
You are given two strings **S** and **patt**.  
Your task is to find the character from **patt** that appears at the **minimum index** in string **S**.

- If multiple characters of `patt` are present in `S`, return the one whose **first occurrence index in `S` is smallest**.
- If none of the characters of `patt` are present in `S`, return **"$"**.

---

## Examples

### Example 1
**Input:**

S = "zsyle"
patt = "bjz"


**Output:**

"z"


**Explanation:**
- Characters of `patt` present in `S` → `'z'`
- `'z'` occurs at index `0` in `S`, which is the minimum.

---

### Example 2
**Input:**

S = "anskg"
patt = "me"


**Output:**

"$"


**Explanation:**
- None of the characters in `patt` appear in `S`

---

## Expected Complexity
- **Time Complexity:** `O(max(|S|, |patt|))`
- **Auxiliary Space:** `O(K)` where `K ≤ 26`

---

## Constraints

- 1 ≤ |S|, |patt| ≤ 10^4

---
