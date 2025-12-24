# Duck Number

## Problem Statement
A **Duck number** is a positive number that contains **at least one non-leading zero**.

### Rules
- Numbers with **only leading zeros** are **not** Duck numbers.
- A zero appearing **after any non-zero digit** makes the number a Duck number.

### Examples
- Duck numbers: `3210`, `8050896`, `70709`, `01203`
- Not Duck numbers: `035`, `0012`

You are given a number `N` as a **string**.  
Return **true** if `N` is a Duck number, otherwise return **false**.

---

## Examples

### Example 1
**Input:**  

N = "707069"


**Output:**  

YES


**Explanation:**  
The number contains a non-leading `0`.

---

### Example 2
**Input:**  

N = "02364"


**Output:**  

NO


**Explanation:**  
The `0` is only a leading zero.

---

## Time and Space Complexity
- **Time Complexity:** `O(|N|)`
- **Auxiliary Space:** `O(1)`

---

## Constraints

1 ≤ Length of N ≤ 10⁴

---
