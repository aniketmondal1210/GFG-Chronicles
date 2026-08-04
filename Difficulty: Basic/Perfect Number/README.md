# Check if a Number is a Perfect Number (Sum of Factorials of Digits)

## Problem Statement

Given an integer `N`, determine whether it is a **perfect number**.

A number is considered **perfect** if the sum of the factorials of its digits is equal to the number itself.

Return:

- `1` if `N` is perfect.
- `0` otherwise.

---

## Examples

### Example 1

**Input**

```text
N = 23
```

**Output**

```text
0
```

**Explanation**

```text
2! + 3!
= 2 + 6
= 8

8 ≠ 23
```

Hence, the answer is **0**.

---

### Example 2

**Input**

```text
N = 145
```

**Output**

```text
1
```

**Explanation**

```text
1! + 4! + 5!
= 1 + 24 + 120
= 145
```

Since the sum equals the original number, the answer is **1**.

---

## Your Task:
You don't need to read input or print anything.Your task is to complete the function isPerfect() which takes a number N as input parameter and returns 1 if N is perfect.Otherwise, it returns 0.


## Expected Time Complexity: O(Log10N)
## Expected Auxillary Space: O(constant)


## Constraints:

- 1 <= N <= 10^9

---
