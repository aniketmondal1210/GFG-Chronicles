# Substring After Nth Occurrence of a Character

## Problem Statement

Given:
- A string `s` (without spaces)
- A character `ch`
- An integer `count`

Return the substring that remains **after the `count`th occurrence** of character `ch`.

### Important Notes:
- Uppercase and lowercase letters are different.
- Return `""` (empty string) if:
  - `ch` does not appear `count` times
  - The remaining substring is empty

---

## Example 1

**Input:**

s = "Thisisdemostring"
ch = 'i'
count = 3


**Output:**

ng


---

## Example 2

**Input:**

s = "Thisisdemostri"
ch = 'i'
count = 3


**Output:**

""


---

## Example 3

**Input:**

s = "abcd"
ch = 'x'
count = 2


**Output:**

""


---

## Constraints

- 1 ≤ s.length ≤ 10^5
- 1 ≤ count ≤ s.length


---

## Time Complexity

O(n)


## Auxiliary Space

O(1)


---
