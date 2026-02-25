# Vector Operations Implementation

## Problem Summary

We need to perform multiple queries on a vector **A**.

### Query Types

| Query | Operation |
|--------|------------|
| `a x` | Add element `x` at the end |
| `b` | Sort vector in ascending order |
| `c` | Reverse the vector |
| `d` | Print size of vector |
| `e` | Print elements of vector |
| `f` | Sort vector in descending order |

---

## Example

### Input Queries
```
a 4 a 6 a 7 b c e
```

### Output
```
7 6 4
```

---

## Complexity

- Add → O(1)
- Sort → O(N log N)
- Reverse → O(N)
- Size → O(1)
- Print → O(N)

---
