# Reconstruct Array Using Bitwise OR

## Problem Statement

You are given an array `arr[]` of length `n`.  

You must **reconstruct the same array in-place** such that:

arr[i] = arr[i] OR arr[i+1]


where `OR` is the bitwise OR operation.

If `i+1` does not exist (i.e., `i` is the last index), then **arr[i] remains unchanged**.

---

## Example 1

**Input:**

n = 5
arr[] = {10, 11, 1, 2, 3}


**Output:**

11 11 3 3 3


**Explanation:**
- arr[0] = 10 OR 11 = 11  
- arr[1] = 11 OR 1 = 11  
- arr[2] = 1 OR 2 = 3  
- arr[3] = 2 OR 3 = 3  
- arr[4] = unchanged  

Resulting array: `{11, 11, 3, 3, 3}`

---

## Example 2

**Input:**

n = 4
arr[] = {5, 9, 2, 6}


**Output:**

13 11 6 6


**Explanation:**
- arr[0] = 5 OR 9 = 13  
- arr[1] = 9 OR 2 = 11  
- arr[2] = 2 OR 6 = 6  
- arr[3] = unchanged  

Resulting array: `{13, 11, 6, 6}`

---

## Your Task
Implement the function:

game_with_number(arr, n)


- Modify `arr[]` in-place.
- Replace each `arr[i]` with `arr[i] OR arr[i+1]`, except the last element.

---

## Expected Time Complexity

O(n)


## Expected Auxiliary Space

O(1)


---

## Constraints

- 1 ≤ n ≤ 10⁵
- 1 ≤ arr[i] ≤ 10⁷

---
