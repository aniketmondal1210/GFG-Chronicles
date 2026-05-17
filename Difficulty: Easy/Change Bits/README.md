# Change Zero Bits to One

## Problem Statement

Given a number `N`:

### Task 1
Generate a new number by changing all `0`s in the binary representation of `N` into `1`s.

### Task 2
Find the difference between the new number and `N`.

Return:

```text
[difference, newNumber]
```

---

# Examples

### Example 1

```text
Input:
N = 8
```

### Binary Representation

```text
8 = 1000
```

Changing all `0`s to `1`:

```text
1111 = 15
```

Difference:

```text
15 - 8 = 7
```

### Output

```text
[7, 15]
```

---

### Example 2

```text
Input:
N = 6
```

### Binary Representation

```text
6 = 110
```

Changing `0` to `1`:

```text
111 = 7
```

Difference:

```text
7 - 6 = 1
```

### Output

```text
[1, 7]
```

---

## Your Task:
You don't need to read input or print anything. Your task is to complete the function changeBits() which takes an integer N as input parameter and returns a list of two integers containing the difference and the generated number respectively.

## Expected Time Complexity: O(log(N))
## Expected Auxiliary Space: O(1)

## Constraints:

- 0 <= N <= 10^8

---
