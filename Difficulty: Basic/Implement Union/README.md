
## Problem Statement
We need to implement a **binary tree data structure** where:  
- Each **leaf node** stores a `double` data value.  
- Each **internal node** has **two child pointers** (`left` and `right`) but no data.  

We must use a **union** so that the same memory location is reused —  
either to store `double data` or to store child pointers.

---

## Concept
- **Union:** Allows storing different data types in the same memory location, but only one at a time.  
- This is memory-efficient because a node can either be:
  - A **leaf node** with data, or  
  - An **internal node** with left and right children.

---
