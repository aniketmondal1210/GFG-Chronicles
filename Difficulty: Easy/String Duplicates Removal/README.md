# Remove Duplicate Characters (Preserving Order)

## Problem Statement

Given a string `s`, remove all duplicate characters while keeping only their **first occurrence**.

The relative order of characters must remain the same.

**Note:** Uppercase and lowercase letters are treated as different characters.

---

# Example 1

## Input

```text
s = "geEksforGEeks"
```

## Process

```text
g -> keep
e -> keep
E -> keep
k -> keep
s -> keep
f -> keep
o -> keep
r -> keep
G -> keep

E, e, k, s -> already seen
```

## Output

```text
"geEksforG"
```

---

# Example 2

## Input

```text
s = "HaPpyNewYear"
```

## Output

```text
"HaPpyNewYr"
```

---

## Constraints:

- 1 ≤ N ≤ 10^6
- String contains uppercase and lowercase english letters.

---
