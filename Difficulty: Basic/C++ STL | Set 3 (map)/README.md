# Implement Operations on a Map

## Problem Statement
You are given multiple test cases. 

For each test case, perform operations on a **map** based on the queries.

Each query can be one of the following:

1. **`a x y`** → Insert key `x` with value `y` into the map  
2. **`b x`** → Print the value of key `x` if present, otherwise print `-1`  
3. **`c`** → Print **all key-value pairs** in the map in insertion order, as  

key1 value1 key2 value2 ...


All outputs for each test case must be printed **in a single line**, space-separated.

---

## Input Format
- First line: Integer `T` (number of test cases)  
- For each test case:
- First line: Integer `Q` (number of queries)
- Next line: `Q` space-separated queries

---

## Output Format
For each test case, print the results of queries (`b` and `c`) in one line.

---

## Constraints

- 1 ≤ T ≤ 100
- 1 ≤ Q ≤ 100


---

## Example

### Input

2

4

a 1 2 a 66 3 b 66 c

3

a 1 66 b 5 c


### Output

3 1 2 66 3

-1 1 66


---

## Explanation

### Test Case 1
Operations:

1. `a 1 2` → Insert key `1` with value `2`  
2. `a 66 3` → Insert key `66` with value `3`  
3. `b 66` → Key found → print `3`  
4. `c` → Print map contents → `1 2 66 3`  

Output:  

3 1 2 66 3


---

### Test Case 2
Operations:

1. `a 1 66` → Insert key `1` with value `66`  
2. `b 5` → Key not found → print `-1`  
3. `c` → Print map contents → `1 66`  

Output:

-1 1 66


---
