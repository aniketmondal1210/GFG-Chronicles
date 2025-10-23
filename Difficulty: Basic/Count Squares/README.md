# Count of Perfect Squares Less Than n

## Problem Statement
Given a positive integer `n`, find the **number of perfect squares** that are **less than** `n`.

The sample space of perfect squares starts from `1`:

1, 4, 9, 16, 25, ...


---

## Input
- A single integer `n`.

**Constraints:**

1 ≤ n ≤ 10⁸


---

## Output
Return the count of perfect squares that are strictly less than `n`.

---

## Explanation
If we list all perfect squares less than `n`, they are:

1², 2², 3², ..., k² < n

The largest integer `k` satisfying `k² < n` is:

k = floor(sqrt(n - 1))

Hence, the number of perfect squares less than `n` is **k**.

---

## Examples

### Example 1
**Input:**

n = 9


**Output:**

2


**Explanation:**
Perfect squares less than 9 → `1, 4`  
Count = 2.

---

### Example 2
**Input:**

n = 3


**Output:**

1


**Explanation:**
Perfect squares less than 3 → `1`  
Count = 1.

---
