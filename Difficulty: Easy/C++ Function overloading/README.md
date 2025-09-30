#  Volume of Cube, Cylinder, and Rectangular Box

## Problem Statement
Gurkaran wants to calculate the volume of different objects (cube, cylinder, rectangular box) based on their dimensions.

- Use the value of π (pi) as **3.14159**.
- Based on the given object type:
  - `1` → Cube (input: side)
  - `2` → Cylinder (input: radius, height)
  - `3` → Rectangular Box (input: length, breadth, height)

You need to compute and output the **volume**.

---

## Input Format
- First line: `t` → number of test cases  
- Next `t` lines: each contains a query  
  - First integer → object type (`1`, `2`, or `3`)  
  - Remaining integers → dimensions of the object  

---

## Output Format
- For each test case, print the volume.  
- The output should be a single integer (for cube and box) or double (for cylinder).  

---

## Examples

### Example 1
**Input**

3

1 2

2 1 2

3 1 2 3


**Output**

8
6.29038
6


---

### Example 2
**Input**

2

1 4

2 2 5


**Output**

64
62.8318


---

## Constraints
- `1 ≤ t ≤ 100`
- `0 ≤ dimensions ≤ 100`
- First number in a query ∈ `{1, 2, 3}`

---
