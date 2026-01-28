# Number with Maximum Zeroes

## Problem Statement
Given an array `arr[]` of integers, find the number that contains the **maximum number of zero digits**.

### Rules
- If **no number contains any zero**, return `-1`.
- If **multiple numbers** have the same (maximum) number of zeroes, return the **largest number among them**.

---

## Examples

### Example 1
**Input**

arr = [10, 20, 3000, 9999, 200]

**Output**

3000

**Explanation**  
- 10 → 1 zero  
- 20 → 1 zero  
- 3000 → 3 zeroes  
- 9999 → 0 zeroes  
- 200 → 2 zeroes  
Maximum zeroes = 3 → number = **3000**

---

### Example 2
**Input**

arr = [1, 2, 3, 4]

**Output**

-1

**Explanation**  
No number contains zero.

---

## Time & Space Complexity:

- Expected Time Complexity: O(n*log10(max(arr[i])). 
- Expected Auxiliary Space: O(1).

---

## Constraints:

- 1 ≤ arr.size() ≤ 10^5
- 1 < arr[i] < 10^100

---
