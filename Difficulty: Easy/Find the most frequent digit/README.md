# Most Occurring Digit in a Number

## Problem Statement
You are given a number **N** in the form of a **string**.  
Your task is to find the **digit that occurs most frequently** in the string.

- If **two or more digits** occur the same maximum number of times, return the **highest digit** among them.
- The result should be returned as a **string**.

---

## Examples

### Example 1
**Input**

N = "12234"

**Output**

2

**Explanation**  
Digit `2` occurs the most number of times.

---

### Example 2
**Input**

N = "1122"

**Output**

2

**Explanation**  
Digits `1` and `2` both occur twice, but `2` is greater than `1`.

---

## Time and Space Complexity
- **Time Complexity:** `O(len(N))`
- **Space Complexity:** `O(1)` (fixed size array of 10 digits)

---

## Constraints

- 1 ≤ len(N) ≤ 101000
- N consists only of digits (0–9)


---
