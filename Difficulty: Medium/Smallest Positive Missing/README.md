# Smallest Positive Missing Number

## Problem
You are given an integer array `arr[]`.  
Your task is to find the **smallest positive number missing** from the array.

---

## Note
- Positive numbers start from **1**.  
- The array can contain negative integers and duplicates.  

---

## Input
- An array `arr[]` of integers.

---

## Output
- A single integer: the smallest positive number missing from the array.

---

## Constraints
- `1 ≤ arr.size() ≤ 10^5`  
- `-10^6 ≤ arr[i] ≤ 10^6`  

---

## Examples

### Example 1
**Input**  

arr = [2, -3, 4, 1, 1, 7]

**Output**  

3

**Explanation**  
The sequence of positive numbers present: 1, 2, 4, 7  
The smallest missing is **3**.

---

### Example 2
**Input**  

arr = [5, 3, 2, 5, 1]

**Output**  

4

**Explanation**  
The sequence of positive numbers present: 1, 2, 3, 5  
The smallest missing is **4**.

---

### Example 3
**Input**  

arr = [-8, 0, -1, -4, -3]

**Output**  

1

**Explanation**  
No positive numbers are present, so the smallest missing is **1**.

---
