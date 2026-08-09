# Find Perfect Cubes in a Range

## Problem Statement

Given two integers `a` and `b` where:

```text
1 ≤ a ≤ b
```

find all the **perfect cubes** between `a` and `b`, inclusive.

A perfect cube is a number that can be expressed as:

```text
n × n × n
```

for some positive integer `n`.

If there is no perfect cube in the given range, return `-1`.

---

## Examples

### Example 1

**Input**

```text
a = 1
b = 100
```

**Output**

```text
[1, 8, 27, 64]
```

**Explanation**

The perfect cubes between `1` and `100` are:

```text
1³ = 1
2³ = 8
3³ = 27
4³ = 64
```

Therefore:

```text
[1, 8, 27, 64]
```

---

### Example 2

**Input**

```text
a = 24
b = 576
```

**Output**

```text
[27, 64, 125, 216, 343, 512]
```

**Explanation**

The perfect cubes in the given range are:

```text
3³ = 27
4³ = 64
5³ = 125
6³ = 216
7³ = 343
8³ = 512
```

---

### Example 3

**Input**

```text
a = 2
b = 7
```

**Output**

```text
-1
```

**Explanation**

There is no perfect cube between `2` and `7`.

---

## Constraints:

- 1 ≤ a ≤ b ≤ 10^4

---
