# Tower of Hanoi (Minimum Moves)

## Problem Description

Given $n$ disks, consider three rods: the starting rod (`from`), the target rod (`to`), and an auxiliary rod (`aux`). Initially, disks are placed on the starting rod. The smallest disk is placed on top and the largest at the bottom.

Calculate the minimum number of moves required to transfer all $n$ disks from the starting rod to the target rod, following these rules:
1. Only one disk can be moved at a time.
2. A disk can only be placed on top of a larger disk or on an empty rod.

---

## Examples

### Example 1
- **Input:** `n = 2`
- **Output:** `3`
- **Explanation:** Total 3 steps are taken to move 2 disks.

### Example 2
- **Input:** `n = 3`
- **Output:** `7`
- **Explanation:** Total 7 steps are taken to move 3 disks.

### Example 3
- **Input:** `n = 0`
- **Output:** `0`
- **Explanation:** Total 0 steps are taken for 0 disks.

---

## Constraints

- $0 \le n \le 20$

---
