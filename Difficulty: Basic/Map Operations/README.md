# Insert Elements in Map and Erase an Element

---

## Problem Statement
Given an array `arr`, insert each element into a map such that the **element is the key** and its **index is the value**.  
Then erase a given element `x` from the map.  
- Print `"erased x"` if it exists and is erased.  
- Otherwise, print `"not found"`.  
Finally, print the map before and after erasing.  

---

## Example

**Input**  
arr = [9, 8, 7, 4, 4, 2, 1, 1, 9, 8], x = 1  

**Output**

1 7
2 5
4 4
7 2
8 9
9 8
erased 1
2 5
4 4
7 2
8 9
9 8


**Explanation**  
- After inserting: `{1:7, 2:5, 4:4, 7:2, 8:9, 9:8}`  
- After erasing `1`: map becomes `{2:5, 4:4, 7:2, 8:9, 9:8}`  

---
