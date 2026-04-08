# Find Node at Given Index (1-Based)

## Problem Statement

Given the head of a **Singly Linked List** and an integer `index` (1-based), return the **value of the node** at that index.

If the index does not exist, return:
```
-1
```

---

# Examples

### Example 1

**Input**
```
LinkedList: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7
index = 3
```

**Output**
```
3
```

**Explanation**
The 3rd node contains value `3`.

---

### Example 2

**Input**
```
LinkedList: 19 -> 28 -> 37 -> 46 -> 55
index = 6
```

**Output**
```
-1
```

**Explanation**
List has only 5 nodes, so index 6 doesn't exist.

---

## Expected Time Complexity: O(n)
## Expected Auxiliary Space: O(1)

# Constraints:

- 1 <= number of nodes <= 10^5
- 1 <= node->data , k <= 10^5

---
