# Good String Verification (Cyclic Alphabet Distance)

## Problem Description

Given a string `s`, determine if it is **good**. 

A string is considered **good** if the **cyclic distance** between every pair of adjacent characters is **exactly 1**.

- The **cyclic distance** between two lowercase English letters is the shortest distance between them in a circular alphabet arrangement ('a' through 'z').
  - For example, distance between `'a'` and `'c'` is 2, and distance between `'a'` and `'y'` is 2.
  - Wrap-around distance between `'z'` and `'a'` is 1.
- A string of length 1 is **always** considered good.

---

## Examples

### Example 1
- **Input:** `s = "aaa"`
- **Output:** `false`
- **Explanation:** The distance between adjacent `'a'` and `'a'` is $0$, which is not $1$.

### Example 2
- **Input:** `s = "cbc"`
- **Output:** `true`
- **Explanation:** 
  - Distance between `'c'` and `'b'` is $1$.
  - Distance between `'b'` and `'c'` is $1$.
  - All adjacent pairs have a cyclic distance of $1$.

---

## Constraints

- $1 \le 	ext{s.size()} \le 10^5$
- `s` consists of only lowercase English letters.

---
