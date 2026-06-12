# Reverse Alphabet Transformation

## Problem

Given a string `s` consisting only of English alphabets, replace each character with its corresponding character in the reversed English alphabet:

```text
a ↔ z
b ↔ y
c ↔ x
...
z ↔ a
```

For uppercase letters, perform the same transformation while preserving the case.

Return the transformed string.

---

## Examples

### Example 1

**Input**

```text
s = "Hello"
```

**Output**

```text
Svool
```

**Explanation**

```text
H → S
e → v
l → o
l → o
o → l
```

Result:

```text
"Svool"
```

---

### Example 2

**Input**

```text
s = "GfG"
```

**Output**

```text
TuT
```

**Explanation**

```text
G → T
f → u
G → T
```

Result:

```text
"TuT"
```

---

## Constraints:

- 1 <= |s| <= 10^5

---
