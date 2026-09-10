# Remove Duplicates from an Unsorted Linked List

## Problem Description

Given the head of an **unsorted** linked list, remove duplicate elements from the list. 

When a value appears in multiple nodes, the node that appeared **first** should be retained, while all subsequent duplicate nodes must be removed.

---

## Examples

### Example 1
- **Input:** `head = 5 -> 2 -> 2 -> 4`
- **Output:** `5 -> 2 -> 4`
- **Explanation:** Node `2` appears twice. The second occurrence is deleted.

### Example 2
- **Input:** `head = 2 -> 2 -> 2 -> 2 -> 2`
- **Output:** `2`
- **Explanation:** Node `2` is repeated 5 times. All trailing duplicate occurrences are removed.

---

## Constraints

- $1 \le 	{size of linked list} \le 10^6$
- $0 \le 	{node.data} \le 10^6$
