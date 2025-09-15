# Insert into Multimap, Erase Element, and Print

## Problem
You are given an array `arr`. You need to:
1. Insert the elements of `arr` into a **multimap** where:
   - key = element value  
   - value = index of that element in the array.  
2. Erase a given element `x` from the multimap.
   - If erased, print `"erased x"`.  
   - Otherwise, print `"not found"`.  
3. Implement `print()` function to print all `(key, value)` pairs of the multimap.

---

### Example

**Input:**

arr[] = [9, 8, 7, 4, 4, 2, 1, 1, 9, 8], x = 1


**Output:**

1 6
1 7
2 5
4 3
4 4
7 2
8 1
8 9
9 0
9 8
erased 1
2 5
4 3
4 4
7 2
8 1
8 9
9 0
9 8


---

### Constraints
- `1 ≤ arr.size() ≤ 1000`
- `1 ≤ arr[i] ≤ 10^6`

---
