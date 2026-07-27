# Convert String to Alternating Lowercase and Uppercase

## Problem

Given a string `s`, convert it into an alternating sequence of lowercase and uppercase characters while keeping the character at index `0` unchanged.

Rules:

- If the first character is **lowercase**:
  - Characters at **even indices** should be lowercase.
  - Characters at **odd indices** should be uppercase.
- If the first character is **uppercase**:
  - Characters at **even indices** should be uppercase.
  - Characters at **odd indices** should be lowercase.

Return the modified string.

---

## Examples

### Example 1

**Input**

```text
s = "geeksforgeeks"
```

**Output**

```text
gEeKsFoRgEeKs
```

**Explanation**

The first character is lowercase.

```text
Even indices  -> lowercase
Odd indices   -> uppercase
```

Result:

```text
g E e K s F o R g E e K s
```

---

### Example 2

**Input**

```text
s = "Geeksforgeeks"
```

**Output**

```text
GeEkSfOrGeEkS
```

**Explanation**

The first character is uppercase.

```text
Even indices  -> uppercase
Odd indices   -> lowercase
```

---

## Constraints:

- 1 ≤ |s| ≤ 10^5

---
