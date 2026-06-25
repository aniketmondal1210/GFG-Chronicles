# Find the Extra Character

## Problem

Given two strings:

- `s1` of length `n`
- `s2` of length `n + 1`

`s2` contains all characters of `s1` plus **one extra character**.

Return the extra character.

---

## Example 1

### Input

```text
s1 = "abcd"
s2 = "badce"
```

### Output

```text
e
```

### Explanation

Characters of `s1`:

```text
a, b, c, d
```

Characters of `s2`:

```text
a, b, c, d, e
```

Extra character:

```text
e
```

---

## Example 2

### Input

```text
s1 = "efg"
s2 = "gtfe"
```

### Output

```text
t
```

### Explanation

`s2` contains all characters of `s1` and one additional character:

```text
t
```

---

## Constraints:

- 1 ≤ s.size() ≤ 10 
- The string s contains only lowercase english letters (a-z).

---
