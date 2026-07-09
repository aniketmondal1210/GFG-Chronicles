# Delete the Middle Node of a Linked List

## Problem

Given the head of a singly linked list, delete its middle node and return the modified list.

**Note:**

- If the linked list has an **even** number of nodes, delete the **second middle** node.
- If the linked list contains only **one node**, return `NULL`.

---

## Examples

### Example 1

**Input**

```text
1 -> 2 -> 3 -> 4 -> 5
```

**Output**

```text
1 -> 2 -> 4 -> 5
```

**Explanation**

The middle node is `3`, so it is removed.

---

### Example 2

**Input**

```text
2 -> 4 -> 6 -> 7 -> 5 -> 1
```

**Output**

```text
2 -> 4 -> 6 -> 5 -> 1
```

**Explanation**

There are two middle nodes (`6` and `7`). According to the problem, the **second middle** (`7`) is deleted.

---

### Example 3

**Input**

```text
7
```

**Output**

```text
<empty linked list>
```

**Explanation**

The list contains only one node, so it is deleted.

---

## Constraints:

- 1 <= number of nodes <= 10^5
- 1 <= node->data <= 10^9

---
