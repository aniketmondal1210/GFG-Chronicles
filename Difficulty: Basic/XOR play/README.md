# XOR of Proper Divisors

## Problem Statement
Given an integer `N`, find all the **proper divisors** of `N` (excluding `N`) in **sorted order**.  
Then, perform the **XOR operation** on all divisors and append the result at the end of the list.

---

## Examples

### Example 1
**Input:**

N = 10

**Output:**

1 2 5
6

**Explanation:**  
The proper divisors of 10 are `[1, 2, 5]`.  
Performing XOR: `1 ^ 2 ^ 5 = 6`.

---

### Example 2
**Input:**

N = 8

**Output:**

1 2 4
7

**Explanation:**  
The proper divisors of 8 are `[1, 2, 4]`.  
Performing XOR: `1 ^ 2 ^ 4 = 7`.

---

## Constraints
- 1 <= N <= 10^9

---

## Expected Complexity
- **Time Complexity:** O(sqrt(N))
- **Space Complexity:** O(K) where K is the number of divisors of N.

---
