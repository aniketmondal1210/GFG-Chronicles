# Vector Erase and Clear Operations

## Problem Statement
You are given a vector `arr[]` containing integers.  
You need to perform different operations on the vector depending on the query:

1. **clearAll()** → Removes all elements from the vector.  
2. **eraseAt(pos)** → Removes the element from a specified position `pos` in the vector (0-based indexing).  
3. **eraseInRange(start, end)** → Removes elements in the given range `[start, end)`, where `end` is **not included**.  

---

## Examples

### Example 1
**Input:**  

arr[] = [2, 3, 4, 5, 6]
query: eraseAt(3)

**Output:**  

[2, 3, 4, 6]

**Explanation:**  
The element at position `3` (i.e., `5`) is removed.

---

### Example 2
**Input:**  

arr[] = [1, 4, 5, 4, 2]
query: eraseInRange(2, 4)

**Output:**  

[1, 4, 2]

**Explanation:**  
Elements from index `2` to `3` (`5, 4`) are removed.

---
