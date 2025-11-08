# Modular Multiplicative Inverse

## Problem Statement
Given two integers `n` and `m`, find the **smallest modular multiplicative inverse** of `n` under modulo `m`.  
If it does not exist, return `-1`.

A number `x` is said to be the modular multiplicative inverse of `n` under modulo `m` if:

(n * x) % m = 1

---

## Example 1
**Input:**

n = 3, m = 11


**Output:**

4


**Explanation:**  
(4 * 3) % 11 = 12 % 11 = 1  
Hence, `4` is the modular inverse of `3` under modulo `11`.

---

## Example 2
**Input:**

n = 10, m = 17


**Output:**

12


**Explanation:**  
(12 * 10) % 17 = 120 % 17 = 1
Hence, `12` is the modular inverse of `10` under modulo `17`.

---

## Constraints

1 ≤ n ≤ 10^4
1 ≤ m ≤ 10^5


---
