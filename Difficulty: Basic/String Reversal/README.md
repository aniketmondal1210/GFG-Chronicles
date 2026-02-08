# Reverse String Without Repeating Characters and Spaces

## Problem Statement
You are given a string `S`.  
Your task is to **reverse the string** while:
- **Eliminating all spaces**
- **Removing repeated characters**
- Keeping **only the first occurrence from the reversed order**

Return the modified string.

---

## Example 1

**Input:**

S = "GEEKS FOR GEEKS"


**Output:**

"SKEGROF"


**Explanation:**
- Remove spaces → `"GEEKSFORGEEKS"`
- Reverse the string → `"SKEEGROFSKEEG"`
- Remove repeated characters while traversing from left to right  
  Result → `"SKEGROF"`

---

## Example 2

**Input:**

S = "I AM AWESOME"


**Output:**

"EMOSWAI"


**Explanation:**
- Remove spaces → `"IAMAWESOME"`
- Reverse the string → `"EMOSEWAMAI"`
- Remove repeated characters  
  Result → `"EMOSWAI"`

---

## Expected Time Complexity

O(|S|)


## Expected Auxiliary Space

O(1)


---

## Constraints

- 1 ≤ |S| ≤ 10⁵
- S may contain uppercase letters and spaces


---
