# Minimum Deletions to Make Strings Equal

## Problem Statement
You are given two strings `s1` and `s2`, consisting only of lowercase English letters.  
Both strings are almost anagrams. Your task is to **count the number of characters that need to be deleted** from either string so that `s1` becomes equal to `s2`.

---

## Example 1
**Input:**  

s1 = "madame"
s2 = "madam"


**Output:**  

1


**Explanation:**  
- `s1 = "madame"`  
- `s2 = "madam"`  
- Extra `'e'` in `s1` must be deleted.  
- Total deletions = **1**.

---

## Complexity
- **Time Complexity:** `O(|s1| + |s2|)` (iterate both strings once).  
- **Space Complexity:** `O(1)` (since we only use an array of size 26).

---


## Constraints
- `1 <= |s1|, |s2| <= 10^4`  
- Strings consist only of lowercase English letters (`'a'`–`'z'`).

---
