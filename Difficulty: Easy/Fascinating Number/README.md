# Fascinating Number

## Problem Statement

Given a number `n`, check whether it is fascinating or not.

A number with **3 or more digits** is considered fascinating if, when it is multiplied by `2` and `3`, and the resulting products are concatenated with the original number, the final sequence contains all the digits from `1` to `9` exactly once.

In other words, construct the concatenation of:

```text
n
n * 2
n * 3
```

and check whether the resulting sequence contains every digit from `1` to `9` exactly once.

---

## Example 1

**Input:**

```text
n = 192
```

**Output:**

```text
true
```

**Explanation:**

```text
192 * 2 = 384
192 * 3 = 576
```

Concatenating the original number and the two products:

```text
192384576
```

This contains all digits from `1` to `9` exactly once.

Therefore:

```text
true
```

---

## Example 2

**Input:**

```text
n = 853
```

**Output:**

```text
false
```

**Explanation:**

The resulting concatenated number does not contain all digits from `1` to `9` exactly once.

Therefore, `853` is not a fascinating number.

---

## Constraints

```text
100 <= n <= 2 * 10^9
```
