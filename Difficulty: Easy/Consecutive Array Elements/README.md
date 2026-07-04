# Check if Array Contains Consecutive Distinct Numbers

## Problem

Given an **unsorted array** `arr` of positive integers, determine whether it contains **consecutive distinct numbers**.

The array is considered consecutive if:

- Every number appears **exactly once**.
- The elements include **every integer** from the minimum value to the maximum value.

Return `true` if the array satisfies these conditions; otherwise, return `false`.

---

## Examples

### Example 1

**Input**

```text
arr = [5, 4, 2, 1, 3]
```

**Output**

```text
true
```

**Explanation**

After sorting, the array becomes:

```text
[1, 2, 3, 4, 5]
```

All numbers from 1 to 5 are present exactly once.

---

### Example 2

**Input**

```text
arr = [2, 1, 4]
```

**Output**

```text
false
```

**Explanation**

The number `3` is missing, so the elements are not consecutive.

---

## Constraints:

- 1 ≤ arr.size() ≤ 10^6
- 1 ≤ arr[i] ≤ 10^6

---
