# Check if Combined String in Linked List is a Palindrome

## Problem

You are given the head of a linked list where each node contains a **string**.

Concatenate the strings from all the nodes in order to form a single string.

Return:

- `true` if the combined string is a palindrome.
- `false` otherwise.

A palindrome is a string that reads the same forwards and backwards.

---

## Examples

### Example 1

**Input**

```text
Linked List:
"abc" -> "dd" -> "cba"
```

**Output**

```text
true
```

**Explanation**

The combined string is:

```text
"abcddcba"
```

Since it reads the same forwards and backwards, it is a palindrome.

---

### Example 2

**Input**

```text
Linked List:
"abc" -> "d" -> "ba"
```

**Output**

```text
false
```

**Explanation**

The combined string is:

```text
"abcdba"
```

It is not a palindrome.

---

## Constraints:

- 1 ≤ Node.data.length ≤ 10^3
- 1 ≤ list.length ≤ 10^3

---
