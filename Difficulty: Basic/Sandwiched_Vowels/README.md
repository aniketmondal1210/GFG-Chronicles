# Eliminate Sandwiched Vowels

## Problem

Given a string `s` consisting of lowercase English letters, remove every vowel that occurs between two immediately adjacent consonants.

A vowel is considered **sandwiched** if:

```text
previous character is a consonant
current character is a vowel
next character is a consonant
```

The remaining characters should appear in their original order.

---

## Example 1

### Input

```text
s = "bab"
```

### Output

```text
"bb"
```

### Explanation

```text
b a b
  ^
```

`a` is a vowel between two consonants, so it is removed.

---

## Example 2

### Input

```text
s = "ceghij"
```

### Output

```text
"cghj"
```

### Explanation

```text
c e g h i j
  ^     ^
```

- `e` is between `c` and `g`
- `i` is between `h` and `j`

Both are removed.

---

## Constraints:

- 1 ≤ s.size() ≤ 10^6
- 'a' ≤ s[i] ≤ 'z'

---
