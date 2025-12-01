# Multiset Operations

## Problem Statement
You are given an array **A** of size **N**.  
Your task is to:

1. Insert all elements of the array into a **multiset**.  
2. Print all the elements of the multiset in sorted order.
3. Erase a given element **x** from the multiset.
4. Print:
   - `"erased x"` if the element was successfully removed.
   - `"not found"` if the element does not exist.
5. Print the multiset again after deletion.

---

## Example

### Input

N = 10
A = 9 8 7 4 4 2 1 1 9 8
x = 1


### Output

1 1 2 4 4 7 8 8 9 9
erased 1
2 4 4 7 8 8 9 9


### Explanation
- After inserting into a multiset → elements are automatically sorted.
- Erase one occurrence of `1` → print `"erased 1"`.
- Print remaining elements.

---

## Functions to Implement
You must complete the following functions:

- `multisetInsert(ms, A)`
- `multisetErase(ms, x)`
- `multisetDisplay(ms)`

Where:

- `ms` is the multiset
- `A` is the input array
- `x` is the element to delete

---

## Constraints

- 1 ≤ N ≤ 1000
- 1 ≤ Ai ≤ 10⁶


--- 
