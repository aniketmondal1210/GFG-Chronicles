# Unordered Set Operations Problem

---

## Problem Statement
You need to perform different operations on an **unordered set** `s` based on queries.

### Queries
1. **a x** → Insert element `x` into the set.  
2. **b x** → Erase element `x` from the set.  
3. **c x** → Print `1` if `x` is present in the set, else print `-1`.  
4. **d** → Print the size of the set.  

---

## Input
- First line: `T` → number of test cases.  
- For each test case:  
  - First line: `Q` → number of queries.  
  - Next line: `Q` space-separated queries.  

---

## Output
- For each test case: print results of all output queries (from `b`, `c`, `d`) space-separated.  

---

## Constraints
- 1 ≤ T ≤ 100  
- 1 ≤ Q ≤ 100  

---

## Example

**Input:**

2
5
a 1 a 2 a 3 b 2 d
4
a 1 a 5 d c 2


**Output:**

2
2 -1


---

## Explanation
- **Test Case 1:**
  - a 1 → {1}  
  - a 2 → {1,2}  
  - a 3 → {1,2,3}  
  - b 2 → {1,3}  
  - d → size = `2`  
  - Output: `2`

- **Test Case 2:**
  - a 1 → {1}  
  - a 5 → {1,5}  
  - d → size = `2`  
  - c 2 → 2 not in set → `-1`  
  - Output: `2 -1`

---
