# Count Characters with Even Frequency

## Problem Statement

You are given a string `s` consisting of lowercase English letters.  
Your task is to **count how many distinct characters appear an even number of times** in the string.

---

## Examples

### Example 1:
**Input:**  
`s = "abacaba"`  
**Output:**  
`2`  
**Explanation:**  
- Frequency of 'a' = 4 (even)  
- Frequency of 'b' = 2 (even)  
- Frequency of 'c' = 1 (odd)  
So, there are 2 characters with even frequency: 'a' and 'b'.

---

### Example 2:
**Input:**  
`s = "zzacccz"`  
**Output:**  
`0`  
**Explanation:**  
- Frequency of 'z' = 3  
- Frequency of 'a' = 1  
- Frequency of 'c' = 3  
All frequencies are odd, so the answer is 0.

---

## Constraints

- `1 <= s.length <= 10^5`
- `s` contains only lowercase English letters.

---
