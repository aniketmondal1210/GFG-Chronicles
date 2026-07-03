# Replace Every Element with Product of Adjacent Elements

## Problem

Given an array `arr[]`, replace every element with the product of itself and its adjacent elements.

For each index `i`:

- `arr[i] = arr[i-1] * arr[i] * arr[i+1]`
- Assume:
  - The previous element of the first element is `1`.
  - The next element of the last element is `1`.

Return the modified array.

---

## Examples

### Example 1

**Input**

```text
arr = [2, 4, 5]
```

**Output**

```text
[8, 40, 20]
```

**Explanation**

- Index 0: `1 × 2 × 4 = 8`
- Index 1: `2 × 4 × 5 = 40`
- Index 2: `4 × 5 × 1 = 20`

Result:

```text
[8, 40, 20]
```

---

### Example 2

**Input**

```text
arr = [2, 5, 7, 8, 3]
```

**Output**

```text
[10, 70, 280, 168, 24]
```

**Explanation**

- Index 0: `1 × 2 × 5 = 10`
- Index 1: `2 × 5 × 7 = 70`
- Index 2: `5 × 7 × 8 = 280`
- Index 3: `7 × 8 × 3 = 168`
- Index 4: `8 × 3 × 1 = 24`

Result:

```text
[10, 70, 280, 168, 24]
```

---

## Constraints:

- 1 ≤ arr[i] ≤ 10^3
- 1 ≤ arr.size() ≤ 10^5

---
