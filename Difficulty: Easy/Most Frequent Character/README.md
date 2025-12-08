# Maximum Occurring Character in a String

Given a string **s** of lowercase alphabets, the task is to find the **maximum occurring character** in the string.

If multiple characters occur the maximum number of times, return the **lexicographically smallest** one.

---

## Examples

### Example 1

Input: s = "testsample"

Output: 'e'

Explanation:

The frequencies are:

t → 2

e → 2

s → 2

a → 1

m → 1

p → 1

l → 1

Characters 't', 'e', and 's' have the same highest frequency (2).

The lexicographically smallest among them is 'e'.


### Example 2

Input: s = "output"

Output: 't'

Explanation:

The characters 't' and 'u' both appear twice.

t is lexicographically smaller than u.

### Constraints

- 1 ≤ |s| ≤ 100
- s contains only lowercase English letters

---
