# Make the String Same-Coloured

## Problem Statement
You are given a string `S` of length `N` consisting only of uppercase characters:
- `'R'` → Red
- `'G'` → Green

Your task is to find the **minimum number of characters to change** so that **all characters in the string become the same colour**.

You may change any character from `'R'` to `'G'` or from `'G'` to `'R'`.

---

## Example 1

### Input

N = 5
S = "RGRGR"


### Output

2


### Explanation
- Count of `'R'` = 3  
- Count of `'G'` = 2  

Change the two `'G'` characters to `'R'`.  
Minimum changes required = **2**.

---

## Example 2

### Input

N = 7
S = "GGGGGGR"


### Output

1


### Explanation
- Count of `'G'` = 6  
- Count of `'R'` = 1  

Change the single `'R'` to `'G'`.  
Minimum changes required = **1**.

---

### Constraints

- 1 ≤ N ≤ 10⁵
- S consists only of characters 'R' and 'G'

---
