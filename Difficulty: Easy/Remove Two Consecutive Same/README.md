# Pairwise Destruction

## Problem Description

Tom has sequences of words `arr[]` to manipulate. If in a sequence, two identical words come together, they destroy each other. Find the number of words left in the sequence after this pairwise destruction.

---

## Examples

### Example 1
- **Input:** `arr[] = ["ab", "aa", "aa", "bcd", "ab"]`
- **Output:** `3`
- **Explanation:** After the first iteration, we'll have: `ab bcd ab`. We can't further destroy more strings, and hence the result is 3.

### Example 2
- **Input:** `arr[] = ["tom", "jerry", "jerry", "tom"]`
- **Output:** `0`
- **Explanation:** After the first iteration: `tom tom`. After the second iteration: empty array. Hence, the result is 0.

---

## Constraints

- $1 \le 	{arr.size()} \le 10^6$
- $1 \le |	{arr}[i]| \le 50$

---
