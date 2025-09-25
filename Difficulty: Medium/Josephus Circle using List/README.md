# Josephus Problem (Last Man Standing)

## Problem Statement
You are given two integers `n` and `k` where:  
- `n` = total number of people standing in a circle.  
- `k` = the k-th person gets killed in each round.  

Find the position of the **last person remaining** (safe position).  

- Indexing starts from **1**.  
- Counting always resumes from the next person after a killing.  

---

## Constraints
- 2 ≤ n, k ≤ 20  

---

## Examples

### Example 1
**Input:**  

n = 3, k = 2

**Output:**  

3

**Explanation:**  
- People = {1, 2, 3}  
- Kill 2 → Remaining {1, 3}  
- Kill 1 → Remaining {3}  

Safe position = **3**

---

### Example 2
**Input:**  

n = 5, k = 3

**Output:**  

4

**Explanation:**  
- People = {1, 2, 3, 4, 5}  
- Kill 3 → Remaining {1, 2, 4, 5}  
- Kill 1 → Remaining {2, 4, 5}  
- Kill 5 → Remaining {2, 4}  
- Kill 2 → Remaining {4}  

Safe position = **4**

---
