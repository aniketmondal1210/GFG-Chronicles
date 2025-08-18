# Transition Point in Sorted Binary Array

## Problem
You are given a **sorted array** `arr[]` containing only `0`s and `1`s.  
Your task is to find the **transition point** – the **first index** where `1` appears (all previous elements are `0`).  

- If the array does **not** contain any `1`, return `-1`.  
- If the array does **not** contain any `0`, return `0`.  

---

## Input
- A sorted array `arr[]` of size `n`.  

## Output
- The index of the transition point.  

---

## Constraints
- `1 ≤ arr.size() ≤ 10^5`  
- `0 ≤ arr[i] ≤ 1`  

---

## Examples

### Example 1
**Input**  

arr = [0, 0, 0, 1, 1]

**Output**  

3

**Explanation**  
Index `3` is the first occurrence of `1`.

---

### Example 2
**Input**  

arr = [0, 0, 0, 0]

**Output**  

-1

**Explanation**  
There are no `1`s in the array.

---

### Example 3
**Input**  

arr = [1, 1, 1]

**Output**  

0

**Explanation**  
The first index itself is `1`.

---

### Example 4
**Input**  

arr = [0, 1, 1]

**Output**  

1

**Explanation**  
Index `1` is the first occurrence of `1`.  

---
