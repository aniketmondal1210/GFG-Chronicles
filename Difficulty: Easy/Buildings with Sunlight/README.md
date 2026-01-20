# Buildings Receiving Sunlight

## Problem Statement
You are given an array `arr[]` representing the **heights of buildings** arranged adjacent to each other in a straight line.

☀️ Sunlight falls from the **left side**.

A building can **receive sunlight** if **no building to its left** has a height **greater than or equal to it**.

Your task is to find the **total number of buildings** that can see the sunlight.

---

## Examples

### Example 1
**Input**

arr = [6, 2, 8, 4, 11, 13]


**Output**

4


**Explanation**
Buildings with heights **6, 8, 11, 13** receive sunlight.

---

### Example 2
**Input**

arr = [2, 5, 1, 8, 3]


**Output**

3


**Explanation**
Buildings with heights **2, 5, 8** receive sunlight.

---

### Example 3
**Input**

arr = [3, 4, 1, 0, 6, 2, 3]


**Output**

3


---

## Time and Space Complexity
- **Time Complexity:** `O(n)`
- **Auxiliary Space:** `O(1)`

---

## Constraints

- 1 ≤ arr.size() ≤ 10^5
- 1 ≤ arr[i] ≤ 10^5


---
