# Winner of Election

## Problem Statement
You are given an array of lowercase strings `arr[]`, where each element represents a vote cast for a candidate.  
Your task is to find:
- The candidate with the **maximum votes**.
- The **vote count** of that candidate.

If there is a tie between two or more candidates, return the **lexicographically smallest** candidate name.

You must return the result as an array of strings:
- First element → candidate name  
- Second element → vote count (as a string)

---

## Examples

### Example 1
**Input**:  

arr[] = ["john", "johnny", "jackie", "johnny", "john", "jackie", "jamie", "jamie", "john", "johnny", "jamie", "johnny", "john"]


**Output**:  

["john", "4"]


**Explanation**:  
- "john" has 4 votes.  
- "johnny" also has 4 votes.  
- Since `"john"` < `"johnny"` lexicographically, `"john"` is chosen.

---

### Example 2
**Input**:  

arr[] = ["andy", "blake", "clark"]


**Output**:  

["andy", "1"]


**Explanation**:  
All candidates have 1 vote, but `"andy"` is lexicographically smallest.

---

## Constraints
- `1 <= arr.size() <= 10^5`  
- `1 <= arr[i].size() <= 10^5`

---

## Expected Complexity
- **Time Complexity**: `O(n log n)` (due to sorting or map traversal)  
- **Space Complexity**: `O(n)` (for vote counting)

---
