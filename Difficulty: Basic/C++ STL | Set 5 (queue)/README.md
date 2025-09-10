# Queue Operations Problem

You are required to implement different operations on a queue `q`.

---

## Problem Statement
Given a set of queries, perform the following queue operations:

1. **a x** → Push an element `x` at the end of the queue.  
2. **b** → If the queue is not empty, pop the front element and print it. Otherwise, print `-1`.  
3. **c** → Print the size of the queue.  
4. **d** → If the queue is not empty, print the front element. Otherwise, print `-1`.  
5. **e** → If the queue is not empty, print the last element. Otherwise, print `-1`.  

---

## Input
- First line contains an integer `T` → number of test cases.  
- For each test case:  
  - First line contains an integer `Q` → number of queries.  
  - Next line contains `Q` space-separated queries.  

---

## Output
- For each test case, output the results of queries in a single line, space-separated.  

---

## Constraints
- 1 ≤ T ≤ 100  
- 1 ≤ Q ≤ 100  

---

## Example

**Input:**

2
5
a 4 a 6 a 7 b c
4
a 55 a 11 d e


**Output:**

4 2
55 11


---

## Explanation
- **Test Case 1:**
  - a 4 → Queue = [4]  
  - a 6 → Queue = [4, 6]  
  - a 7 → Queue = [4, 6, 7]  
  - b → Pop front = `4`, Queue = [6, 7]  
  - c → Size = `2`  
  - Output: `4 2`

- **Test Case 2:**
  - a 55 → Queue = [55]  
  - a 11 → Queue = [55, 11]  
  - d → Front = `55`  
  - e → Last = `11`  
  - Output: `55 11`

---
