# Modular Node in Linked List

## Problem Statement

Given the head of a **singly linked list** and an integer `k`, find the **last node** whose **position (1-based index)** is divisible by `k`.

If no such node exists, return:
```
-1
```

---

# Examples

### Example 1

**Input**
```
LinkedList: 1 → 2 → 3 → 4 → 5 → 6 → 7
k = 3
```

**Indices**
```
1  2  3  4  5  6  7
```

Indices divisible by 3:
```
3, 6
```

Last such index = **6**

**Output**
```
6
```

---

### Example 2

**Input**
```
LinkedList: 19 → 28 → 37 → 46 → 55
k = 13
```

No index divisible by 13

**Output**
```
-1
```

---

## Constraints:

- 1 <= number of nodes <= 10^5
- 1 <= node->data , k <= 10^5

---
