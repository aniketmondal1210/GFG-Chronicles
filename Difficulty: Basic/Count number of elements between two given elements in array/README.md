# Count Elements Between Two Given Elements

## Problem Statement
You are given an **unsorted array** `arr[]` and two elements `num1` and `num2`.

Your task is to **count the number of elements that occur between `num1` and `num2`**, excluding both `num1` and `num2`.

### Important Rules
- If there are **multiple occurrences** of `num1`, consider the **leftmost occurrence**.
- If there are **multiple occurrences** of `num2`, consider the **rightmost occurrence**.
- Count only the elements **strictly between** these two indices.

---

## Examples

### Example 1
**Input:**

arr[] = [4, 2, 1, 10, 6]
num1 = 4
num2 = 6


**Output:**

3


**Explanation:**
- Leftmost index of `num1 (4)` = 0  
- Rightmost index of `num2 (6)` = 4  
- Elements between them = `[2, 1, 10]`  
- Count = **3**

---

### Example 2
**Input:**

arr[] = [3, 2, 1, 4]
num1 = 2
num2 = 4


**Output:**

1


**Explanation:**
- Leftmost index of `num1 (2)` = 1  
- Rightmost index of `num2 (4)` = 3  
- Elements between them = `[1]`  
- Count = **1**

---

## Expected Complexity
- **Time Complexity:** `O(n)`
- **Auxiliary Space:** `O(1)`

---

## Constraints

- 2 ≤ arr.size() ≤ 10^6
- 1 ≤ arr[i], num1, num2 ≤ 10^6

---
