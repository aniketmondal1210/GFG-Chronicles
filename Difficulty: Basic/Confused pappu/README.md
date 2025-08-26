# Pappu and Confusion Between 6 & 9

## Problem
Pappu is confused between `6` & `9`.  
He works in the billing department of abc company, and his task is to return the remaining amount to customers.  
If the actual remaining amount is given, we need to calculate the **maximum possible extra amount** Pappu might mistakenly give to customers.

---

## Constraints
- `1 ≤ N ≤ 10^7`
- **Expected Time Complexity:** `O(log10(amount))`  
- **Expected Auxiliary Space:** `O(log10(amount))`

---

## Examples

### Example 1
**Input**

amount = 56

**Output**

3

**Explanation**
- Pappu may treat `56` as `59`.
- Extra = `59 - 56 = 3`.

---

### Example 2
**Input**

amount = 66

**Output**

33

**Explanation**
- Pappu may treat `66` as `99`.
- Extra = `99 - 66 = 33`.

---

✅ Time Complexity = `O(log10(N))` (processing each digit once)  
✅ Space Complexity = `O(log10(N))` (string storage or digits)

---
