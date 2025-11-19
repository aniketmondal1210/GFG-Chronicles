# Count Buildings That Can See the Sunrise

## Problem Statement
You are given an array `height[]` representing the heights of buildings.  
The sun rises from the **left side** (starting point of the array).

A building can see the sunrise if and only if its height is **strictly greater** than all the buildings to its left.

Your task is to count how many buildings can see the sunrise.

---

## Example 1
**Input:**

height = [7, 4, 8, 2, 9]


**Output:**

3


**Explanation:**
- 7 can see the sunrise (first building)  
- 4 cannot (blocked by 7)  
- 8 can see (greater than 7)  
- 2 cannot (blocked by 8)  
- 9 can see (greater than all previous)

Total buildings that see the sunrise = **3**

---

## Example 2
**Input:**

height = [2, 3, 4, 5]


**Output:**

4


**Explanation:**  
All buildings are increasing in height, so all can see the sunrise.

---

## Expected Time Complexity

O(n)


## Expected Auxiliary Space

O(1)


---

## Constraints

1 ≤ height.size() ≤ 10⁶
1 ≤ height[i] ≤ 10⁸


---
