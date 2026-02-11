# Check if a Number Exists in an Arithmetic Sequence

## Problem Statement
You are given three integers:

- `a` → First term of an arithmetic sequence  
- `c` → Common difference  
- `b` → Target value  

Determine whether `b` exists in the arithmetic sequence defined by:

a, a + c, a + 2c, a + 3c, ...


Return:
- `1` (or true) if `b` is present  
- `0` (or false) otherwise  

---

## Example 1

**Input:**

a = 1, b = 3, c = 2


**Output:**

true


**Explanation:**
Sequence: `1, 3, 5, 7, ...`  
3 is present in the sequence.

---

## Example 2

**Input:**

a = 1, b = 2, c = 3


**Output:**

false


**Explanation:**
Sequence: `1, 4, 7, 10, ...`  
2 is not present.

---

## Example 3

**Input:**

a = 1, b = 2, c = 4


**Output:**

false


**Explanation:**
Sequence: `1, 5, 9, 13, ...`  
2 is not present.

---

## Constraints

-10⁹ ≤ a, b, c ≤ 10⁹


---

## Time and Space Complexity

- **Time Complexity:** `O(1)`
- **Auxiliary Space:** `O(1)`

---
