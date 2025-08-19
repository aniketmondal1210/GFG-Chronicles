# Leftmost Index in Sorted Array

## Problem
Given a sorted array of integers of size `N` and a number `X`, find the **leftmost index** of `X` in the array `arr[]`.  

If `X` does not exist in the array, return `-1`.

---

## Input
- `arr[]`: a sorted array of integers (may contain duplicates).  
- `N`: size of the array.  
- `X`: target number.  

---

## Output
- The leftmost index of `X` in `arr[]`.  
- Return `-1` if `X` is not present.  

---

## Constraints
- `1 <= N <= 10^6`  
- `-10^5 <= arr[i] <= 10^5`  
- Array may contain duplicate elements.  

---

## Expected Complexity
- **Time Complexity**: `O(log N)`  
- **Space Complexity**: `O(1)`  

---

## Examples

### Example 1
**Input**  

N = 10
arr = [1, 1, 2, 2, 3, 4, 5, 5, 6, 7]
X = 1

**Output**  

0

**Explanation**  
Element `1` occurs at indices `0` and `1`. The leftmost occurrence is at index `0`.  

---

### Example 2
**Input**  

N = 5
arr = [2, 2, 3, 3, 4]
X = 4

**Output**  

4

**Explanation**  
Element `4` appears only once at index `4`.  

---
