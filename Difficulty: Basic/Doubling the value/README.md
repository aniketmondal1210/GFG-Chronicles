# Find Final Value of B after Traversal

## Problem
You are given:  
- An integer array `arr[]` of size `N`.  
- An integer `B`.  

You must traverse the array **from the beginning**.  
- Whenever an element in the array equals `B`, **double `B`** and continue.  
- Return the value of `B` after completing the traversal.

---

## Input
- `arr[]`: array of integers  
- `N`: size of the array  
- `B`: starting integer  

---

## Output
- Final value of `B` after complete traversal.  

---

## Constraints
- `1 ≤ N ≤ 50`  
- `1 ≤ B ≤ 1000`  
- `1 ≤ arr[i] ≤ 10^18`  

---

## Examples

### Example 1
**Input**  

N = 5, B = 2
arr = [1, 2, 3, 4, 8]

**Output**  

16

**Explanation**  
- Initially `B = 2`.  
- At index `1`, we find `2 → B = 4`.  
- At index `2`, we find `4 → B = 8`.  
- At index `3`, we find `8 → B = 16`.  
- Final answer = `16`.  

---

### Example 2
**Input**  

N = 5, B = 3
arr = [1, 2, 3, 4, 8]

**Output**  

6

**Explanation**  
- Initially `B = 3`.  
- At index `2`, we find `3 → B = 6`.  
- No further matches.  
- Final answer = `6`.  

---
