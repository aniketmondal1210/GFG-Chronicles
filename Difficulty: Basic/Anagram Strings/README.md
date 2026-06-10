# Check if Two Strings are Anagrams

## Problem

Given two strings `S1` and `S2`, return:

- `"1"` if both strings are anagrams.
- `"0"` otherwise.

An anagram contains exactly the same characters with the same frequencies, possibly in a different order.

---

## Examples

### Example 1

**Input**

```text
S1 = "cdbkdub"
S2 = "dsbkcsdn"
```

**Output**

```text
0
```

**Explanation**

The lengths of the strings are different, so they cannot be anagrams.

---

### Example 2

**Input**

```text
S1 = "geeks"
S2 = "skgee"
```

**Output**

```text
1
```

**Explanation**

Both strings contain the same characters with the same frequencies.

---

## Your Task:  
You don't need to read input or print anything. Your task is to complete the function areAnagram() which takes S1 and S2 as input and returns "1" if both strings are anagrams otherwise returns "0".

## Expected Time Complexity: O(n)
## Expected Auxiliary Space: O(K) ,Where K= Contstant

## Constraints:

- 1 <= |S1| <= 1000
- 1 <= |S2| <= 1000

---
