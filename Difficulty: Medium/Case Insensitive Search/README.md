# Case Insensitive Pattern Search

## Approach

Convert both strings to the same case (lowercase) and then check every possible starting position in `txt`.

If the substring of length `m` matches the pattern, store the index.

---

# Example 1

### Input

```text
txt = "aBcAb"
pat = "aB"
```

### After Lowercase Conversion

```text
txt = "abcab"
pat = "ab"
```

### Matches

```text
Index 0 -> "ab"
Index 3 -> "ab"
```

### Output

```text
[0, 3]
```

---

# Example 2

### Input

```text
txt = "aAAa"
pat = "Aa"
```

### After Lowercase Conversion

```text
txt = "aaaa"
pat = "aa"
```

### Matches

```text
Index 0
Index 1
Index 2
```

### Output

```text
[0, 1, 2]
```

---

## Constraints:

- 1 ≤ txt.size() ≤ 10^5
- 1 ≤ pat.size() < txt.size()
- Both the strings consist of uppercase or lowercase English alphabets.

---
