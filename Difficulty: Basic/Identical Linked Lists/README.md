# Check if Two Linked Lists are Identical

## Problem Statement

Given two singly linked lists `head1` and `head2`, determine whether they are **identical**.

Two linked lists are identical if:
1. They have the **same number of nodes**
2. Each corresponding node has the **same value in the same order**

Return:
```
true  → if identical  
false → otherwise
```

---

# Examples

### Example 1

**Input**
```
head1: 1 → 2 → 3 → 4 → 5 → 6  
head2: 99 → 59 → 42 → 20
```

**Output**
```
false
```

**Explanation**
Different lengths and values.

---

### Example 2

**Input**
```
head1: 1 → 2 → 3 → 4 → 5  
head2: 1 → 2 → 3 → 4 → 5
```

**Output**
```
true
```

**Explanation**
All nodes match in value and order.

---

## Constraints:

- 1 ≤ length of lists ≤ 10^5
- 1 ≤ elements of lists ≤ 10^5

---
Same values + same length → identical  
Else → not identical
```
