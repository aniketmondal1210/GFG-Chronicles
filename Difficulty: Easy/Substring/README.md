# Substring from L to R

## Problem Statement

Given a string **S** and two integers **L** and **R**, return the substring containing characters from **index L to R (inclusive)**.

- Indexing is **0-based**.
- The substring must include both **L and R** positions.

---

## Examples

### Example 1

**Input**
```
S = "cdbkdub"
L = 0
R = 5
```

**Output**
```
"cdbkdu"
```

**Explanation**

Characters from index **0 to 5**:

```
c d b k d u
```

---

### Example 2

**Input**
```
S = "sdiblcsdbud"
L = 3
R = 7
```

**Output**
```
"blcsd"
```

**Explanation**

Characters from index **3 to 7**:

```
b l c s d
```

---

## Expected Time Complexity: O(|S|)

## Expected Auxiliary Space: O(|S|)

## Constraints:

- 1<= |S| <=1000
- 1 <= L <= 800
- 1 <= R <= 900

---
