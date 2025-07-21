# Perfect Square ASCII Sum

## Problem Statement

You are given a string `S`. Your task is to determine if the **sum of ASCII values** of all characters results in a **perfect square** or not.  
If it is a perfect square, return `1`, otherwise return `0`.

---

## Examples

### Example 1:
**Input:**  
S = `"d"`  
**Output:**  
1  
**Explanation:**  
ASCII value of `'d'` is `100`, and `100` is a perfect square (`10 × 10`).

### Example 2:
**Input:**  
S = `"1Qy"`  
**Output:**  
0  
**Explanation:**  
ASCII values: `'1'` = 49, `'Q'` = 81, `'y'` = 121  
Total = 49 + 81 + 121 = 251, which is **not** a perfect square.

---

## Constraints

- 1 ≤ |S| ≤ 10⁵

---

## Expected Time Complexity

- O(|S|)

## Expected Auxiliary Space

- O(1)

---
