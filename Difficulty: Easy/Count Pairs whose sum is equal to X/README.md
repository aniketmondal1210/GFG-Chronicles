# Count Pairs from Two Linked Lists with Given Sum

## Problem Statement

You are given two linked lists:
- `head1`
- `head2`

👉 All elements in each list are **distinct**

Find the number of pairs `(a, b)` such that:
```
a ∈ head1  
b ∈ head2  
a + b = x
```

---

## Important Note

```
(a, b) and (b, a) are DIFFERENT
But here:
a must come from list1  
b must come from list2
```

---

# Examples

### Example 1

**Input**
```
head1 = 1->2->3->4->5->6
head2 = 11->12->13
x = 15
```

**Output**
```
3
```

---

### Example 2

**Input**
```
head1 = 7->5->1->3
head2 = 3->5->2->8
x = 10
```

**Output**
```
2
```

---

## Constraints:

- 1<= size of both LinkedList <=10^6
- 1 <= node->data <= 10^9
- 1<= x <= 10^9
- Note: All elements in each linked list are unique.

---
