# Iterate Over a Vector Using Iterators

We are given a vector `v`.  
We need to use **iterators (`it1` and `it2`)** to iterate over the vector from `begin()` to `end()` and print its elements.

---

## 🔹 Example

### Input

vector -> 1 2 3 4 5


### Output

1 2 3 4 5


---

## 🔹 Explanation

- `vector<int>::iterator it1 = v.begin();` → points to the first element.  
- `vector<int>::iterator it2 = v.end();` → points to **one position after the last element**.  
- We loop from `it1` to `it2` and dereference (`*it`) to access values.

---
