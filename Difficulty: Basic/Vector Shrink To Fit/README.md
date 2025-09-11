# Vector Resize and Shrink to Fit

We are given a **vector** and a **new size**.  
The task is to:
1. Print the **current size of the vector** before resizing.  
2. Use `resize(newsize)` to change its size.  
3. Apply `shrink_to_fit()` to minimize capacity.  
4. Print the size after resizing.

---

## 🔹 STL Functions Used

- **`resize(n)`**  
  Resizes the container so that it contains `n` elements.  

- **`shrink_to_fit()`**  
  Requests the container to reduce its capacity to fit its size.  

---

## 🔹 Example

### Input

1
20
10


### Output

20
10


**Explanation:**  
- Initial size = 20  
- After resizing to 10 and applying `shrink_to_fit()`, new size = 10  

---
