# Palindrome Sentence

## Approach

A sentence is a palindrome if:

1. Convert all uppercase letters to lowercase.
2. Remove all non-alphanumeric characters.
3. Check whether the resulting string reads the same forwards and backwards.

A two-pointer approach allows us to do this without creating a new string.

---

# Example 1

## Input

```text
s = "Too hot to hoot"
```

## Processed String

```text
toohottohoot
```

## Output

```text
true
```

---

# Example 2

## Input

```text
s = "Abc 012..## 10cbA"
```

## Processed String

```text
abc01210cba
```

## Output

```text
true
```

---

# Example 3

## Input

```text
s = "ABC $. def01ASDF"
```

## Processed String

```text
abcdef01asdf
```

## Output

```text
false
```

---

## Constraints:

- 1 ≤ s.length() ≤ 10^6

---
