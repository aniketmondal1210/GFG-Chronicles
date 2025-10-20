# Find the Minimum Integer X such that S ≤ N × X

## Problem Statement
You are given an array `A` of size `N`.  
Let `S` denote the **sum of all integers** present in the array.  

Your task is to find the **minimum integer X** such that:

S ≤ N × X


---

## Input
- An integer `N` — the size of the array.
- An array `A` of `N` integers.

**Constraints:**

1 ≤ N ≤ 10⁵
1 ≤ A[i] ≤ 10⁹


---

## Output
Return the **minimum integer X** that satisfies the condition `S ≤ N × X`.

---

## Explanation
We can rearrange the condition:

S ≤ N × X ⟹ X ≥ S / N

Since `X` must be an **integer** present in the array `A`,  
we find the **smallest element in A** that is **greater than or equal to** `S / N`.

---

## Examples

### Example 1
**Input:**

N = 3
A = [1, 3, 2]

**Output:**

2

**Explanation:**
Sum `S = 1 + 3 + 2 = 6`  
We need the smallest `X` such that `6 ≤ 3 × X` ⟹ `X ≥ 2`  
Smallest such integer in array is **2**.

---

### Example 2
**Input:**

N = 1
A = [3]

**Output:**

3

**Explanation:**
Sum `S = 3` and `N = 1`,  
so `3 ≤ 1 × X` ⟹ `X ≥ 3`.  
Only possible value is **3**.

---
