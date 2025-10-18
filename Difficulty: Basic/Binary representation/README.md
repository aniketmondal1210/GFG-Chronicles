# 32-Bit Binary Representation

## Problem Statement

You are given an integer `n`, and you need to return its **binary representation** as a string containing exactly **32 bits**.

---

## Input

* A single integer `n`.

**Constraints:**

```
1 ≤ n ≤ 10⁹
```

---

## Output

* A string representing the 32-bit binary representation of `n`.

---

## Explanation

Convert `n` to binary and pad it with leading zeros to make it 32 bits long.

Example:
If `n = 2`, binary is `10`, and as 32 bits → `00000000000000000000000000000010`.

---

## Examples

### Example 1

**Input:**

```
2
```

**Output:**

```
00000000000000000000000000000010
```

### Example 2

**Input:**

```
5
```

**Output:**

```
00000000000000000000000000000101
```

---
