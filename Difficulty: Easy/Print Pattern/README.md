# Recursive Number Pattern

## Problem Statement

Given a number **n**, print a sequence:

1. Start from **n**
2. Decrease the number by **5 recursively**
3. Continue until the value becomes **≤ 0**
4. Then **increase by 5 recursively**
5. Stop when the sequence returns to the **original number n**

⚠️ **Loops are not allowed. Only recursion must be used.**

---

# Examples

### Example 1

**Input**
```
n = -16
```

**Output**
```
[-16]
```

**Explanation**

Since **n ≤ 0**, the sequence contains only **n**.

---

### Example 2

**Input**
```
n = 10
```

**Output**
```
[10, 5, 0, 5, 10]
```

**Explanation**

```
10 → 5 → 0  (decreasing by 5)
0 → 5 → 10  (increasing by 5)
```

---

## Constraints:

- -10^5 ≤ n ≤ 10^5

---
