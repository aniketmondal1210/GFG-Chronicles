# Largest Element with Minimum Frequency

## Problem Statement

Given an array **A[]** of size **N**, find the **largest element** among those elements that have the **minimum frequency**.

---

# Examples

### Example 1

**Input**
```
A = [2, 2, 5, 50, 1]
```

**Frequencies**
```
2 → 2 times
5 → 1 time
50 → 1 time
1 → 1 time
```

Minimum frequency = **1**

Elements with freq = 1:
```
5, 50, 1
```

Largest among them:
```
50
```

**Output**
```
50
```

---

### Example 2

**Input**
```
A = [3, 3, 5, 5]
```

**Frequencies**
```
3 → 2
5 → 2
```

Minimum frequency = **2**

Largest element:
```
5
```

**Output**
```
5
```

---

## Expected Time Complexity: O(N)
## Expected Space Complexity: O(N)

## Constraints:

- 1 <= N <= 10^5
- 1 <= A[i] <= 10^6

---
