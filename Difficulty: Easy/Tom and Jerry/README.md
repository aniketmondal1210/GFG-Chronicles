# Divisor Game

## Problem Description

Given an integer `n`, Tom and Jerry play a game. On each turn, a player chooses a divisor of the current value of `n` that is less than `n` and subtracts it from `n`.

- The resulting value becomes the `n` for the next turn.
- A player who has no valid divisor to subtract loses the game.
- Tom makes the first move, and both players play optimally.

Return `true` if Tom wins; otherwise, return `false`.

---

## Examples

### Example 1
- **Input:** `n = 2`
- **Output:** `true`
- **Explanation:** Tom subtracts 1 from 2, making `n = 1`. Jerry has no valid move, so Tom wins.

### Example 2
- **Input:** `n = 3`
- **Output:** `false`
- **Explanation:** Tom can only subtract 1 from 3, making `n = 2`. Jerry then subtracts 1 from 2, making `n = 1`. Tom has no valid move, so Tom loses.

---

## Constraints

- $1 < n \le 10^8$

---
