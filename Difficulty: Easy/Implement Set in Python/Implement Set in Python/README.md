# Set Operations in Python

A **set** is an **unordered collection** of items where every element is **unique** and must be **immutable**, but the set itself is **mutable**.  
You **cannot access an element of a set using indexing or slicing**, but you **can update the set**.

---

## Some Important Set Functions in Python:

- `add()`: Adds an element to the set.
- `clear()`: Removes all elements from the set.
- `discard()`: Removes an element from the set if present.
- `remove()`: Removes an element from the set. If the element is not present, it raises an error.
- `pop()`: Removes and returns an arbitrary set element. Raises an error if the set is empty.
- `union()`: Returns the union of sets in a new set.
- `update()`: Updates the set with the union of itself and others.
- `len()`: Returns the length of the set.
- `sorted()`: Returns a new sorted list from elements in the set.
- `sum()`: Returns the sum of all elements in the set.

---

## Problem: Perform Given Queries on a Set

The task is to perform the given queries on the set as described below:

- **a. `i element`**: Add element `i` to the set.
- **b. `r element`**: Remove element `r` from the set.
- **c. `s`**: Find the sum of elements in the set.

---

## Examples:

### Example 1:

**Input:**  
`st = [6, 7, 81, 2, 1]`, `i = 3`, `r = 6`  

**Output:**  
1 2 3 6 7 81

1 2 3 7 81

94


**Explanation:**  
After adding 3, set becomes `[1, 2, 3, 6, 7, 81]`.  
After removing 6, set becomes `[1, 2, 3, 7, 81]`.  
Sum of set is `94`.

---

### Example 2:

**Input:**  
`st = [1, 9, 6]`, `i = 78`, `r = 9`  

**Output:**  

1 6 9 78

1 6 78

85


**Explanation:**  
After adding 78, set becomes `[1, 6, 9, 78]`.  
After removing 9, set becomes `[1, 6, 78]`.  
Sum of set is `85`.

---

## Constraints:

- 1 ≤ S[i] ≤ 10⁴
