# License Key Formatting

## Problem

Given a string `s` consisting of alphanumeric characters and dashes (`'-'`), and an integer `k`, reformat the string according to the following rules:

1. Remove all dashes.
2. Convert all alphabetic characters to uppercase.
3. Divide the remaining characters into groups of size `k`, starting from the **right**.
4. The **first** group may contain fewer than `k` characters.
5. Join the groups using dashes (`-`).
6. If no characters remain after removing dashes, return an empty string.

Return the formatted string.

---

## Examples

### Example 1

**Input**

```text
s = "5F3Z-2e-9-w"
k = 4
```

**Output**

```text
"5F3Z-2E9W"
```

**Explanation**

After removing dashes and converting to uppercase:

```text
5F3Z2E9W
```

Group from the right into groups of 4:

```text
5F3Z | 2E9W
```

Join with dashes:

```text
5F3Z-2E9W
```

---

### Example 2

**Input**

```text
s = "2-5g-3-J"
k = 2
```

**Output**

```text
"2-5G-3J"
```

**Explanation**

After processing:

```text
25G3J
```

Group from the right:

```text
2 | 5G | 3J
```

Result:

```text
2-5G-3J
```

---

## Constraints:

- 1 ≤ |s| ≤ 10^5
- 1 ≤ k ≤ |s|

---
