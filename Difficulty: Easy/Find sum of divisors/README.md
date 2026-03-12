# Sum of Divisors of All Divisors

## Problem Statement

Given a natural number **N**, find the **sum of the divisors of all the divisors of N**.

Steps involved:
1. Find all **divisors of N**.
2. For each divisor `d`, compute the **sum of its divisors**.
3. Return the **total sum**.

---

## Examples

### Example 1

**Input**
```
N = 54
```

**Output**
```
232
```

**Explanation**

Divisors of `54`:

```
1, 2, 3, 6, 9, 18, 27, 54
```

Sum of divisors of each:

```
1  → 1
2  → 1+2 = 3
3  → 1+3 = 4
6  → 1+2+3+6 = 12
9  → 1+3+9 = 13
18 → 1+2+3+6+9+18 = 39
27 → 1+3+9+27 = 40
54 → 1+2+3+6+9+18+27+54 = 120
```

Total:

```
1 + 3 + 4 + 12 + 13 + 39 + 40 + 120 = 232
```

---

### Example 2

**Input**
```
N = 10
```

**Output**
```
28
```

**Explanation**

Divisors of `10`:

```
1, 2, 5, 10
```

Sum of divisors:

```
1  → 1
2  → 3
5  → 6
10 → 18
```

Total:

```
1 + 3 + 6 + 18 = 28
```

---

## Expected Time Complexity: O(NloglogN)
## Expected Auxiliary Space: O(N)

## Constraints:

- 1 <= N <= 10^4

---
