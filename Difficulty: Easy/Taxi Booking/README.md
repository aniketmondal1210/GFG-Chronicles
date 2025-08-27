# Minimum Time to Board a Taxi

## Problem
You are at position `cur` on an infinite X-axis.  
There are `N` taxis available, each at position `pos[i]`, and each taxi takes `time[i]` seconds to travel one unit of distance.

You need to find the **minimum time required** to board a taxi.

---

## Constraints
- `1 ≤ N ≤ 10^5`
- `1 ≤ cur ≤ 10^5`
- `1 ≤ pos[i] ≤ 10^5`
- `1 ≤ time[i] ≤ 10^3`
- **Expected Time Complexity:** `O(N)`
- **Expected Auxiliary Space:** `O(1)`

---

## Examples

### Example 1
**Input**

N = 3, cur = 4
pos = [1, 5, 6]
time = [2, 3, 1]

**Output**

2

**Explanation**
- Taxi 1: |4 - 1| × 2 = 6  
- Taxi 2: |5 - 4| × 3 = 3  
- Taxi 3: |6 - 4| × 1 = 2  
Minimum = **2**

---

### Example 2
**Input**

N = 2, cur = 1
pos = [1, 6]
time = [10, 3]

**Output**

0

**Explanation**
- Taxi 1: |1 - 1| × 10 = 0  
- Taxi 2: |6 - 1| × 3 = 15  
Minimum = **0**

---

✅ Time Complexity = `O(N)`  
✅ Space Complexity = `O(1)`

---
