# Total Fine on Given Date

## Problem Statement

You are given:
- An array of car numbers `car[]`
- An array of penalties `fine[]`
- An integer value `date`

The fine is collected based on the following rule:
- On **even** dates, collect fine from cars with **odd** numbers.
- On **odd** dates, collect fine from cars with **even** numbers.

Your task is to calculate the **total fine collected** on the given date.

---

## Examples

### Example 1  
**Input:**  
`date = 12`  
`car[] = [2375, 7682, 2325, 2352]`  
`fine[] = [250, 500, 350, 200]`  
**Output:**  
`600`  
**Explanation:**  
Date is even → collect from odd-numbered cars:  
- 2375 → 250  
- 2325 → 350  
Total fine = 250 + 350 = 600

---

### Example 2  
**Input:**  
`date = 8`  
`car[] = [2222, 2223, 2224]`  
`fine[] = [200, 300, 400]`  
**Output:**  
`300`  
**Explanation:**  
Date is even → collect from odd-numbered cars:  
- 2223 → 300  
Total fine = 300

---

## Constraints

- `1 ≤ car.size ≤ 10^5`
- `1 ≤ car[i], fine[i], date ≤ 10^5`

---
