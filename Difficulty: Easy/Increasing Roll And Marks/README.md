# Sort Student Records by Roll Number, Marks, and Subject Code

## Problem Statement
We are given student records where each student has:
- **Roll Number**
- **Marks**
- **Subject Code**

Each student may have different numbers of subjects.  
We need to sort the records in **ascending order** according to:
1. Roll Number
2. Marks (if roll numbers are the same)
3. Subject Code (if both roll number and marks are the same)

---

## Input Format
- First line: `T` → number of test cases.  
- For each test case:
  - First line: `N` → total number of data available.  
  - Next 3 lines contain `N` integers each:  
    - Roll numbers `R[i]`  
    - Marks `M[i]`  
    - Subject codes `S[i]`  

---

## Output Format
For each test case, print the sorted records in three lines:
1. Sorted Roll Numbers
2. Sorted Marks
3. Sorted Subject Codes  

---
