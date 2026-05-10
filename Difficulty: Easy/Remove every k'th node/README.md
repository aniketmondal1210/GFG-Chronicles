# Remove Every Kth Node from Linked List

## Problem Statement

Given a singly linked list and an integer `k`, remove every `kth` node from the linked list.

Return the modified linked list.

---

# Examples

### Example 1

```text
Input:
1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8
k = 2

Output:
1 -> 3 -> 5 -> 7
```

### Explanation

Nodes at positions:

```text
2, 4, 6, 8
```

are removed.

---

### Example 2

```text
Input:
1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10
k = 3

Output:
1 -> 2 -> 4 -> 5 -> 7 -> 8 -> 10
```

---

# Constraints

```text
1 <= size of linked list <= 10^6
1 <= k <= size of linked list
```

---
