# Maximum Diamonds in K Minutes

## Problem
You are given `n` bags, where the `i`-th bag contains `arr[i]` diamonds.  
In 1 minute, you may choose a bag, collect all diamonds from it, and then the bag refills with `⌊arr[i] / 2⌋` diamonds.

Find the **maximum number of diamonds** you can collect in `k` minutes.

---

### Examples

#### Input:

arr = [2, 1, 7, 4, 2], k = 3

#### Output:

14

#### Explanation:
- Take from bag with 7 → gain 7, bag becomes 3  
- Take from bag with 4 → gain 4, bag becomes 2  
- Take from bag with 3 → gain 3, bag becomes 1  
Total = 14

---

#### Input:

arr = [7, 1, 2], k = 2

#### Output:

10

#### Explanation:
- Take from bag with 7 → gain 7, bag becomes 3  
- Take from bag with 3 → gain 3, bag becomes 1  
Total = 10  

---

### Constraints
- `1 ≤ n ≤ 10^5`  
- `0 ≤ k, arr[i] ≤ 10^5`  

---
