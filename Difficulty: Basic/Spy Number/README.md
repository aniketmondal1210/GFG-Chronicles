# Spy Number

## Problem Statement

A number is called a **Spy Number** if:

```text
Sum of digits == Product of digits
```

Return:

- `true` → if the number is a Spy number
- `false` → otherwise

---

# Examples

### Example 1

```text
Input:
n = 1412

Output:
true
```

### Explanation

```text
Sum = 1 + 4 + 1 + 2 = 8

Product = 1 × 4 × 1 × 2 = 8

Since sum == product,
1412 is a Spy Number.
```

---

### Example 2

```text
Input:
n = 13

Output:
false
```

### Explanation

```text
Sum = 1 + 3 = 4

Product = 1 × 3 = 3

Since sum != product,
13 is not a Spy Number.
```

---

## Constraints:

- 1 ≤ n ≤ 10^9

---
