# Last Coin in a Greedy Game

## Problem Description

You are given an integer array `arr[]` representing the values of coins arranged in a row. Two players play a game by picking coins alternately under the following rules:
- At each turn, a player can pick a coin from either the beginning or the end of the array.
- Both players follow a greedy strategy: they always pick the coin with the maximum value among the two available ends.
- The game continues until only one coin remains.

Return the value of the last remaining coin.

---

## Examples

### Example 1
- **Input:** `arr[] = [5, 3, 1, 6, 9]`
- **Output:** `1`
- **Explanation:** 
  - Pick `9` (right end), remaining: `[5, 3, 1, 6]`
  - Pick `6` (right end), remaining: `[5, 3, 1]`
  - Pick `5` (left end), remaining: `[3, 1]`
  - Pick `3` (left end), remaining: `[1]`
  - Final remaining coin: `1`

### Example 2
- **Input:** `arr[] = [5, 9, 2, 5]`
- **Output:** `2`

### Example 3
- **Input:** `arr[] = [11]`
- **Output:** `11`
- **Explanation:** Only one coin is present; no moves are made.

---

## Constraints

- $1 \le \text{arr.size()} \le 10^5$
- $1 \le \text{arr}[i] \le 10^6$

---
