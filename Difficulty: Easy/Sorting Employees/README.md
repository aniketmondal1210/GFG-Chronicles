# Sort Employees by Salary

## Problem Statement
You are given two arrays:
- `employee[]`: where `employee[i]` denotes the name of the i-th employee
- `salary[]`: where `salary[i]` denotes the salary of the i-th employee

Your task is to **sort the `employee` array** based on the following rules:
1. Sort employees by **salary in non-decreasing order**
2. If two or more employees have the **same salary**, sort them **alphabetically by their names**

Return the sorted `employee` array.

---

## Example 1
**Input:**

employee = ["chef", "geek"]
salary = [100, 50]


**Output:**

["geek", "chef"]


**Explanation:**
- `"geek"` has a lower salary (50) than `"chef"` (100), so `"geek"` comes first.

---

## Example 2
**Input:**

employee = ["ram", "shyam", "rohan"]
salary = [60, 45, 60]


**Output:**

["shyam", "ram", "rohan"]


**Explanation:**
- `"shyam"` has the lowest salary (45)
- `"ram"` and `"rohan"` both have salary 60, so they are sorted alphabetically

---

## Constraints

- 1 ≤ employee.size() = salary.size() ≤ 10⁵
- 1 ≤ salary[i] ≤ 10⁶
- employee[i] contains only lowercase alphabetic characters


---
