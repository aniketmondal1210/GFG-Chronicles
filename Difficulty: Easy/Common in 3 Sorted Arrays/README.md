# Common Elements in Three Sorted Arrays

## Problem
You are given three sorted arrays `arr1[]`, `arr2[]`, and `arr3[]` in **non-decreasing order**.  
Your task is to print all elements that are **common to all three arrays** in **non-decreasing order**.  

- If there are **no common elements**, return `[-1]`.  
- Ignore **duplicates** (each element should appear only once in the result).  

---

## Input
- Three sorted arrays `arr1`, `arr2`, and `arr3`.  

## Output
- An array containing common elements in sorted order (or `[-1]` if none).  

---

## Constraints
- `1 <= arr1.size(), arr2.size(), arr3.size() <= 10^5`  
- `-10^5 <= arr1[i], arr2[i], arr3[i] <= 10^5`  

---

## Examples

### Example 1
**Input**  

arr1 = [1, 5, 10, 20, 40, 80]
arr2 = [6, 7, 20, 80, 100]
arr3 = [3, 4, 15, 20, 30, 70, 80, 120]

**Output**  

[20, 80]

**Explanation**  
Only `20` and `80` are common across all three arrays.

---

### Example 2
**Input**  

arr1 = [1, 2, 3, 4, 5]
arr2 = [6, 7]
arr3 = [8, 9, 10]

**Output**  

[-1]

**Explanation**  
There are no common elements.

---

### Example 3
**Input**  

arr1 = [1, 1, 1, 2, 2, 2]
arr2 = [1, 1, 2, 2, 2]
arr3 = [1, 1, 1, 1, 2, 2, 2, 2]

**Output**  

[1, 2]

**Explanation**  
Duplicates are ignored, final output is unique.

---
