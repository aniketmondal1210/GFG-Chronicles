# N-Bit OR Gate Output

## Problem Statement
You are given **N bits** as input to an **OR Gate**.  
You need to determine the **output** produced after performing the **bitwise OR operation** on all N bits.

---

## OR Gate Truth Table

| Input A | Input B | Output (A OR B) |
|----------|----------|----------------|
| 1 | 1 | 1 |
| 1 | 0 | 1 |
| 0 | 1 | 1 |
| 0 | 0 | 0 |

The OR operation returns `1` if **any** input is `1`, otherwise it returns `0`.

---

## Example 1

**Input:**

N = 4
arr = [1, 1, 1, 0]


**Output:**

1


**Explanation:**

1 | 1 = 1
1 | 1 = 1
1 | 0 = 1
Final Output = 1


---

## Example 2

**Input:**

N = 4
arr = [0, 0, 1, 0]


**Output:**

1


**Explanation:**

0 | 0 = 0
0 | 1 = 1
1 | 0 = 1
Final Output = 1


---

## Constraints

1 <= N <= 1000
arr[i] ∈ {0, 1}


**Expected Time Complexity:** O(N)  
**Expected Space Complexity:** O(1)

---
