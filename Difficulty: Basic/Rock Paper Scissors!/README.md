# Rock Paper Scissors (RPS Game Result)

## Problem Statement

Two players **A** and **B** play Rock-Paper-Scissors.

Each chooses one move from:


{ R, P, S }


Where:
- `R` → Rock
- `P` → Paper
- `S` → Scissors

You are given a string `S` of length 2:
- `S[0]` → Move of Player A
- `S[1]` → Move of Player B

Return:
- `"A"` → If A wins
- `"B"` → If B wins
- `"DRAW"` → If both choose the same move

---

## Example 1

**Input**

S = "RR"


**Output**

DRAW


---

## Example 2

**Input**

S = "RS"


**Output**

A


**Explanation**
Rock crushes Scissors → A wins.

---

## ⏱️ Complexity

- **Time Complexity:** `O(1)`
- **Space Complexity:** `O(1)`

---

## Constraints

- |S| = 2
- S[i] ∈ {R, P, S}

---
