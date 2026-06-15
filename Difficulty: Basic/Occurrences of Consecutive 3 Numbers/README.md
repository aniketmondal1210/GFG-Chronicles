# Count Distinct Special Integers

## Problem

Given an integer array `arr` of length `n`, count the number of **distinct special integers**.

An integer `x` is called **special** if all three values are present in the array:

```text
x - 1
x
x + 1
```

Only distinct special integers should be counted.

---

## Example 1

### Input

```text
n = 5
arr = {1, 2, 3, 3, 4}
```

### Output

```text
2
```

### Explanation

Distinct elements:

```text
{1, 2, 3, 4}
```

- 2 is special because 1, 2, 3 exist.
- 3 is special because 2, 3, 4 exist.

Answer:

```text
2
```

---

## Example 2

### Input

```text
n = 4
arr = {2, 3, 5, 7}
```

### Output

```text
0
```

### Explanation

No element has both its predecessor and successor present.

---

## Your Task: 
You have to complete the function specialIntegers() which takes integer n and an array arr of length n as input, and return the number of distinct special integers in the arr.

## Constraints:

- 1 <= n <= 10^5
- -10^9 <= arr[i] <= 10^9

---
