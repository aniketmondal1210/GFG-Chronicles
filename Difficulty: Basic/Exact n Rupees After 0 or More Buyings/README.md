# Geek and Chocolates

## Problem

Given an integer `n`, determine whether Geek can have **exactly `n` rupees** after buying **0 or more chocolates** from a shop.

- Geek initially has **100 rupees**.
- The shop sells two types of chocolates costing **3** rupees and **7** rupees.
- Geek can buy any number of chocolates, including zero chocolates.

Return `true` if it is possible to have exactly `n` rupees remaining; otherwise, return `false`.

### Example 1

**Input:**
```text
n = 99
```

**Output:**
```text
false
```

**Explanation:**

Geek starts with 100 rupees, so he needs to spend:

```text
100 - 99 = 1
```

No combination of chocolates costing 3 and 7 rupees can total 1 rupee. Therefore, the answer is `false`.

### Example 2

**Input:**
```text
n = 97
```

**Output:**
```text
true
```

**Explanation:**

Geek needs to spend:

```text
100 - 97 = 3
```

He can buy one chocolate costing 3 rupees, leaving exactly 97 rupees.

---

## Constraints:

- 0 ≤ n ≤ 100
