# Taking String and Integer Input in C++

## Problem
There are many times when we need to take input of a string that contains multiple words.  
Here, we will learn how to take input of a string that comprises of multiple words.  
Also, we will learn to clear the input buffer using `cin.ignore()`.

Your task is to take input of strings and integers and produce the output.

---

## Notes
1. Use `std::cin`, `getline()`, and `cin.ignore()`.  
2. When `cin` is followed by `getline()`, the leftover newline character in the buffer causes issues.  
   - This problem can be solved by using `cin.ignore()` before calling `getline()`.

---

## Input Format
- First line: `T` (number of testcases).  
- For each testcase, there will be three lines of input:  
  1. A string (may contain spaces)  
  2. An integer  
  3. Another string (may contain spaces)

---

## Output Format
For each testcase, print the variables in the **same order** as taken in input.

---

## Example

### Input

1
hello world
5
hello


### Output

hello world
5
hello


---

## Constraints
- 1 ≤ T ≤ 10  
- Strings may contain spaces  
- Integers fit within `int` range  

---
