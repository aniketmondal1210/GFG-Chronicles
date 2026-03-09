# Absolute Difference Between Square of Sum and Sum of Squares

## Problem Statement

Given an integer `N`, compute the **absolute difference** between:

1. **Sum of the squares** of the first `N` natural numbers.
2. **Square of the sum** of the first `N` natural numbers.

Return:

```
| (sum of squares) - (square of sum) |
```

---

## Examples

### Example 1

**Input**
```
N = 2
```

**Output**
```
4
```

**Explanation**

Sum of squares:

```
1² + 2² = 1 + 4 = 5
```

Square of sum:

```
(1 + 2)² = 3² = 9
```

Absolute difference:

```
|5 - 9| = 4
```

---

### Example 2

**Input**
```
N = 3
```

**Output**
```
22
```

**Explanation**

Sum of squares:

```
1² + 2² + 3² = 1 + 4 + 9 = 14
```

Square of sum:

```
(1 + 2 + 3)² = 6² = 36
```

Absolute difference:

```
|14 - 36| = 22
```

---

## Expected Time Complexity: O(1)
```
```
## Expected Auxiliary Space: O(1)

## Constraints:

- 1<= N <=103

---
