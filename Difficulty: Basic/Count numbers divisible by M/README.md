# Count Numbers Divisible by M in a Range

## Problem Statement

Given three integers:

- `A` and `B` defining a range `[A, B]` (inclusive)
- `M` as the divisor  

Find the **count of numbers divisible by M** within the range `[A, B]`.

## Examples

### Example 1

**Input**
```
A = 6, B = 15, M = 3
```

**Output**
```
4
```

**Explanation**
Multiples of 3 in range:
```
6, 9, 12, 15
```
Total = 4

---

### Example 2

**Input**
```
A = 25, B = 100, M = 30
```

**Output**
```
3
```

**Explanation**
Multiples of 30 in range:
```
30, 60, 90
```
Total = 3

---

## Constraint:

```
1 <= A, B, M <= 10^6
```

Expected Time Complexity: `O(1)`  
Expected Auxiliary Space: `O(1)`

---
