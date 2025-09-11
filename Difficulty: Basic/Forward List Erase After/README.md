# Erase Element from a Forward List using `erase_after()`

We are given a **forward_list** of size `n`.  
The task is to **erase only one element after the default iterator position** and return the updated list.  

We can use the STL method **`erase_after()`**.

---

## 🔹 STL Function Used

- **`erase_after(position)`**  
  Removes the element **immediately after** the given iterator `position`.

---

## 🔹 Example

### Input

n = 4
fwdlist = [10, 20, 30, 40]


### Output

10 30 40


**Explanation:**  
- Default iterator points to the **first element** (`10`).  
- `erase_after()` removes the element right after it (`20`).  
- Final list becomes `[10, 30, 40]`.

---
