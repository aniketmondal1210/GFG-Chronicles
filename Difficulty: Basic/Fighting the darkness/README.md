# Maximum Days the Room Will Stay Illuminated

You are given an array `arr[]` where each element represents the **size of a candle**.  
Each day, **every candle reduces its size by 1 unit**.

The room remains illuminated as long as **at least one candle has size greater than 0**.

Your task is to determine the **maximum number of days** the room will stay illuminated.

---

## Examples

### Example 1

Input:
arr = [1, 1, 2]

Output:
2


**Explanation:**
- Day 1 → [0, 0, 1]
- Day 2 → [0, 0, 0]  
Room was illuminated for **2 days**.

---

### Example 2

Input:
arr = [2, 3, 4, 2, 1]

Output:
4


**Explanation:**
- The candle with maximum size `4` determines the duration.
- After 4 days, all candles become zero.

---

### Constraints

- 1 ≤ arr.size() ≤ 10^6
- 1 ≤ arr[i] ≤ 10^9

---
