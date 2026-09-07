# Equal Character Frequencies in Two Halves

## Problem

Given a string `s`, split it into two halves from the middle.

If the length of `s` is odd, ignore the middle character before splitting.

Return `true` if both halves contain the same frequency of every character. Otherwise, return `false`.

---

## Examples

### Example 1

**Input:**
```text
s = "abcdbca"
```

**Output:**
```text
true
```

**Explanation:**

The string has length `7`, which is odd. Therefore, we ignore the middle character `'d'`.

The two halves are:

```text
First Half  = "abc"
Second Half = "bca"
```

Both halves contain the same frequency of `'a'`, `'b'`, and `'c'`, so the answer is `true`.

---

### Example 2

**Input:**
```text
s = "abbaab"
```

**Output:**
```text
false
```

**Explanation:**

The two halves are:

```text
First Half  = "abb"
Second Half = "aab"
```

The character frequencies are not the same in both halves, so the answer is `false`.

---

## Constraints

- `1 <= |s| <= 10^5`

---

## Function Signature

```text
boolean sameFrequency(String s)
```

---

## Topics

- Strings
- Hashing
- Frequency Counting
