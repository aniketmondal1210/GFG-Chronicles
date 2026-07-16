# Rotate Array Clockwise by `k` Positions

## Problem

Given an array `arr[]` of integers and an integer `k`, rotate the array **clockwise** `k` times.

In one clockwise rotation:

- The **last** element moves to the **front**.
- All other elements shift one position to the **right**.

Return the rotated array.

---

## Examples

### Example 1

**Input**

```text
arr = [1, 2, 3, 4, 5, 6]
k = 2
```

**Output**

```text
[5, 6, 1, 2, 3, 4]
```

**Explanation**

After one rotation:

```text
[6, 1, 2, 3, 4, 5]
```

After the second rotation:

```text
[5, 6, 1, 2, 3, 4]
```

---

### Example 2

**Input**

```text
arr = [1, 2, 3, 4, 5]
k = 4
```

**Output**

```text
[2, 3, 4, 5, 1]
```

**Explanation**

Rotating the array four times clockwise results in:

```text
[2, 3, 4, 5, 1]
```

---

## Constraints:

- 1 ≤ arr.size() ≤ 10^5
- 0 ≤ arr[i] ≤ 10^9
- 0 ≤ k ≤ 10^9

---
