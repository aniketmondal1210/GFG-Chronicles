# Insert Elements of an Array into a Forward List

You are given an array `arr[]`.  
The task is to **insert the elements of this array into a forward list**.

---

## 🔹 Key Concept
- A **forward_list** in C++ is a **singly-linked list** that supports fast insertion and removal from the front.  
- If we insert elements using `push_front()`, the elements will be **stored in reverse order** compared to the input sequence.

---

## 🔹 Examples

### Example 1
**Input:**  

arr = [1, 2, 3, 4, 5]


**Output:**  

5 4 3 2 1


**Explanation:**  
Each element is inserted using `push_front()`. The last inserted element (`5`) appears first.

---

### Example 2
**Input:**  

arr = [2, 1, 5]


**Output:**  

5 1 2


**Explanation:**  
`push_front()` reverses the insertion order.

---
