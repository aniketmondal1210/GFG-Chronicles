# Student(s) with Maximum Average Score

## Problem Statement

A file contains records of students in the following format:

```text
{StudentName, Marks1, Marks2, Marks3}
```

There are `N` students in the class.

For each student:

- Compute the average of the three marks.
- The average is **floored** (integer division).

Return a string containing:

- The names of all students having the **maximum average**, in the same order as they appear in the input.
- Followed by the maximum average.

---

## Examples

### Example 1

**Input**

```text
N = 2

S = {
"Shrikanth 20 30 10",
"Ram 100 50 10"
}
```

**Output**

```text
Ram 53
```

**Explanation**

```text
Shrikanth → (20 + 30 + 10) / 3 = 20

Ram → (100 + 50 + 10) / 3 = 53
```

Ram has the highest average.

---

### Example 2

**Input**

```text
N = 3

S = {
"Adam 50 10 40",
"Rocky 100 90 10",
"Suresh 10 90 100"
}
```

**Output**

```text
Rocky Suresh 66
```

**Explanation**

```text
Adam   → 33

Rocky  → 66

Suresh → 66
```

Rocky and Suresh share the highest average.

---

## Your Task:
You don't need to read input or print anything. Your task is to complete the function studentRecord() which takes an Integer N and a vector of vector of strings where each string vector contains 4 space separated inputs, the first being the name of the student and the rest being the marks of the student. The function should return a string consisting of two or more words where the last word is the max average of the class and the preceding words are names of student/s who have the max average. The names of the students should appear in the same order as they are given in the Input.

 

## Expected Time Complexity: O(N)
## Expected Auxiliary Space: O(N)

 

## Constraints:

- 1 <= N <= 10^4
- 1 <= marks <= 100
- 1 <= Length of the Name <= 10

---
