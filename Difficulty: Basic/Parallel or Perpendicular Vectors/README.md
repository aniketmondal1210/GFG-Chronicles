# Check Whether Two 3D Vectors are Parallel or Perpendicular

## Problem Statement

You are given six integers:

- `a1, a2, a3` representing vector

```text
A = (a1, a2, a3)
```

- `b1, b2, b3` representing vector

```text
B = (b1, b2, b3)
```

Determine the relationship between the two vectors:

- Return **1** if the vectors are **parallel**.
- Return **2** if the vectors are **perpendicular**.
- Return **0** otherwise.

### Note

If either vector is the **zero vector**, return **0**, since a zero vector is both parallel and perpendicular to every vector.

---

## Mathematical Formulas

### Dot Product

```text
A · B = a1*b1 + a2*b2 + a3*b3
```

If

```text
A · B = 0
```

then the vectors are **perpendicular**.

---

### Cross Product

```text
A × B =
(a2*b3 - a3*b2,
 a3*b1 - a1*b3,
 a1*b2 - a2*b1)
```

If

```text
|A × B|² = 0
```

then the vectors are **parallel**.

---

## Examples

### Example 1

**Input**

```text
a1 = 3, a2 = 2, a3 = 1
b1 = 6, b2 = 4, b3 = 2
```

**Output**

```text
1
```

**Explanation**

```text
B = 2 × A

Cross product = (0,0,0)

Hence, vectors are parallel.
```

---

### Example 2

**Input**

```text
a1 = 4, a2 = 6, a3 = 1
b1 = 1, b2 = -1, b3 = 2
```

**Output**

```text
2
```

**Explanation**

```text
Dot Product

= 4×1 + 6×(-1) + 1×2
= 4 - 6 + 2
= 0

Hence, vectors are perpendicular.
```

---

## Constraints:

- -100 ≤ a1, a2, a3, b1, b2, b3 ≤ 100

---
