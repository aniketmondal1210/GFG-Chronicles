# Reverse and Add Until Palindrome

Given a positive integer `n`, repeatedly reverse its digits and add the reversed number to the current number until:

- The result becomes a palindrome, in which case return that palindrome.
- More than **5 iterations** are required, in which case return `-1`.

## Examples

### Example 1

**Input:**
```text
n = 23
```

**Output:**
```text
55
```

**Explanation:**

```text
23 + reverse(23)
23 + 32 = 55
```

`55` is a palindrome, so the answer is `55`.

### Example 2

**Input:**
```text
n = 73
```

**Output:**
```text
121
```

**Explanation:**

```text
73 + reverse(73) = 73 + 37 = 110
110 + reverse(110) = 110 + 11 = 121
```

`121` is a palindrome, so the answer is `121`.

## Constraint

```text
1 <= n <= 10^4
```
