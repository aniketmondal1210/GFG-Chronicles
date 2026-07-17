# Find the Shortest and Longest Word in a String

## Problem

Given a string `s` containing uppercase and lowercase English letters, where words are separated by spaces, find:

- The **minimum length** word.
- The **maximum length** word.

### Rules

- If multiple words have the **minimum** length, return the **first** one.
- If multiple words have the **maximum** length, return the **last** one.

Return both words.

---

## Examples

### Example 1

**Input**

```text
s = "Hi from Gfg"
```

**Output**

```text
["Hi", "from"]
```

**Explanation**

- Word lengths:
  - Hi → 2
  - from → 4
  - Gfg → 3

Shortest word is `"Hi"`.

Longest word is `"from"`.

---

### Example 2

**Input**

```text
s = "water WATER evEry WHere BUT nor a Drop to Drink"
```

**Output**

```text
["a", "Drink"]
```

**Explanation**

- Shortest word is `"a"` (length 1).
- Longest words have length 5:
  - water
  - WATER
  - evEry
  - WHere
  - Drink

Among them, return the **last** one, which is `"Drink"`.

---

## Constraints:

- 1 <= s.size() <= 10^5

---
