# Convert Sentence to Camel Case

## Problem Statement
Given a sentence `s`, your task is to **remove all spaces** and convert it into **Camel Case**.  

In Camel Case:
- Words are joined without spaces.  
- The **first word** keeps its original case.  
- Each **subsequent word** starts with an uppercase letter.  

It is guaranteed that the input string has no leading spaces.  

---

## Examples

### Example 1
**Input:**  

s = "i got intern at geeksforgeeks"

**Output:**  

iGotInternAtGeeksforgeeks

**Explanation:**  
- Words = ["i", "got", "intern", "at", "geeksforgeeks"]  
- First word → "i" (no change).  
- Remaining words → capitalize first letter.  
- Joined result = **"iGotInternAtGeeksforgeeks"**  

---

### Example 2
**Input:**  

s = "here comes the garden"

**Output:**  

hereComesTheGarden

**Explanation:**  
- First word = "here".  
- Next words → "Comes", "The", "Garden".  
- Final string = **"hereComesTheGarden"**  

---

### Example 3
**Input:**  

s = "coding is fun"

**Output:**  

codingIsFun


---

## Constraints
- `1 <= s.size() <= 10^6`  
- The string `s` contains only **lowercase English alphabets** and **spaces**.  

---
