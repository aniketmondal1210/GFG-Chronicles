# Nim-like XOR Game Winner

## Problem Description

Given an array `arr[]` of positive integers, two players take turns removing exactly one element from the array:
- Before every turn, if the bitwise XOR of all remaining elements is `0`, the player whose turn it is wins immediately.
- If the XOR is not `0`, the player must remove one element.
- Both players play optimally.
- If the array becomes empty, the XOR is considered `0`.

Return `true` if the second player wins; otherwise, return `false`.

---

## Examples

### Example 1
- **Input:** `arr[] = [1, 2, 3]`
- **Output:** `false`
- **Explanation:** The initial XOR sum is $1 \oplus 2 \oplus 3 = 0$. Therefore, the first player wins immediately.

### Example 2
- **Input:** `arr[] = [1, 2, 4]`
- **Output:** `true`
- **Explanation:** The initial XOR sum is non-zero, so the first player is forced to remove an element. With an odd number of elements initially, the second player secures the winning position.

---

## Constraints

- $1 \le \text{arr.size()} \le 10^5$
- $1 \le \text{arr}[i] \le 10^8$

---
