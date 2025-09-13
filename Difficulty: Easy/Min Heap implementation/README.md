# Priority Queue Operations

## Problem Statement
You are given a **priority queue** and `Q` queries.  
The task is to perform operations based on the queries:

1. `p x` → Push element `x` into the priority queue and print its **size**.  
2. `pp` → Pop the **top element** from the priority queue and print its **size**.  
3. `t` → Print the **top element** of the priority queue. If empty, return `-1`.  

---

## Example
**Input:**  

Q = 5
p 5
p 3
p 1
t
pp


**Output:**  

1
2
3
1
2


**Explanation:**  
- Push `5` → size = 1  
- Push `3` → size = 2  
- Push `1` → size = 3  
- Top → `1` (min element at top since min heap is used)  
- Pop → removes `1`, size = 2  

---

## Constraints
- `1 <= Q <= 100`

---
