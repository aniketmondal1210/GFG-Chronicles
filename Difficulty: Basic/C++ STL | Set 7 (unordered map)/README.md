# Implement Operations on Unordered Map

We are given a number of queries to be performed on an **unordered_map**.  
The task is to implement these operations:

---

## 🔹 Query Types

1. **`a x y`** → Insert a key-value pair `(x, y)` into the map.  
2. **`b x`** → Print the value of key `x` if it exists, otherwise print `-1`.  
3. **`c`** → Print the size of the map.  
4. **`d x`** → Remove the entry with key `x` from the map (if it exists).

---

## 🔹 Example

### Input

2
5
a 1 2 a 66 3 b 66 d 1 c
3
a 1 66 b 5 c


### Output

3 1
-1 1


**Explanation:**

- **Test case 1:**
  - `a 1 2` → map = {1 → 2}  
  - `a 66 3` → map = {1 → 2, 66 → 3}  
  - `b 66` → prints `3`  
  - `d 1` → removes key `1`, map = {66 → 3}  
  - `c` → size = `1`  

  Output: `3 1`

- **Test case 2:**
  - `a 1 66` → map = {1 → 66}  
  - `b 5` → key `5` not found → `-1`  
  - `c` → size = `1`  

  Output: `-1 1`

---
