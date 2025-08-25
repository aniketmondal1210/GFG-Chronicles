# Restaurant Menu Fight Check

## Problem Statement  
Two restaurants each have a menu of 5 items. There may be a **chance of fight** if **any one of them have an item in common**.  
Your task is to check:  
- If any item is common → return `"CHANGE"`.  
- If no item is common → return `"BEHAPPY"`.  

---

## Examples  

### Example 1
**Input:**  

cake pastry fish candy meat
burger ham fish cake sauce


**Output:**  

CHANGE


**Explanation:**  
The item `"fish"` is common in both menus. Hence output is **CHANGE**.  

---

### Example 2
**Input:**  

pizza chicken cake chilli candy
choco coco cabbage panner cheese


**Output:**  

BEHAPPY


**Explanation:**  
No item is common in both menus. Hence output is **BEHAPPY**.  

---

## Constraints
- Each menu contains exactly **5 items**.  
- `1 <= Size of each string <= 1000`  

---
