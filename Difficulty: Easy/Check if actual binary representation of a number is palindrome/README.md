# Binary Palindrome Check

## Problem
Given a non-negative integer `N`, check whether its **binary representation** is a palindrome or not.  
- **Palindrome** means the binary string reads the same forward and backward.  
- No leading zeros are considered.  

Return:
- `1` if palindrome  
- `0` otherwise  

---

## Constraints
- `0 ≤ N ≤ 2^63 - 1`
- **Expected Time Complexity:** `O(log(N))`  
- **Expected Auxiliary Space:** `O(1)`  

---

## Examples

### Example 1
**Input**

N = 5


**Output**

1


**Explanation**  
Binary representation of 5 = `101` → palindrome.

---

### Example 2
**Input**

N = 10


**Output**

0


**Explanation**  
Binary representation of 10 = `1010` → not palindrome.  

---
