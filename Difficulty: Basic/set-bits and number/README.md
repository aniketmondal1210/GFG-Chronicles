# Product of Number and Its Set Bits

## Problem Statement

Given an integer `N`, return:

```
N × (number of set bits in N)
```

A **set bit** is a bit with value `1` in the binary representation.

---

# Examples

### Example 1

**Input**
```
N = 2
```

Binary:
```
2 → 10
```

Set bits = 1  

**Output**
```
2 × 1 = 2
```

---

### Example 2

**Input**
```
N = 3
```

Binary:
```
3 → 11
```

Set bits = 2  

**Output**
```
3 × 2 = 6
```

---

## Expected Time Complexity: O(Log N)
## Expected Auxiliary Space: O(1)


## Constraints:

- 1 <= N <= 10^6

---
