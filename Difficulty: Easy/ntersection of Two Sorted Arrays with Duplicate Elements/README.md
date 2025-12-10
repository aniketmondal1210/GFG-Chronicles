# Intersection of Two Sorted Arrays (Distinct Elements)

You are given two **sorted arrays** `a[]` and `b[]`, each possibly containing duplicates.  
Your task is to return the **distinct common elements** present in both arrays, in **sorted order**.

---

## Examples

### Example 1

Input:
a = [1, 2, 3, 4, 5]

b = [1, 2, 3, 6, 7]

Output:

1 2 3


### Example 2

Input:
a = [2, 2, 3, 4, 5]

b = [1, 1, 2, 3, 4]

Output:

2 3 4


### Example 3

Input:

a = [1, 1, 1, 1]

b = [2, 2, 2, 2]

Output:
[]


---

### Constraints:
- 1  <=  a.size(), b.size()  <=  10^5
- -10^9  <=  a[i] , b[i]  <=  10^9
