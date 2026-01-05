# Change All Even Position Bits to 0

## Problem Statement
You are given an integer `N`.  
Your task is to **change all bits at even positions to `0`** and return the resulting number.

> Bit positions are considered **1-based from the rightmost (LSB)**.

---

## Examples

### Example 1
**Input:**

N = 30


**Output:**

10


**Explanation:**
- Binary representation of `30` is `11110`
- Even positions (2, 4, ...) are highlighted  
- After setting even-position bits to `0`, we get `01010`
- Decimal value of `01010` is `10`

---

### Example 2
**Input:**

N = 10


**Output:**

10


**Explanation:**
- Binary representation of `10` is `1010`
- Even-position bits are already `0`
- Result remains `10`

---

## Complexity Analysis
- **Time Complexity:** `O(1)`
- **Auxiliary Space:** `O(1)`

---

## Constraints

1 <= N <= 32-bit integer


---
