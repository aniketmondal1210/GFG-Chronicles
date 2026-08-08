# Sum of Elements in All Subsets

## Problem Statement

Given an integer `n`, find the sum of all elements from all possible **non-empty subsets** of the set containing the first `n` natural numbers:

```text
{1, 2, 3, ..., n}
```

---

## Examples

### Example 1

**Input**

```text
n = 2
```

The non-empty subsets are:

```text
[1]
[2]
[1,2]
```

Sum of all elements:

```text
1 + 2 + 1 + 2 = 6
```

**Output**

```text
6
```

---

### Example 2

**Input**

```text
n = 3
```

The non-empty subsets are:

```text
[1]
[2]
[3]
[1,2]
[1,3]
[2,3]
[1,2,3]
```

Sum:

```text
1 + 2 + 3
+ (1 + 2)
+ (1 + 3)
+ (2 + 3)
+ (1 + 2 + 3)
= 24
```

**Output**

```text
24
```

---
