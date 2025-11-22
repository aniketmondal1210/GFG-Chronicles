# Implement Operations on a Set

## Problem Statement
You are given multiple test cases.  
For each test case, perform operations on a **set `s`** based on queries.

Each query is one of the following types:

1. **`a x`** → Insert element `x` into the set  
2. **`b`** → Print all elements of the set in sorted order  
3. **`c x`** → Erase element `x` from the set  
4. **`d x`** → Print `1` if `x` is present, else print `-1`  
5. **`e`** → Print the size of the set  

All outputs for a test case must be printed **in one line**, space-separated.

---

## Input Format
- First line: integer `T` (number of test cases)  
- For each test case:
  - First line: integer `Q` (number of queries)
  - Next line: `Q` space-separated queries

---

## Output Format
For each test case, print the results of the queries (`b`, `d`, `e`) in a single line.

---

## Constraints

- 1 ≤ T ≤ 100
- 1 ≤ Q ≤ 100


---

## Example

### Input

2

6

a 1 a 2 a 3 b c 2 b

5

a 1 a 11 e d 5 d 2


### Output

1 2 3 1 3

2 1 -1


---

## Explanation

### Test Case 1  
Queries performed:

1. `a 1` → set = {1}  
2. `a 2` → set = {1, 2}  
3. `a 3` → set = {1, 2, 3}  
4. `b` → output: `1 2 3`  
5. `c 2` → set = {1, 3}  
6. `b` → output: `1 3`  

Final output:  

1 2 3 1 3


### Test Case 2  
Queries performed:

1. `a 1` → set = {1}  
2. `a 11` → set = {1, 11}  
3. `e` → output: `2`  
4. `d 5` → output: `-1`  
5. `d 2` → output: `-1`  

Final output:  

2 -1 -1
