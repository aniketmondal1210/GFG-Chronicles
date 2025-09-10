# Heapify a Vector using `make_heap()`

You are given a vector `arr[]` of integers.  
The task is to **heapify the given vector** using the STL function `make_heap()`.

---

## 🔹 Function: `make_heap()`

- **Definition**: Transforms a sequence into a **heap**.  
- **Default Behavior**: Creates a **max-heap** (largest element at the root).  
- **Syntax**:
  ```cpp
  make_heap(v.begin(), v.end());

🔹 Examples
Example 1

Input:

arr = [3, 6, 4, 2, 1, 5]

Output:

[6, 3, 5, 2, 1, 4]

Example 2

Input:

arr = [3, 2, 1, 3]

Output:

[3, 3, 1, 2]
