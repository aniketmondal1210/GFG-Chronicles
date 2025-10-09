# String Pattern Problem

## Problem Statement

Given a string `s`, print a pattern where each line removes one character from the end of the string until only one character remains.

---

## Input

A single string `s`.

**Constraints:**

```
1 ≤ |s| ≤ 10^3
```

---

## Output

Print the pattern by reducing one character from the end of the string in each line.

---

## Examples

### Example 1

**Input:**

```
s = "GeeK"
```

**Output:**

```
Geek
Gee
Ge
G
```

**Explanation:** The string length decreases by one in each line.

---

### Example 2

**Input:**

```
s = "G*g"
```

**Output:**

```
G*g
G*
G
```

**Explanation:** One character is removed from the end after each line.

---
