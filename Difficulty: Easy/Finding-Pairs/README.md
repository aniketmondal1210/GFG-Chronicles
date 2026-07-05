# Count Character Pairs Present in a String

## Problem

You are given:

- An array `arr[]` of character pairs.
- A string `s`.

For each pair `(a, b)`, count it if **both characters are present** anywhere in the string `s`.

Return the total number of such pairs.

---

## Examples

### Example 1

**Input**

```text
arr = [('A','G'), ('d','i'), ('P','o')]
s = "APiod"
```

**Output**

```text
2
```

**Explanation**

- `(A, G)` ❌ (`G` is missing)
- `(d, i)` ✅
- `(P, o)` ✅

Hence, the answer is **2**.

---

### Example 2

**Input**

```text
arr = [('r','e')]
s = "ghe"
```

**Output**

```text
0
```

**Explanation**

The character `r` is not present in the string.

---

## Expected Time Complexity: O(n), n is the size of arr.
## Expected Auxiliary Space: O(1).

## Constraints:

- 1<=s.size()<=10^6
- 1<=arr.size()<=10^6
- The string s and the characters in each pair are either lowercase or uppercase alphabets.

---
