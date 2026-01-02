# Check if All 0's Are Together in a Binary String

## Problem Statement
You are given a binary string `str` consisting only of characters `'0'` and `'1'`.

Your task is to check whether **all the `'0'` characters appear together (contiguously)** in the string.

- Return **1** if all `'0'`s are together.
- Return **0** otherwise.

---

## Examples

### Example 1
**Input:**

str = "000"

**Output:**

YES

**Explanation:**  
All the `0`s appear together in one continuous block.

---

### Example 2
**Input:**

str = "111"

**Output:**

NO

**Explanation:**  
There are no `0`s in the string, so they are not considered together.

---

## Function Description
**Function Name:** `checkTogether(str)`  

**Parameters:**
- `str` (string): Binary string containing only `'0'` and `'1'`

**Returns:**
- `1` → if all `0`s are together  
- `0` → otherwise

---

## Complexity Analysis
- **Time Complexity:** `O(N)`  
- **Auxiliary Space:** `O(1)`

---

## Constraints

- 1 ≤ |str| ≤ 10000

---
