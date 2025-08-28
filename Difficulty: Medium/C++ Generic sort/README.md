# Sort an Array of Different Data Types

## Problem Statement
You are given an array `a[]` of size `n`.  
The array can be of the following **data types**:
1. Integer  
2. String  
3. Floating point number  

Your task is to **sort the array in ascending order** and print the result.  

---

## Input Format
- First line contains two integers:  
  - `n` → size of the array  
  - `q` → type of array (1 = Integer, 2 = String, 3 = Float).  
- Next line contains `n` elements of type specified by `q`.  

---

## Output Format
- Print the sorted array in ascending order.  

---

## Examples

### Example 1
**Input:**  

3 3
34.23 -4.35 3.4


**Output:**  

-4.35 3.4 34.23


**Explanation:**  
Array type = floating point. After sorting: **-4.35 3.4 34.23**

---

### Example 2
**Input:**  

4 1
123 -2311 837 0


**Output:**  

-2311 0 123 837


**Explanation:**  
Array type = Integer. After sorting: **-2311 0 123 837**

---

## Constraints
- `1 <= T <= 50`  
- `1 <= n <= 10000`  
- `1 <= q <= 3`  
- Integer values range: `1 <= |Integer| <= 100000`  
- Float values range: `1.0 <= Floating Number <= 100000.0`  
- String length: `1 <= size <= 100`  
- String consists of only **lowercase English alphabets**.  

---
