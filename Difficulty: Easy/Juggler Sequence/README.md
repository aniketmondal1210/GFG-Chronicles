# Juggler Sequence

## Problem Description

The **Juggler Sequence** is a series of integers starting with a positive integer $n$. Each subsequent term is generated from the previous term using the following recurrence relation:

$$a_{k+1} = \begin{cases} \lfloor a_k^{1/2} \rfloor = \lfloor \sqrt{a_k} \rfloor & \text{if } a_k \text{ is even} \\ \lfloor a_k^{3/2} \rfloor = \lfloor \sqrt{a_k^3} \rfloor & \text{if } a_k \text{ is odd} \end{cases}$$

Given an integer $n$, generate the complete Juggler Sequence starting from $n$ until it reaches $1$.

---

## Examples

### Example 1
- **Input:** `n = 9`
- **Output:** `[9, 27, 140, 11, 36, 6, 2, 1]`
- **Explanation:**
  - $a_0 = 9$ (Odd) $\rightarrow \lfloor \sqrt{9^3} \rfloor = \lfloor \sqrt{729} \rfloor = 27$
  - $a_1 = 27$ (Odd) $\rightarrow \lfloor \sqrt{27^3} \rfloor = \lfloor \sqrt{19683} \rfloor = 140$
  - $a_2 = 140$ (Even) $\rightarrow \lfloor \sqrt{140} \rfloor = 11$
  - $a_3 = 11$ (Odd) $\rightarrow \lfloor \sqrt{11^3} \rfloor = \lfloor \sqrt{1331} \rfloor = 36$
  - $a_4 = 36$ (Even) $\rightarrow \lfloor \sqrt{36} \rfloor = 6$
  - $a_5 = 6$ (Even) $\rightarrow \lfloor \sqrt{6} \rfloor = 2$
  - $a_6 = 2$ (Even) $\rightarrow \lfloor \sqrt{2} \rfloor = 1$

### Example 2
- **Input:** `n = 6`
- **Output:** `[6, 2, 1]`
- **Explanation:**
  - $a_0 = 6$ (Even) $\rightarrow \lfloor \sqrt{6} \rfloor = 2$
  - $a_1 = 2$ (Even) $\rightarrow \lfloor \sqrt{2} \rfloor = 1$

---

## Constraints

- $1 \le n \le 100$

---
