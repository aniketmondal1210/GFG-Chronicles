# Maximum and Minimum Number by Replacing 5 and 6

## Problem

Given a positive integer `n`, you may perform the following operation any number of times:

- Change any digit `5` to `6`.
- Change any digit `6` to `5`.

Find:

- The **maximum** number possible.
- The **minimum** number possible.

Return the **sum** of these two numbers.

---

## Examples

### Example 1

**Input**

```text
n = 35
```

**Output**

```text
71
```

**Explanation**

```text
Original : 35

Maximum:
35 → 36

Minimum:
35

Answer:
36 + 35 = 71
```

---

### Example 2

**Input**

```text
n = 22
```

**Output**

```text
44
```

**Explanation**

```text
No digit is 5 or 6.

Maximum = 22
Minimum = 22

Answer = 22 + 22 = 44
```

---

## Constraints:

- 1 ≤ n ≤ 10^9

---
