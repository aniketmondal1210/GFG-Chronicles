# Ceil of an Element in a Sorted Array

## Problem
Given a sorted array `arr[]` and an integer `x`, find the **index (0-based)** of the smallest element in `arr[]` that is **greater than or equal to `x`**.  

This element is called the **ceil of `x`**.  

If such an element does not exist, return `-1`.  
In case of multiple occurrences of the ceil, return the **first occurrence**.

---

## Input
- `arr[]`: A sorted array of integers.  
- `x`: An integer.  

---

## Output
- The index of the ceil element.  
- Return `-1` if no ceil exists.  

---

## Constraints
- `1 ≤ arr.size() ≤ 10^6`  
- `1 ≤ arr[i] ≤ 10^6`  
- `0 ≤ x ≤ arr[n-1]`  

---

## Expected Complexity
- **Time Complexity**: `O(log N)`  
- **Space Complexity**: `O(1)`  

---

## Examples

### Example 1
**Input**  

arr = [1, 2, 8, 10, 11, 12, 19]
x = 5

**Output**  

2

**Explanation**  
The smallest number `>= 5` is `8`, located at index `2`.

---

### Example 2
**Input**  

arr = [1, 2, 8, 10, 11, 12, 19]
x = 20

**Output**  

-1

**Explanation**  
There is no element `>= 20`, so return `-1`.

---

### Example 3
**Input**  

arr = [1, 1, 2, 8, 10, 11, 12, 19]
x = 0

**Output**  

0

**Explanation**  
The ceil of `0` is `1`. Since `1` occurs at indices `0` and `1`, we return the **first occurrence** at index `0`.

---
