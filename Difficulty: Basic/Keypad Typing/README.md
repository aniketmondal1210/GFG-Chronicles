# Problem: Convert String to Keypad Numbers

## Problem Statement

Given a string `s` consisting of lowercase English letters, each letter corresponds to a number on a standard keypad.

Replace every character in `s` with its corresponding keypad number and return the resulting numeric string.

The keypad mapping is:

```text
2 -> abc
3 -> def
4 -> ghi
5 -> jkl
6 -> mno
7 -> pqrs
8 -> tuv
9 -> wxyz
```

---

## Example 1

**Input:**

```text
s = "geeksforgeeks"
```

**Output:**

```text
4335736743357
```

**Explanation:**

Each character is converted to its corresponding keypad digit and the digits are concatenated in order.

```text
g -> 4
e -> 3
e -> 3
k -> 5
s -> 7
f -> 3
o -> 6
r -> 7
g -> 4
e -> 3
e -> 3
k -> 5
s -> 7
```

Therefore:

```text
4335736743357
```

---

## Example 2

**Input:**

```text
s = "geeksquiz"
```

**Output:**

```text
433577849
```

**Explanation:**

```text
g -> 4
e -> 3
e -> 3
k -> 5
s -> 7
q -> 7
u -> 8
i -> 4
z -> 9
```

Therefore:

```text
433577849
```

---

## Constraints:

- 1 ≤ s.size() ≤ 100

---
