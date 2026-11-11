# Swap Nibbles in a Byte

## Problem Description

Given a number `n` ($0 \le n \le 255$), the task is to swap its two nibbles and find the resulting number. 

A **nibble** is a four-bit aggregation (half an octet). An 8-bit byte consists of two nibbles: the upper 4 bits and the lower 4 bits.

---

## Examples

### Example 1
- **Input:** `n = 100`
- **Output:** `70`
- **Explanation:** 
  - `100` in binary is `01100100`. 
  - Two nibbles: `0110` (upper) and `0100` (lower). 
  - Swapping them yields `01000110`, which is `70` in decimal.

### Example 2
- **Input:** `n = 129`
- **Output:** `24`
- **Explanation:** 
  - `129` in binary is `10000001`. 
  - Two nibbles: `1000` (upper) and `0001` (lower). 
  - Swapping them yields `00011000`, which is `24` in decimal.

---

## Constraints

- $0 \le n \le 255$

---
