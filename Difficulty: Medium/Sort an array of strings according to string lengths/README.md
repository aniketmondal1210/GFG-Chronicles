# Sort Strings by Length (Stable Sort)

## Problem Description

Given an array of strings `arr[]`, sort the array in ascending order based on the lengths of the strings. If two strings have the same length, maintain their original relative order (stable sort).

---

## Examples

### Example 1
- **Input:** `arr = ["GeeksforGeeeks", "I", "from", "am"]`
- **Output:** `["I", "am", "from", "GeeksforGeeeks"]`
- **Explanation:** The strings are sorted in increasing order of length: `"I"` (1), `"am"` (2), `"from"` (4), `"GeeksforGeeeks"` (14).

### Example 2
- **Input:** `arr = ["You", "are", "beautiful", "looking"]`
- **Output:** `["You", "are", "looking", "beautiful"]`
- **Explanation:** `"You"` and `"are"` both have length 3 and maintain their relative order. `"looking"` (7) and `"beautiful"` (9) follow.

---

## Constraints

- $1 \le 	{arr.size()} \le 10^5$
- $1 \le 	{arr}[i]	ext{.size()} \le 100$
- Each string contains only English letters.

---
