# String Comparison Based on Priority

## Problem
You are given two strings `s1` and `s2`.  
Compare them lexicographically (dictionary order):

- Return **0** if both strings are equal.
- Return **1** if `s1` is greater than `s2`.
- Return **-1** if `s1` is lesser than `s2`.

---

## Constraints
- `1 ≤ |s1|, |s2| ≤ 10^3`
- Strings contain only lowercase English alphabets.

---

## Examples

### Example 1
**Input**

s1 = "adding", s2 = "addio"

**Output**

-1

**Explanation**  
At index 3, `n` vs `o`:  
Since `'n' < 'o'`, string1 < string2. Return -1.

---

### Example 2
**Input**

s1 = "abcno", s2 = "abcng"

**Output**

1

**Explanation**  
At index 4, `o` vs `g`:  
Since `'o' > 'g'`, string1 > string2. Return 1.

---
