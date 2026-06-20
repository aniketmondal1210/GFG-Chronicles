# Last Digit of a^b

## Problem

Given two non-negative integers `a` and `b` as strings, find the **last digit** of:

```text
a^b
```

Since `a` and `b` can be very large (up to 1000 digits), direct computation is not possible.

---

## Example 1

### Input

```text
a = "3"
b = "10"
```

### Output

```text
9
```

### Explanation

```text
3^10 = 59049
```

Last digit:

```text
9
```

---

## Example 2

### Input

```text
a = "6"
b = "2"
```

### Output

```text
6
```

### Explanation

```text
6^2 = 36
```

Last digit:

```text
6
```

---

## Constraints:

- 1 ≤ a.size(), b.size() ≤ 1000
- a and b consist only of numeric digits ('0' - '9')
- a and b do not contain any leading zeros, except when number itself is "0"

---
