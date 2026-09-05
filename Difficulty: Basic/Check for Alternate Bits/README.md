# Alternating Bits

## Problem

Given a non-negative integer `n`, check whether its binary representation consists of alternating bits.

A binary representation has alternating bits if no two adjacent bits are the same.

---

## Examples

### Example 1

**Input:**
```text
n = 12
```

**Output:**
```text
false
```

**Explanation:**

```text
12 = "1100"
```

The binary representation contains consecutive `1`s and consecutive `0`s, so it does not have an alternating pattern.

---

### Example 2

**Input:**
```text
n = 10
```

**Output:**
```text
true
```

**Explanation:**

```text
10 = "1010"
```

The bits alternate between `1` and `0`, so the answer is `true`.

---

## Constraints

- `0 <= n <= 10^9`

---

## Function Signature

```text
boolean hasAlternatingBits(int n)
```

---

## Topics

- Bit Manipulation
- Binary Representation
- Mathematics
