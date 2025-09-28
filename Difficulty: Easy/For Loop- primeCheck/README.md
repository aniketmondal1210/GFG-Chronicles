# Prime Number Check using For Loop

## Problem Statement
You are given a number `n`.  
Your task is to determine whether the number is **prime** or not.  

- A number is **prime** if it is divisible **only by 1 and itself**.  
- **Note:** 1 is **not prime**.

---

## Examples

### Example 1
**Input:**  

n = 1

**Output:**  

No

**Explanation:**  
1 is not a prime number.

---

### Example 2
**Input:**  

n = 2

**Output:**  

Yes

**Explanation:**  
2 is divisible only by 1 and 2 → hence it is prime.

---

### Example 3
**Input:**  

n = 15

**Output:**  

No

**Explanation:**  
15 is divisible by 3 and 5 → not prime.

---

## Complexity
- **Time Complexity:** `O(√n)` (since checking till square root is enough).  
- **Auxiliary Space:** `O(1)`.

---

## Constraints
- `1 ≤ n ≤ 10^9`

---
