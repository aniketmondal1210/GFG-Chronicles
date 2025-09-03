# Top Three Largest Distinct Integers

## Problem Statement
You are given an array `arr[]`, and you need to find the **top three largest distinct integers** present in the array.  
Return an array of size **three** in descending order.  

- If there are less than three distinct elements in the array, return the available distinct numbers in descending order.

---

## Example 1
**Input:**

arr = [10, 4, 3, 50, 23, 90, 90]


**Output:**

[90, 50, 23]


**Explanation:**  
Since `90` appears twice, it is only counted once.  
The top 3 distinct largest numbers are `[90, 50, 23]`.

---

## Example 2
**Input:**

arr = [10, 10, 10]


**Output:**

[10]


**Explanation:**  
Only one distinct element exists, hence the answer is `[10]`.

---

## Example 3
**Input:**

arr = [6, 8, 9, 2, 1, 10]


**Output:**

[10, 9, 8]


---

## Constraints
- `1 <= arr.size() <= 10^5`
- `0 <= arr[i] <= 10^5`

---
