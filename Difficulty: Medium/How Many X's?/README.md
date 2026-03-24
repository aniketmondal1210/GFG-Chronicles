# Count Occurrences of Digit X in Range (L, R)

## Problem Statement

Given integers `L`, `R`, and digit `X`, count how many times digit `X` appears in all numbers **strictly between L and R**.

Range:
```
(L, R) → excludes L and R
```

---

# Examples

### Example 1

**Input**
```
L = 10, R = 19, X = 1
```

**Numbers in range**
```
11, 12, 13, 14, 15, 16, 17, 18
```

Occurrences of `1`:
```
11 → 2
12 → 1
13 → 1
14 → 1
15 → 1
16 → 1
17 → 1
18 → 1
```

**Total = 9**

**Output**
```
9
```

---

### Example 2

**Input**
```
L = 18, R = 81, X = 9
```

**Output**
```
7
```

---

## Expected Time Complexity:O(RLogR)
## Expected Auxillary Space:O(1)

## Constraints:

- 1 <= L< R <= 105
- 0 <= X <= 9 

---
