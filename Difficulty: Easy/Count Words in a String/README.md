# Count Words in a String

## Problem

Given a string `s` consisting of:

- Lowercase English letters (`a-z`)
- Spaces (`' '`)
- Tab characters (`'\t'`)
- Newline characters (`'\n'`)

Count the total number of **words** in the string.

A **word** is defined as a continuous sequence of lowercase English letters. Spaces, tabs, and newlines act as separators.

---

## Examples

### Example 1

**Input**

```text
s = "abc def"
```

**Output**

```text
2
```

**Explanation**

The space separates the string into two words:

```text
"abc" and "def"
```

---

### Example 2

**Input**

```text
s = "a\nyo\t"
```

**Output**

```text
2
```

**Explanation**

The newline (`\n`) and tab (`\t`) act as separators.

The words are:

```text
"a"
"yo"
```

---

## Constraints:

2 <= Length of String <= 10^6

---
