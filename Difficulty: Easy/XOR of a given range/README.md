# XOR of Given Range in Array

## Problem Statement

You are given an array `nums`.  

Your task is to complete the function `getXor()` which returns the **XOR of elements from index `a` to `b` (inclusive)**.

---

## Examples

### Example 1

**Input**
```
nums = {1, 3, 5, 7, 9, 11}
a = 1, b = 3
```

**Output**
```
1
```

**Explanation**
```
3 ^ 5 ^ 7 = 1
```

---

### Example 2

**Input**
```
nums = {1, 2, 3, 4, 5}
a = 0, b = 4
```

**Output**
```
1
```

**Explanation**
```
1 ^ 2 ^ 3 ^ 4 ^ 5 = 1
```

---

---

## Time Complexity

```
O(n)
```

In worst case, we traverse the entire array.

---

## Space Complexity

```
O(1)
```

Only one variable is used.

---
