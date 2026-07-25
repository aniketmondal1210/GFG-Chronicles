# Check if Unique Elements Form Contiguous Integers

## Problem

Given an array `arr[]`, determine whether all the **unique elements** form a contiguous sequence of integers.

A set of integers is contiguous if it contains every integer between its minimum and maximum values exactly once.

Return:

- `"Yes"` if the unique elements are contiguous.
- `"No"` otherwise.

---

## Examples

### Example 1

**Input**

```text
arr = [5, 2, 3, 6, 4, 4, 6, 6]
```

**Output**

```text
Yes
```

**Explanation**

Unique elements are:

```text
{2, 3, 4, 5, 6}
```

They form the contiguous sequence:

```text
2, 3, 4, 5, 6
```

---

### Example 2

**Input**

```text
arr = [10, 14, 10, 12, 12, 13, 15]
```

**Output**

```text
No
```

**Explanation**

Unique elements are:

```text
{10, 12, 13, 14, 15}
```

The number `11` is missing, so they are **not** contiguous.

---

## Expected Time Complexity: O(nlog(n)).
## Expected Auxiliary Space: O(n).

## Constraints:

- 1 ≤ arr.size() ≤ 10^5
- 1 ≤ arr[i] ≤ 10^5

---
