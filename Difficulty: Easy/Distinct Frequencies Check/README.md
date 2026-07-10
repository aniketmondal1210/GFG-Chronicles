# Check if Array Frequencies are Unique

## Problem

Given an array `arr[]` of integers, determine whether the frequency of every distinct element is unique.

Return:

- `true` if all frequencies are unique.
- `false` if any two distinct elements have the same frequency.

---

## Examples

### Example 1

**Input**

```text
arr = [1, 1, 2, 5, 5]
```

**Output**

```text
false
```

**Explanation**

Frequencies are:

```text
1  -> 2
2  -> 1
5  -> 2
```

Both `1` and `5` occur `2` times, so the frequencies are not unique.

---

### Example 2

**Input**

```text
arr = [2, 2, 5, 10, 1, 2, 10, 5, 10, 2]
```

**Output**

```text
true
```

**Explanation**

Frequencies are:

```text
1  -> 1
2  -> 4
5  -> 2
10 -> 3
```

All frequencies are distinct.

---

### Example 3

**Input**

```text
arr = [1, 1, 1]
```

**Output**

```text
true
```

**Explanation**

There is only one distinct element, so its frequency is unique.

---

## Constraints:
- 1 ≤ arr.size() ≤ 10^5
- -10^9 ≤ arr[i] ≤ 10^9
