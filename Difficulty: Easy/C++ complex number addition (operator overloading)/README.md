# C++ Complex Number Addition (Operator Overloading)

## Problem Description

This is a functional problem i.e. partial code is already done for you. Your task is to complete the solution accordingly.

You need to add 2 given complex numbers and print the resulting complex number using the `+` operator.

### Requirements

Implement a class named `complex` containing:

- Data members for **real** and **imaginary** parts.
- A **constructor** to assign values to the complex number.
- An **operator function** to add 2 complex numbers.
- A **display()** method to print the resulting complex number in the format:  

real + imaginary_i

yaml
Copy code

---

## Input

- The first line contains the number of test cases.  
- Each test case contains 4 space-separated integers: `Real1 Imag1 Real2 Imag2`.

---

## Output

For each test case, output the resulting complex number in a single line.

---

## Constraints

- 1 <= Test case <= 100
- All integers are within the range of standard int in C++.

---

## Example

### Input
2
3 6 -1 4
2 2 -1 -1

shell
Copy code

### Output
2 + 10i
1 + 1i

cpp
Copy code

---
