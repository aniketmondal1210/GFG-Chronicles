# Problem: Evaluate Polynomial

## Problem Statement

Given an integer array `poly[]` representing the coefficients of a polynomial in decreasing order of powers of `x`, and an integer `x`, evaluate the polynomial at `x` and return its value.

The polynomial represented by:

```text
poly[] = {a0, a1, a2, ..., an}
```

is:

```text
a0*x^n + a1*x^(n-1) + ... + a(n-1)*x + an
```

---

## Example 1

**Input:**

```text
poly = {2, -6, 2, -1}
x = 3
```

**Output:**

```text
5
```

**Explanation:**

The polynomial is:

```text
2x^3 - 6x^2 + 2x - 1
```

Evaluating it at `x = 3`:

```text
2(3^3) - 6(3^2) + 2(3) - 1
= 54 - 54 + 6 - 1
= 5
```

---

## Example 2

**Input:**

```text
poly = {1, 2, 0, 4}
x = 2
```

**Output:**

```text
20
```

**Explanation:**

The polynomial is:

```text
x^3 + 2x^2 + 4
```

Evaluating it at `x = 2`:

```text
2^3 + 2(2^2) + 4
= 8 + 8 + 4
= 20
```

---

## Approach

Use **Horner's Method** to evaluate the polynomial efficiently.

Start with the first coefficient and repeatedly update the result using:

```text
result = result * x + poly[i]
```

For example, for:

```text
2x^3 - 6x^2 + 2x - 1
```

the calculation becomes:

```text
((2 * x - 6) * x + 2) * x - 1
```

This avoids explicitly calculating powers of `x`.

---

## Complexity

### Time Complexity

```text
O(n)
```

where `n` is the number of coefficients.

### Auxiliary Space

```text
O(1)
```

Only a constant amount of extra space is required.

---

## Constraints

```text
1 <= poly.size() <= 8
-100 <= poly[i] <= 100
1 <= x <= 5
```
