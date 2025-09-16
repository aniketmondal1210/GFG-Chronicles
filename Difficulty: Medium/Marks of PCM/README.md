# Custom Sort of Student Marks

## Problem
You are provided with marks of `N` students in **Physics**, **Chemistry**, and **Maths**.  
You need to sort them according to the following rules:

1. Sort students in **ascending order of Physics marks**.  
2. If Physics marks are equal, sort by **descending order of Chemistry marks**.  
3. If both Physics and Chemistry marks are equal, sort by **ascending order of Maths marks**.  

The sorting should update the original arrays.

---

## Example

### Input

N = 10
phy[] = {4, 1, 10, 4, 4, 4, 1, 10, 1, 10}
chem[] = {5, 2, 9, 6, 3, 10, 2, 9, 14, 10}
math[] = {12, 3, 6, 5, 2, 10, 16, 32, 10, 4}


### Output

1 14 10
1 2 3
1 2 16
4 10 10
4 6 5
4 5 12
4 3 2
10 10 4
10 9 6
10 9 32


### Explanation
- First, Physics marks are sorted in ascending order.  
- For equal Physics marks, Chemistry is sorted in descending order.  
- For equal Physics and Chemistry marks, Maths is sorted in ascending order.  

---

## Constraints
- `1 <= N <= 10000`
- **Time Complexity:** `O(N log N)`
- **Auxiliary Space:** `O(N)`

---
