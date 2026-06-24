# Find First Occurrence of a Character in a String

## Problem

Given a string `s` and a character `ch`, find the **first index** where `ch` appears in the string.

If the character is not present, return:

```text
-1
```

---

## Example 1

### Input

```text
s = "geeksforgeeks"
ch = 'k'
```

### Output

```text
3
```

### Explanation

Occurrences of `'k'`:

```text
geeksforgeeks
   ^
index = 3

and

geeksforgeeks
           ^
index = 11
```

The first occurrence is at index:

```text
3
```

---

## Example 2

### Input

```text
s = "geeksforgeeks"
ch = 'z'
```

### Output

```text
-1
```

### Explanation

The character `'z'` does not occur in the string.

---

## Constraints:

- 1 ≤ |s| ≤ 10^5

---
