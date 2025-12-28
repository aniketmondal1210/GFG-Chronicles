# Count Wrongly Placed Balls

## Problem Statement
You are given a string `S` of length `N` representing balls placed on a table from index `1` to `N`.

- `'R'` denotes a **Red** ball  
- `'B'` denotes a **Blue** ball  

### Rules for Wrong Placement
- A **Red** ball placed at an **even index** is wrongly placed.
- A **Blue** ball placed at an **odd index** is wrongly placed.

Your task is to **count the number of wrongly placed balls**.

---

## Examples

### Example 1
**Input**

S = "RRBB"


**Output**

2


**Explanation**
- Index 2 → `'R'` on even index → wrong
- Index 3 → `'B'` on odd index → wrong  
Total wrongly placed balls = `2`

---

### Example 2
**Input**

S = "RBRB"


**Output**

0


**Explanation**
- All balls are placed correctly according to the rules.

---

## Time and Space Complexity
- **Time Complexity:** `O(N)`
- **Auxiliary Space:** `O(1)`

---

## Constraints

- 1 ≤ N ≤ 10^5
- S[i] ∈ {'R', 'B'}

---
