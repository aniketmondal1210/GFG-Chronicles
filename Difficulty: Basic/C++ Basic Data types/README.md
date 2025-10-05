# Identify Basic C++ Data Type and Return Its Size

## 🧩 Problem Statement
Given a **string `S`**, determine which of the following basic **C++ data types** it represents and return its **size in bytes**.

The possible data types are:
1. `Integer` → **4 bytes**  
2. `Float` → **4 bytes**  
3. `Double` → **8 bytes**  
4. `Character` → **1 byte**

---

## Examples

### Example 1
**Input:**  

S = a

**Output:**  

1

**Explanation:**  
`a` is a single character → represents `char` → **size = 1 byte**

---

### Example 2
**Input:**  

S = 98.45685456

**Output:**  

8

**Explanation:**  
The value has many digits after the decimal → represents a **double** → **size = 8 bytes**

---

## Constraints
- 1 ≤ |S| ≤ 10  
- **Expected Time Complexity:** O(N)  
- **Expected Auxiliary Space:** O(1)

---
