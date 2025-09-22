# Self Referential Structures in C

## Explanation
Self-referential structures are structures that contain one or more pointers pointing to the **same type of structure** as their member.  
They are an important concept used when implementing data structures such as:
- **Linked Lists**
- **Trees**
- **Graphs**

In a **Linked List**, each node contains:
1. **Data** → the value stored in the node.  
2. **Pointer to next node** → which connects the current node to the next node in the list.  

This pointer is of type `struct node*`, hence the structure becomes **self-referential**.

---
