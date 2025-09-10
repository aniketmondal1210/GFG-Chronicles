# Deque Operations Problem

---

## Problem Statement
You are given queries to perform operations on a **deque**.  
The deque supports:  
1. Insert at front  
2. Insert at back  
3. Remove from front  
4. Remove from back  
5. Sort the deque  
6. Reverse the deque  
7. Print the deque  
8. Print size  
9. Print front element  
10. Print back element  

If the deque is empty when performing a remove or access operation, print `-1`.

---

## Input Format
- First line: `T` → number of test cases  
- For each test case:  
  - First line: `Q` → number of queries  
  - Next line: `Q` space-separated queries  

---

## Output Format
- Print output for each query as required.  
- For queries that modify or display the deque, print its contents.  
- For queries that return values (size, front, back), print those values.  
- Print `-1` when deque is empty and an invalid operation is attempted.  

---

## Example

**Input**

1
10
1 6 2 9 9 10 5 6 7 8 3 4


**Output**

6
6 9
6
9
6 9
9 6
9 6
2
6
-1

