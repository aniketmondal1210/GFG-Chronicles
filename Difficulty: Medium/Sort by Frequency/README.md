# Sort Characters by Frequency (Ascending)

## Problem

Given a string `s`, arrange its characters according to the **frequency** of each character in **ascending order**.

If two characters have the same frequency, arrange them in **lexicographical order**.

Return the resulting string.

---

## Examples

### Example 1

**Input**

```text
s = "geeksforgeeks"
```

**Output**

```text
forggkksseeee
```

**Explanation**

Character frequencies are:

```text
f -> 1
o -> 1
r -> 1
g -> 2
k -> 2
s -> 2
e -> 4
```

Characters are ordered by increasing frequency. Characters with the same frequency are arranged lexicographically.

---

### Example 2

**Input**

```text
s = "abc"
```

**Output**

```text
abc
```

**Explanation**

Each character appears exactly once, so they are arranged in lexicographical order.

---

## Constraints :

- 1 ≤ s.length() ≤ 10^6
- s consist of lowercase english alphabets.

---
