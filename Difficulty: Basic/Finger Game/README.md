# Count Numbers on Fingers

## Problem Description

Count numbers on fingers in a back-and-forth sequential pattern to find the exact finger on which a given number $n$ ends.

### Finger Numbering & Pattern
- **Finger 1 (Thumb):** 1
- **Finger 2 (Index):** 2
- **Finger 3 (Middle):** 3
- **Finger 4 (Ring):** 4
- **Finger 5 (Little):** 5
- **Finger 4 (Ring):** 6
- **Finger 3 (Middle):** 7
- **Finger 2 (Index):** 8
- **Finger 1 (Thumb):** 9
- **Finger 2 (Index):** 10

The counting pattern forms a repeating cycle of **8 steps**:
`[1, 2, 3, 4, 5, 4, 3, 2]`

---

## Examples

### Example 1
- **Input:** `n = 3`
- **Output:** `3`
- **Explanation:** $3 \pmod 8 = 3$, which maps to Finger 3 (Middle Finger).

### Example 2
- **Input:** `n = 6`
- **Output:** `4`
- **Explanation:** $6 \pmod 8 = 6$, which maps to Finger 4 (Ring Finger).

---

## Constraints

- $1 \le n \le 10^6$

---
