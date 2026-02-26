# Balanced Number

## Problem Statement

Given a number `N` (as a string) having an **odd number of digits**, determine whether it is a **Balanced Number**.

A number is called **balanced** if:

- The sum of digits to the **left of the middle digit**
- Equals the sum of digits to the **right of the middle digit**

Return:

- `true` → if balanced  
- `false` → otherwise  

The driver code prints:
- `1` if true  
- `0` if false  

---

## Examples

### Example 1

**Input**
```
N = 1234006
```

**Explanation**
- Total digits = 7  
- Middle digit = 4  
- Left sum = 1 + 2 + 3 = 6  
- Right sum = 0 + 0 + 6 = 6  

Since both sums are equal → Balanced  

**Output**
```
1
```

---

### Example 2

**Input**
```
N = 12345
```

**Explanation**
- Middle digit = 3  
- Left sum = 1 + 2 = 3  
- Right sum = 4 + 5 = 9  

Not equal → Not balanced  

**Output**
```
0
```

---

## Time Complexity

```
O(n)
```
Where `n` is number of digits in `N`.

---

## Auxiliary Space

```
O(1)
```
Only a few variables are used.

---
