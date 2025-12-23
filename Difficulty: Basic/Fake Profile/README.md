# Determine Gender from Username

## Problem Statement
A hacker named **Vijay** has devised a method to determine whether a user on a social networking site is **male** or **female** based on their username.

### Vijay’s Method
- Count the number of **distinct consonant characters** in the username.
- **Ignore vowels** (`a, e, i, o, u`).
- If the count of distinct consonants is:
  - **Odd** → User is **Male** → print `"HE!"`
  - **Even** → User is **Female** → print `"SHE!"`

The input string contains **only lowercase English alphabets**.

---

## Examples

### Example 1
**Input:**  

a = "jpmztf"


**Output:**  

SHE!


**Explanation:**  
Distinct consonants = `{j, p, m, z, t, f}` → count = 6 (even)  
So, the user is **Female**.

---

### Example 2
**Input:**  

a = "plkaitw"


**Output:**  

HE!


**Explanation:**  
Vowels ignored: `a, i`  
Distinct consonants = `{p, l, k, t, w}` → count = 5 (odd)  
So, the user is **Male**.

---

## Time and Space Complexity
- **Time Complexity:** `O(|a|)`
- **Space Complexity:** `O(1)`  
  (At most 21 consonants can be stored.)

---

## Constraints

1 ≤ Length of string ≤ 1000

---
