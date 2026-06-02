# Equilibrium Index in an Array

## Problem Statement

Find the first index such that:

```text
Sum of elements before it
=
Sum of elements after it
```

Return `-1` if no such index exists.

---

# Example 1

## Input

```text
arr = [1,3,5,2,2]
```

## Explanation

At index `2`:

```text
Left Sum  = 1 + 3 = 4
Right Sum = 2 + 2 = 4
```

Hence,

```text
Output = 2
```

---

# Example 2

## Input

```text
arr = [1]
```

## Explanation

```text
Left Sum  = 0
Right Sum = 0
```

Hence,

```text
Output = 0
```

---

# Example 3

## Input

```text
arr = [5,4,3,2,1]
```

## Output

```text
-1
```

---

## Constraints:

- 1 ≤ arr.size() ≤ 10^6
- 0 ≤ arr[i] ≤ 10^6

---
