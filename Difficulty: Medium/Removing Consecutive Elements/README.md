# Remove Consecutive Same Special Numbers

You are given an array `arr[]` of positive integers and two special numbers `x` and `y`.  
The task is to **remove all consecutive same occurrences of these special numbers** from the array.  
The final array should be free from any consecutive same special elements.  

👉 The final array may be empty.

---

## Examples

**Input:**  
`arr[] = [2, 1, 2, 2, 2, 5], x = 1, y = 2`  
**Output:**  
`2 1 2 5`  

**Explanation:**  
- Special numbers are `1` and `2`.  
- Original array: `[2, 1, 2, 2, 2, 5]`.  
- Remove consecutive `2`s → `[2, 1, 2, 5]`.  
- Now, no consecutive `1` or `2`.  
- Final answer: `2 1 2 5`.

---

## Constraints
- `1 ≤ arr.size() ≤ 10^5`  
- `1 ≤ arr[i] ≤ 10^5`  
- `1 ≤ x, y ≤ 10^5`  

---
