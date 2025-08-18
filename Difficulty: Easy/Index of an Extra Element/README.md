# Index of Extra Element

## Problem
You are given two **sorted arrays** `arr1[]` and `arr2[]` of distinct elements.  
The first array `arr1[]` has **one extra element** inserted at some position.  
Your task is to find the **index of this extra element** in `arr1[]`.

- Indexing is **0-based**.

---

## Input
- Two sorted arrays `arr1[]` and `arr2[]`.

---

## Output
- A single integer: the index of the extra element in `arr1[]`.

---

## Constraints
- `2 ≤ arr1.size() ≤ 10^5`  
- `1 ≤ arr1[i], arr2[i] ≤ 10^6`  

---

## Examples

### Example 1
**Input**  

arr1 = [2,4,6,8,9,10,12]
arr2 = [2,4,6,8,10,12]

**Output**  

4

**Explanation**  
`9` is extra in arr1, index = **4**.

---

### Example 2
**Input**  

arr1 = [3,5,7,8,11,13]
arr2 = [3,5,7,11,13]

**Output**  

3

**Explanation**  
`8` is extra in arr1, index = **3**.

---

### Example 3
**Input**  

arr1 = [3,5]
arr2 = [3]

**Output**  

1

**Explanation**  
`5` is extra, index = **1**.

---
