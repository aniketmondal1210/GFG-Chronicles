# Sum of All Subsequences of a Number

## Problem Statement

Given a number represented as a **string `S`**, find the **sum of elements present in all possible subsequences**.

A **subsequence** is a sequence derived by deleting some or no elements **without changing the order**.

---

# Examples

### Example 1

**Input**
```
S = "123"
```

**Subsequences**

```
{1}
{2}
{3}
{1,2}
{1,3}
{2,3}
{1,2,3}
```

**Sum**

```
1 + 2 + 3 + (1+2) + (1+3) + (2+3) + (1+2+3)
= 1 + 2 + 3 + 3 + 4 + 5 + 6
= 24
```

**Output**
```
24
```

---

### Example 2

**Input**
```
S = "5"
```

**Subsequences**
```
{5}
```

**Output**
```
5
```

---

## Expected Time Complexity: O(|s|)
## Expected Auxiliary Space: O(1)

## Constraints:

- 1 <= |S| <= 20

---
