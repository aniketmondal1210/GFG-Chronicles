# Maximum Sum by Selecting k Elements with Highest Frequency

## Problem
You are given:  
- An integer array `arr[]`  
- An integer `k`  

Your task is to **select exactly `k` integers** from the array such that:  
1. You can only select elements with the **maximum frequency** at each step.  
2. Once selected, the chosen element is removed (frequency decreases by 1).  
3. If multiple elements have the same maximum frequency, you can choose any.  
4. Your goal is to **maximize the sum**.

---

## Examples

### Example 1
**Input:**  

k = 3
arr = [1, 1, 2, 3, 3]


**Output:**  

7


**Explanation:**  
- Initially: freq(1) = 2, freq(3) = 2 → max frequency = 2.  
  Pick `3`. Sum = 3.  
- Now freq(1) = 2, freq(3) = 1 → pick `1`. Sum = 3+1=4.  
- Now freq(1) = 1, freq(3) = 1 → pick the larger (3). Sum = 4+3=7.  

✅ Answer = 7.

---

### Example 2
**Input:**  

k = 4
arr = [4, 4, 4, 2, 2, 6]


**Output:**  

16


**Explanation:**  
- freq(4)=3, freq(2)=2, freq(6)=1  
- Pick `4` three times → sum = 12.  
- One pick left → pick `2`.  
✅ Final sum = 16.

---

## Constraints
- `1 ≤ k ≤ arr.size() ≤ 10^5`  
- `1 ≤ arr[i] ≤ 10^5`

---
