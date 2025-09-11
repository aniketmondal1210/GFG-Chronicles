# List Operations in C++

You are given an empty list. You need to implement different operations on **List A**:

---

## 🔹 Operations Supported

1. **`1 x`** → Adds element `x` to the **end** of the list and print the list.  
2. **`2`** → Sorts the list in ascending order and print it.  
3. **`3`** → Reverses the list and print it.  
4. **`4`** → Prints the **size** of the list.  
5. **`5`** → Prints space-separated values of the list. If the list is empty, print `-1`.  
6. **`6`** → Removes an element from the **back** of the list and print it. If empty, print `-1`.  
7. **`7`** → Removes an element from the **front** of the list and print it. If empty, print `-1`.  
8. **`8 x`** → Adds element `x` to the **front** of the list and print the list.  

---

## 🔹 Example

### Input

1
8
1 5 8 1 3 4 5 6 1 6 7


### Output

5
1 5
5 1
2
5 1
5
5 6
6


---

## 🔹 Explanation
- `1 5` → add `5` at end → `[5]`  
- `8 1` → add `1` at front → `[1, 5]`  
- `3` → reverse → `[5, 1]`  
- `4` → size = `2`  
- `5` → print → `5 1`  
- `6` → remove from back (`1`) → `[5]`, print `5`  
- `1 6` → add `6` at end → `[5, 6]`  
- `7` → remove from front (`5`) → `[6]`, print `6`  

---
